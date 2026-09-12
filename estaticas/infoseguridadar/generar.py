#!/usr/bin/env python3
"""
InfoSeguridadAR — generador de estaticas 1080x1350 para Instagram.

Lee notas.json, arma un HTML standalone por nota (fuentes y fotos embebidas
en base64, sin dependencias de internet) y lo renderiza a PNG con Chromium.

Uso:
    python3 generar.py            # HTML + PNG de todas las notas
    python3 generar.py --solo-html
"""
import base64
import json
import pathlib
import re
import sys

BASE = pathlib.Path(__file__).parent
OUT = BASE / "out"
FOTOS = BASE / "fotos"

W, H = 1080, 1350          # formato 4:5 de Instagram
ESCALA = 2                 # PNG retina -> 2160x2700


# ---------------------------------------------------------------- utilidades
def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def slug(texto: str) -> str:
    t = texto.lower()
    for a, b in zip("áéíóúüñ", "aeiouun"):
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:48]


def mime(path: pathlib.Path) -> str:
    return {".png": "image/png", ".webp": "image/webp"}.get(
        path.suffix.lower(), "image/jpeg"
    )


def resaltar(texto: str) -> str:
    """*palabra* -> palabra en verde."""
    texto = (texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", texto)


# -------------------------------------------------------------------- assets
FUENTES = {
    "var": b64(BASE / "fonts" / "archivo-var.woff2"),
    "black": b64(BASE / "fonts" / "archivo-black.woff2"),
}

_logo = next((p for p in [BASE / "logo.png", BASE / "logo.svg"] if p.exists()), None)


def bloque_logo() -> str:
    """Logo real si el usuario lo dejo en la carpeta; si no, reconstruccion CSS."""
    if _logo and _logo.suffix == ".png":
        return f'<img class="logo-img" src="data:image/png;base64,{b64(_logo)}">'
    if _logo:
        return f'<img class="logo-img" src="data:image/svg+xml;base64,{b64(_logo)}">'
    return """
    <div class="logo">
      <div class="logo-badge">info</div>
      <div class="logo-txt">
        <span class="logo-portal">PORTAL DE NOTICIAS</span>
        <span class="logo-word">seguridad<b>AR</b></span>
      </div>
    </div>"""


# ------------------------------------------------------------------ template
PLANTILLA = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>__TITULO__</title>
<style>
@font-face{font-family:'Archivo';src:url(data:font/woff2;base64,__VAR__) format('woff2-variations');
  font-weight:100 900;font-stretch:62% 125%;font-display:block}
@font-face{font-family:'Archivo Black';src:url(data:font/woff2;base64,__BLACK__) format('woff2');
  font-weight:400;font-display:block}

:root{
  --negro:#000000;
  --verde:#2BE06B;
  --blanco:#FFFFFF;
  --gris:#B6BDC1;
  --gris-tenue:#6E7679;
  --linea:#2A2E30;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#101214;font-family:'Archivo',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
body{display:flex;align-items:flex-start;justify-content:center}

.card{
  width:1080px;height:1350px;background:var(--negro);color:var(--blanco);
  padding:52px 56px 44px;display:flex;flex-direction:column;overflow:hidden;position:relative;
}

/* ---- barra superior: categoria + NOTA NUEVA ---- */
.topbar{display:flex;align-items:center;gap:22px;flex:0 0 auto}
.chip{background:var(--verde);color:#000;font-weight:800;font-size:23px;line-height:1;
  letter-spacing:.055em;text-transform:uppercase;padding:11px 17px 10px;border-radius:5px}
.sep{width:2px;height:26px;background:#3A3F42}
.kicker{font-weight:700;font-size:23px;letter-spacing:.075em;text-transform:uppercase;color:#fff}

/* ---- foto ---- */
.media{margin-top:30px;flex:0 0 auto;height:566px;border-radius:16px;overflow:hidden;position:relative}
.media img{width:100%;height:100%;object-fit:cover;display:block}

/* portada tipografica cuando no hay foto */
.media.sinfoto{background:
  radial-gradient(120% 100% at 18% 0%, rgba(43,224,107,.30) 0%, rgba(43,224,107,0) 58%),
  radial-gradient(90% 80% at 100% 100%, rgba(43,224,107,.12) 0%, rgba(0,0,0,0) 60%),
  linear-gradient(160deg,#0D1512 0%,#050706 55%,#0A0F0D 100%);
  display:flex;align-items:flex-end;padding:40px 44px}
.media.sinfoto::before{content:'';position:absolute;inset:0;opacity:.16;
  background-image:linear-gradient(rgba(43,224,107,.55) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(43,224,107,.55) 1px,transparent 1px);
  background-size:64px 64px;
  -webkit-mask-image:radial-gradient(120% 90% at 20% 10%,#000 0%,transparent 70%)}
.media.sinfoto .marca-agua{font-family:'Archivo Black',sans-serif;font-size:104px;line-height:.88;
  letter-spacing:-.035em;color:rgba(255,255,255,.09);text-transform:uppercase;position:relative}

/* ---- texto ---- */
.titular{margin-top:34px;flex:0 0 auto;text-align:left;font-weight:900;font-stretch:92%;
  font-size:88px;line-height:.95;letter-spacing:-.022em;color:#fff;text-wrap:balance}
.titular em{font-style:normal;color:var(--verde)}
.bajada{margin-top:22px;flex:0 0 auto;text-align:left;font-weight:400;font-size:30px;
  line-height:1.33;letter-spacing:-.005em;color:var(--gris);max-width:92%}

.aire{flex:1 1 auto;min-height:48px}

/* ---- pie ---- */
.fila-logo{display:flex;justify-content:flex-end;align-items:flex-end;flex:0 0 auto;padding-bottom:20px}
.logo-img{height:62px;width:auto;display:block}
.logo{display:flex;align-items:center;gap:9px}
.logo-badge{background:var(--verde);color:#000;font-weight:800;font-size:31px;line-height:1;
  padding:9px 11px 8px;border-radius:7px;letter-spacing:-.02em}
.logo-txt{display:flex;flex-direction:column;gap:3px}
.logo-portal{font-size:11px;font-weight:700;letter-spacing:.26em;color:#fff;
  background:var(--verde);color:#000;padding:2px 6px;border-radius:3px;align-self:flex-start}
.logo-word{font-weight:800;font-size:31px;line-height:1;letter-spacing:-.025em;color:#fff}
.logo-word b{color:var(--verde);font-weight:800}

.regla{height:2px;background:var(--verde);opacity:.85;flex:0 0 auto}
.fila-cta{display:flex;justify-content:space-between;align-items:center;margin-top:22px;flex:0 0 auto}
.cta{display:flex;align-items:center;gap:16px;color:var(--verde);font-weight:600;font-size:29px;
  letter-spacing:-.01em}
.flecha{font-family:'Archivo',sans-serif;font-weight:500;font-size:34px;line-height:1;transform:translateY(-1px)}
.sitio{font-size:22px;font-weight:400;color:var(--gris-tenue);letter-spacing:.01em}
</style></head>
<body>
<div class="card" id="card">
  <div class="topbar">
    <span class="chip">__CATEGORIA__</span>
    <span class="sep"></span>
    <span class="kicker">__ETIQUETA__</span>
  </div>

  __MEDIA__

  <h1 class="titular" id="titular">__TITULAR__</h1>
  <p class="bajada" id="bajada">__BAJADA__</p>

  <div class="aire"></div>

  <div class="fila-logo">__LOGO__</div>
  <div class="regla"></div>
  <div class="fila-cta">
    <span class="cta"><span class="flecha">&#10230;</span>__CTA__</span>
    <span class="sitio">infoseguridadit.com</span>
  </div>
</div>

<script>
// Ajuste automatico: el titular achica hasta que la pieza cierra sin desbordar.
(function(){
  var card=document.getElementById('card'),
      tit=document.getElementById('titular'),
      baj=document.getElementById('bajada'),
      media=document.querySelector('.media');
  function desborda(){return card.scrollHeight>card.clientHeight+1;}
  var t=parseFloat(getComputedStyle(tit).fontSize);
  while(desborda()&&t>54){t-=2;tit.style.fontSize=t+'px';}
  var b=parseFloat(getComputedStyle(baj).fontSize);
  while(desborda()&&b>25){b-=1;baj.style.fontSize=b+'px';}
  if(media){
    var m=media.getBoundingClientRect().height;
    while(desborda()&&m>400){m-=12;media.style.height=m+'px';}
    // si sobro aire, la foto crece para cerrar la composicion
    while(!desborda()&&m<780){m+=6;media.style.height=m+'px';}
    if(desborda()){m-=6;media.style.height=m+'px';}
  }
  document.documentElement.dataset.listo='1';
})();
</script>
</body></html>
"""


def armar_html(nota: dict) -> str:
    foto = nota.get("foto")
    ruta = FOTOS / foto if foto else None
    if ruta and ruta.exists():
        media = (
            f'<div class="media"><img src="data:{mime(ruta)};base64,{b64(ruta)}"></div>'
        )
    else:
        agua = nota.get("marca_agua", nota["categoria"])
        media = (
            f'<div class="media sinfoto"><span class="marca-agua">{agua}</span></div>'
        )

    reemplazos = {
        "__VAR__": FUENTES["var"],
        "__BLACK__": FUENTES["black"],
        "__TITULO__": nota["titular"].replace("*", ""),
        "__CATEGORIA__": nota["categoria"].upper(),
        "__ETIQUETA__": nota.get("etiqueta", "Nota nueva").upper(),
        "__MEDIA__": media,
        "__TITULAR__": resaltar(nota["titular"]),
        "__BAJADA__": resaltar(nota["bajada"]),
        "__CTA__": nota.get("cta", "Nota completa en el link de la bio"),
        "__LOGO__": bloque_logo(),
    }
    html = PLANTILLA
    for k, v in reemplazos.items():
        html = html.replace(k, v)
    return html


# ------------------------------------------------------------------- proceso
def main() -> int:
    notas = json.loads((BASE / "notas.json").read_text(encoding="utf-8"))["notas"]
    OUT.mkdir(exist_ok=True)

    piezas = []
    for i, nota in enumerate(notas, 1):
        nombre = f"{i:02d}-{slug(nota['titular'].replace('*', ''))}"
        destino = OUT / f"{nombre}.html"
        destino.write_text(armar_html(nota), encoding="utf-8")
        piezas.append((nombre, destino))
        print(f"HTML  {destino.relative_to(BASE)}")

    if "--solo-html" in sys.argv:
        return 0

    from playwright.sync_api import sync_playwright

    # El contenedor trae Chromium preinstalado; se usa ese binario si esta.
    candidatos = [
        pathlib.Path("/opt/pw-browsers/chromium-1194/chrome-linux/chrome"),
        pathlib.Path("/opt/pw-browsers/chromium/chrome-linux/chrome"),
    ]
    binario = next((str(c) for c in candidatos if c.exists()), None)

    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=binario, args=["--no-sandbox"])
        pag = nav.new_page(
            viewport={"width": W, "height": H}, device_scale_factor=ESCALA
        )
        for nombre, ruta in piezas:
            pag.goto(ruta.as_uri())
            pag.wait_for_function("document.documentElement.dataset.listo==='1'")
            pag.wait_for_timeout(220)
            png = OUT / f"{nombre}.png"
            pag.locator("#card").screenshot(path=str(png))
            print(f"PNG   {png.relative_to(BASE)}  ({W*ESCALA}x{H*ESCALA})")
        nav.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
