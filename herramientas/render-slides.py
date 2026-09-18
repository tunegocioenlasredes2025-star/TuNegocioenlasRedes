#!/usr/bin/env python3
"""
render-slides.py — Exporta slides de un HTML a PNG usando Chromium de verdad.

POR QUÉ EXISTE
    El botón de descarga de las plantillas de carrusel usa html2canvas, que no
    rasteriza con el motor del navegador: vuelve a medir el texto por su cuenta
    y lo redibuja. Cuando hay `letter-spacing`, esa medición se desfasa y produce
    los tres síntomas juntos:

      · los espacios entre palabras desaparecen  ("hicimosquecadaconsulta")
      · los fondos de texto resaltado quedan corridos respecto de las letras
      · esos fondos se pintan de negro, porque html2canvas no soporta gradientes
        ni `box-decoration-break` en elementos inline

    Chromium headless no tiene ninguno de esos problemas: rasteriza el DOM real.
    Mismo HTML, mismo CSS, sin tocar el diseño.

USO
    python3 herramientas/render-slides.py carrusel.html
    python3 herramientas/render-slides.py carrusel.html --selector ".slide"
    python3 herramientas/render-slides.py carrusel.html --salida ./png --escala 3
    python3 herramientas/render-slides.py carrusel.html --diagnostico

REQUISITOS
    pip install playwright
"""

import argparse
import pathlib
import re
import shutil
import subprocess
import sys

# Chromium ya instalado en el entorno; si no está, Playwright usa el suyo.
CHROME_PREINSTALADO = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# Selectores habituales en plantillas de carrusel, del más específico al más laxo.
CANDIDATOS = [
    "[data-slide]", ".slide", ".pieza", ".canvas", ".card",
    ".post", "section.slide", "article.slide", "body > section",
]

ANCHO_MINIMO = 500      # por debajo de esto no es un lienzo, es un componente


def buscar_chrome() -> str | None:
    if pathlib.Path(CHROME_PREINSTALADO).exists():
        return CHROME_PREINSTALADO
    return None


def diagnosticar(html: pathlib.Path) -> None:
    """Revisa el HTML y reporta lo que suele romper la exportación."""
    texto = html.read_text(encoding="utf-8", errors="ignore")
    print(f"\nDiagnóstico de {html.name}\n" + "─" * 46)

    hallazgos = []
    if re.search(r"html2canvas", texto, re.I):
        hallazgos.append(
            "html2canvas está en el archivo. Es la causa de los espacios que se\n"
            "    comen y de los resaltados en negro. Exportá con este script."
        )
    if re.search(r"fonts\.googleapis\.com|fonts\.gstatic\.com", texto):
        hallazgos.append(
            "Las fuentes se cargan desde CDN. Si al exportar no llegaron todavía,\n"
            "    el render sale con la fuente de reserva. Conviene embeberlas en base64."
        )
    if re.search(r"background-clip\s*:\s*text|mix-blend-mode", texto):
        hallazgos.append(
            "Hay background-clip:text o mix-blend-mode. Chromium los dibuja bien;\n"
            "    html2canvas no."
        )

    if hallazgos:
        for h in hallazgos:
            print(f"  • {h}")
    else:
        print("  Sin problemas conocidos de exportación.")
    print()


def detectar_selector(pagina) -> str:
    """Elige el selector cuyos elementos parecen lienzos: varios y del mismo tamaño."""
    mejor, mejor_puntaje = None, -1
    for selector in CANDIDATOS:
        cajas = pagina.evaluate(
            """(sel) => [...document.querySelectorAll(sel)]
                 .map(e => { const r = e.getBoundingClientRect();
                             return {w: Math.round(r.width), h: Math.round(r.height)}; })""",
            selector,
        )
        cajas = [c for c in cajas if c["w"] >= ANCHO_MINIMO and c["h"] >= ANCHO_MINIMO]
        if not cajas:
            continue
        # Puntaje: cantidad de elementos, con premio si todos miden igual.
        uniformes = len({(c["w"], c["h"]) for c in cajas}) == 1
        puntaje = len(cajas) + (10 if uniformes else 0)
        if puntaje > mejor_puntaje:
            mejor, mejor_puntaje = selector, puntaje
    return mejor


def comprimir(archivo: pathlib.Path) -> None:
    if not shutil.which("pngquant"):
        return
    subprocess.run(
        ["pngquant", "--quality", "80-98", "--speed", "1",
         "--force", "--output", str(archivo), str(archivo)],
        check=False, stderr=subprocess.DEVNULL,
    )


def renderizar(html: pathlib.Path, selector: str | None,
               salida: pathlib.Path, escala: float, comprimido: bool) -> int:
    from playwright.sync_api import sync_playwright

    salida.mkdir(parents=True, exist_ok=True)
    chrome = buscar_chrome()

    with sync_playwright() as p:
        navegador = p.chromium.launch(
            executable_path=chrome,
            args=["--no-sandbox", "--force-color-profile=srgb",
                  "--font-render-hinting=none", "--disable-lcd-text"],
        )
        pagina = navegador.new_page(
            viewport={"width": 1400, "height": 1400},
            device_scale_factor=escala,
        )
        pagina.goto("file://" + str(html.resolve()))

        # Clave: esperar a las fuentes ANTES de capturar. Sin esto el PNG puede
        # salir con la tipografía de reserva y el interlineado corrido.
        pagina.wait_for_load_state("networkidle")
        pagina.evaluate("() => document.fonts.ready")
        pagina.wait_for_timeout(600)

        if not selector:
            selector = detectar_selector(pagina)
            if not selector:
                navegador.close()
                sys.exit(
                    "No encontré los slides solos. Pasá el selector a mano:\n"
                    "  --selector \".mi-slide\""
                )
            print(f"   selector detectado: {selector}")

        elementos = pagina.query_selector_all(selector)
        elementos = [e for e in elementos if (e.bounding_box() or {}).get("width", 0) >= ANCHO_MINIMO]
        if not elementos:
            navegador.close()
            sys.exit(f"El selector «{selector}» no devolvió ningún lienzo.")

        base = html.stem
        for i, elemento in enumerate(elementos, 1):
            destino = salida / f"{base}-{i:02d}.png"
            elemento.scroll_into_view_if_needed()
            elemento.screenshot(path=str(destino))
            if comprimido:
                comprimir(destino)
            caja = elemento.bounding_box()
            print(f"   ✔ {destino.name}  ({int(caja['width'])}×{int(caja['height'])} "
                  f"→ {int(caja['width']*escala)}×{int(caja['height']*escala)})")

        navegador.close()
        return len(elementos)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", help="el HTML del carrusel")
    ap.add_argument("--selector", help="selector CSS de cada slide (por defecto lo detecta)")
    ap.add_argument("--salida", default=None, help="carpeta destino (por defecto ./png junto al HTML)")
    ap.add_argument("--escala", type=float, default=2, help="factor de pixel ratio (por defecto 2)")
    ap.add_argument("--sin-comprimir", action="store_true", help="no pasar pngquant")
    ap.add_argument("--diagnostico", action="store_true", help="solo revisar el HTML, sin renderizar")
    args = ap.parse_args()

    html = pathlib.Path(args.html)
    if not html.exists():
        sys.exit(f"No existe {html}")

    diagnosticar(html)
    if args.diagnostico:
        return

    salida = pathlib.Path(args.salida) if args.salida else html.parent / "png"
    print(f"→ renderizando {html.name}")
    total = renderizar(html, args.selector, salida, args.escala, not args.sin_comprimir)
    print(f"\nListo: {total} slide(s) en {salida}/")


if __name__ == "__main__":
    main()
