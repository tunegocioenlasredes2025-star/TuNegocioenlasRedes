#!/usr/bin/env python3
"""
generar.py — Estáticas de Instagram para infoseguridadAR.

Modelo: cada nota publicada en infoseguridadit.com sale como una estática 1080x1350
que invita a leerla en el link de la bio.

USO
    python3 generar.py                 # genera todas las notas de notas.json
    python3 generar.py aliara onvif    # genera solo esos ids
    python3 generar.py --html          # deja solo el HTML (sin renderizar PNG)

ENTRADA   notas.json  (ver SISTEMA-VISUAL.md para el esquema)
SALIDA    salida/<id>.png  +  salida/preview.html  +  salida/contacto-hoja.png
"""

import base64
import html as html_mod
import json
import pathlib
import re
import shutil
import subprocess
import sys

RAIZ = pathlib.Path(__file__).parent
SALIDA = RAIZ / "salida"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

ANCHO, ALTO = 1080, 1350


# ── Ajuste tipográfico ──────────────────────────────────────────────────────
# El titular es el único elemento de tamaño variable: se achica en escalones
# según el largo para que nunca desborde ni quede raquítico.
ESCALONES = [
    (42, 113),  # hasta 42 caracteres -> 113px
    (58, 102),
    (74, 92),
    (92, 83),
    (112, 75),
    (999, 67),
]


def tamano_titular(texto: str) -> int:
    largo = len(re.sub(r"<[^>]+>", "", texto))
    for tope, px in ESCALONES:
        if largo <= tope:
            return px
    return ESCALONES[-1][1]


def destacar(titular: str, palabra: str | None) -> str:
    """Pinta de verde la palabra/frase elegida dentro del titular."""
    seguro = html_mod.escape(titular)
    if not palabra:
        return seguro
    objetivo = html_mod.escape(palabra)
    if objetivo not in seguro:
        print(f"   ! aviso: no encontré «{palabra}» en el titular, va sin destacado")
        return seguro
    return seguro.replace(objetivo, f"<em>{objetivo}</em>", 1)


def foto_data_uri(nombre: str | None) -> str:
    """Embebe la foto en base64 para que el HTML sea 100% autónomo."""
    if not nombre:
        return ""
    ruta = RAIZ / "fotos" / nombre
    if not ruta.exists():
        print(f"   ! falta la foto {ruta.name}, la pieza sale en modo tipográfico")
        return ""
    tipo = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(
        ruta.suffix.lstrip(".").lower(), "jpeg"
    )
    return f"data:image/{tipo};base64,{base64.b64encode(ruta.read_bytes()).decode()}"


def _cache(fn):
    guardado = {}
    def envuelto():
        if "v" not in guardado:
            guardado["v"] = fn()
        return guardado["v"]
    return envuelto


@_cache
def logo_data_uri() -> str:
    """El logo vectorial va embebido: el HTML queda autónomo y el PNG nítido."""
    svg = (RAIZ / "logo-infoseguridad.svg").read_bytes()
    return "data:image/svg+xml;base64," + base64.b64encode(svg).decode()


@_cache
def fuentes_css() -> str:
    """Inter + JetBrains Mono en base64. Nunca CDN: el render no depende de internet."""
    return (RAIZ / "fonts_embedded.css").read_text(encoding="utf-8")


def pieza_html(nota: dict) -> str:
    foto = foto_data_uri(nota.get("foto"))
    titular = destacar(nota["titular"], nota.get("destacar"))
    encuadre = nota.get("encuadre", "center")

    estilo_foto = (
        f"background-image:url('{foto}');background-position:{encuadre};"
        if foto
        else ""
    )
    bajada = (
        f'<p class="bajada">{html_mod.escape(nota["bajada"])}</p>'
        if nota.get("bajada")
        else ""
    )

    LOGO = logo_data_uri()
    return f"""
<div class="pieza{'' if foto else ' sin-foto'}" data-id="{html_mod.escape(nota['id'])}">
  <div class="foto" style="{estilo_foto}"></div>

  <div class="barra">
    <span class="rubro">{html_mod.escape(nota.get('rubro', 'NOTA'))}</span>
    <span class="sep"></span>
    <span class="sello">{html_mod.escape(nota.get('sello', 'NOTA NUEVA'))}</span>
  </div>

  <div class="contenido">
    <h1 class="titular" style="--titular-size:{tamano_titular(nota['titular'])}px">{titular}</h1>
    {bajada}
    <div class="pie">
      <span class="cta">
        <svg viewBox="0 0 34 18" fill="none" aria-hidden="true">
          <path d="M0 9h30M23 2l8 7-8 7" stroke="currentColor" stroke-width="2.6"
                stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        {html_mod.escape(nota.get('cta', 'Nota completa en el link de la bio'))}
      </span>
      <span class="marca">
        <img src="{LOGO}" alt="infoseguridadAR">
        <span class="dominio">infoseguridadit.com</span>
      </span>
    </div>
  </div>
</div>"""


def construir(notas: list[dict]) -> pathlib.Path:
    plantilla = (RAIZ / "plantilla.html").read_text(encoding="utf-8")
    plantilla = plantilla.replace("/*__FUENTES__*/", fuentes_css())
    cuerpo = "\n".join(pieza_html(n) for n in notas)
    doc = re.sub(
        r"<!-- ▼▼.*?</body>",
        cuerpo + "\n</body>",
        plantilla,
        flags=re.S,
    )
    SALIDA.mkdir(exist_ok=True)
    destino = SALIDA / "preview.html"
    destino.write_text(doc, encoding="utf-8")
    return destino


def renderizar(pagina_html: pathlib.Path, notas: list[dict]) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        navegador = p.chromium.launch(
            executable_path=CHROME,
            args=[
                "--no-sandbox",
                "--force-color-profile=srgb",
                "--font-render-hinting=none",
                "--disable-lcd-text",
            ],
        )
        pagina = navegador.new_page(
            viewport={"width": ANCHO + 120, "height": ALTO},
            device_scale_factor=2,           # PNG retina 2160x2700
        )
        pagina.goto("file://" + str(pagina_html.resolve()))
        pagina.wait_for_timeout(900)

        for nota in notas:
            elemento = pagina.query_selector(f'.pieza[data-id="{nota["id"]}"]')
            destino = SALIDA / f"{nota['id']}.png"
            elemento.screenshot(path=str(destino))
            comprimir(destino)
            print(f"   ✔ {destino.name}")

        navegador.close()


def comprimir(destino: pathlib.Path) -> None:
    """Cuantiza el PNG si hay pngquant. Arte plana: baja ~80% sin pérdida visible."""
    if not shutil.which("pngquant"):
        return
    subprocess.run(
        ["pngquant", "--quality", "82-98", "--speed", "1",
         "--force", "--output", str(destino), str(destino)],
        check=False,
        stderr=subprocess.DEVNULL,
    )


def hoja_de_contacto(notas: list[dict], columnas: int = 4) -> None:
    """Montaje de todas las piezas en una sola imagen, para revisar de un vistazo."""
    try:
        from PIL import Image
    except ImportError:
        return

    ancho, alto, borde = 360, 450, 12
    filas = (len(notas) + columnas - 1) // columnas
    hoja = Image.new(
        "RGB",
        (columnas * ancho + (columnas + 1) * borde, filas * alto + (filas + 1) * borde),
        (26, 28, 31),
    )
    for i, nota in enumerate(notas):
        archivo = SALIDA / f"{nota['id']}.png"
        if not archivo.exists():
            continue
        miniatura = Image.open(archivo).convert("RGB").resize((ancho, alto), Image.LANCZOS)
        fila, columna = divmod(i, columnas)
        hoja.paste(
            miniatura,
            (borde + columna * (ancho + borde), borde + fila * (alto + borde)),
        )
    destino = SALIDA / "contacto-hoja.png"
    hoja.save(destino)
    print(f"   ✔ {destino.name}")


def main() -> None:
    argumentos = [a for a in sys.argv[1:] if not a.startswith("--")]
    solo_html = "--html" in sys.argv

    notas = json.loads((RAIZ / "notas.json").read_text(encoding="utf-8"))["notas"]
    if argumentos:
        notas = [n for n in notas if n["id"] in argumentos]
        if not notas:
            sys.exit(f"No encontré ninguna nota con esos ids: {', '.join(argumentos)}")

    print(f"→ {len(notas)} pieza(s)")
    pagina = construir(notas)
    print(f"   ✔ {pagina.relative_to(RAIZ)}")

    if not solo_html:
        renderizar(pagina, notas)

        hoja_de_contacto(notas)

    print(f"\nListo. Los PNG quedaron en {SALIDA.relative_to(RAIZ)}/")


if __name__ == "__main__":
    main()
