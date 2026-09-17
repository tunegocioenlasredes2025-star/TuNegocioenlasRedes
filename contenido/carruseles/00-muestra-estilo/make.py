#!/usr/bin/env python3
"""Muestra de estilo: 4 slides para validar el traslado de la web v3 a Instagram."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import fonts_css, img, render

D = pathlib.Path(__file__).resolve().parent
LOGO = img('logo-256.png', 'image/png')
TONCARS = img('trabajos/toncars-automotores-web-celular.webp', 'image/webp')

ARROW = '<svg class="arw" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h14M12 5l7 7-7 7"/></svg>'

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --paper:#FFFFFF; --mist:#F2F6FC; --mist-2:#E7EEF9; --line:#DFE7F2;
  --ink:#0A1B33; --ink-2:#46526B; --muted:#6B7690;
  --navy:#003878; --blue:#1657D0; --sky:#00A8E8; --hl:#A8E1F8;
  --display:'Bricolage Grotesque',sans-serif; --font:'Figtree',sans-serif;
  --safe:88px;
}
body{background:#DDE5F0;display:flex;flex-direction:column;align-items:center;gap:28px;padding:28px;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--paper);
  color:var(--ink);font-family:var(--font);display:flex;flex-direction:column;
  padding:var(--safe);page-break-after:always}
.slide.mist{background:var(--mist)}
.slide.navy{background:var(--navy);color:#fff}

/* etiqueta superior: el eyebrow de la web, con el guion celeste */
.eyebrow{display:flex;align-items:center;gap:16px;font-size:22px;font-weight:700;
  letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.eyebrow::before{content:"";width:40px;height:5px;border-radius:5px;background:var(--sky);flex:none}
.navy .eyebrow{color:#8FD8F5}
.navy .eyebrow::before{background:var(--sky)}

.body-zone{flex:1;display:flex;flex-direction:column;justify-content:center;
  text-align:left;padding:48px 0}
h1{font-family:var(--display);font-weight:800;letter-spacing:-.03em;line-height:1.02;
  text-align:left;color:inherit}
.xl{font-size:112px}
.lg{font-size:92px}
.md{font-size:74px}
p.sub{font-size:36px;line-height:1.42;color:var(--ink-2);margin-top:36px;max-width:820px;text-align:left}
.navy p.sub{color:#B9CFE8}

/* marcador celeste detras de la palabra clave: la firma de la marca */
.mark{background:linear-gradient(transparent 56%,var(--hl) 56%,var(--hl) 94%,transparent 94%);
  padding:0 .06em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.navy .mark{background:linear-gradient(transparent 56%,rgba(0,168,232,.42) 56%,rgba(0,168,232,.42) 94%,transparent 94%)}
.blue{color:var(--blue)}
.navy .blue{color:#63C8F2}

/* pie: logo a la izquierda, numero de slide a la derecha */
.foot{display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:14px}
.brand img{width:46px;height:46px;display:block}
.brand span{font-size:21px;font-weight:700;color:var(--muted);letter-spacing:.01em}
.navy .brand span{color:#8FA9C8}
.num{font-size:21px;font-weight:700;color:var(--muted);letter-spacing:.18em}
.navy .num{color:#8FA9C8}

.swipe{display:inline-flex;flex:none;align-items:center;gap:14px;font-size:24px;font-weight:700;
  letter-spacing:.14em;text-transform:uppercase;color:var(--blue)}

/* tarjeta con la captura real del cliente */
.split{display:flex;gap:60px;align-items:center}
.split-text{flex:1;min-width:0}
.shot{flex:none;width:360px;height:720px;border-radius:28px;overflow:hidden;
  box-shadow:0 34px 80px -30px rgba(0,0,0,.6);border:1px solid rgba(255,255,255,.16)}
.shot img{width:100%;display:block}
.sm{font-size:60px}
.split p.sub{font-size:31px;margin-top:28px}

.arw{width:.9em;height:.9em;flex:none}
.cta{display:inline-flex;align-self:flex-start;align-items:center;gap:16px;background:var(--blue);color:#fff;
  font-size:30px;font-weight:700;padding:28px 44px;border-radius:999px;margin-top:44px;
  box-shadow:0 18px 40px -16px rgba(22,87,208,.6)}

/* Impresion a PDF. Va al final a proposito: el bloque de arriba define
   body{padding:28px} para ver los slides separados en el navegador, y si estas
   reglas fueran antes perderian por orden de cascada. build.py imprime un slide
   por vez, asi que aca no hace falta ningun salto de pagina. */
@page{size:11.25in 14.0625in;margin:0}
@media print{
  html,body{display:block;margin:0;padding:0;gap:0;width:1080px}
  /* Chromium redondea la pagina a 1350,7px. Estirar el slide a ese alto lo
     empuja a una segunda pagina, asi que se deja en 1350 y el fondo del body
     tapa el medio pixel que sobra al pie. */
  .slide{break-inside:avoid}
}
"""

SLIDES = [
  # (clase, eyebrow, html del cuerpo)
  ('', 'Caso real · TonCars · Ing. Maschwitz',
   '<h1 class="xl">El problema<br>no era la web.<br>Era el <span class="mark">primer<br>mensaje</span>.</h1>'
   '<p class="sub">Cómo hicimos que cada consulta llegue con el auto ya elegido.</p>'),

  ('mist', 'El problema',
   '<h1 class="lg">Un usado se vende<br>con la foto y el precio<br><span class="mark">a la vista</span>.</h1>'
   '<p class="sub">Si cada unidad vive en una publicación suelta, la persona compara en otra pestaña. Y no vuelve.</p>'),

  ('navy', 'Qué construimos',
   '<div class="split"><div class="split-text">'
   '<h1 class="sm">Una ficha<br>por auto.<br>Con su propio<br><span class="blue">botón de<br>consulta</span>.</h1>'
   '<p class="sub">Financiación, permuta, consignación y el paso a paso de la compra: escritos una vez, para siempre.</p>'
   '</div><div class="shot"><img src="%s" alt="Web de TonCars en el celular"></div></div>' % TONCARS),

  ('', 'Qué tiene hoy',
   '<h1 class="lg">Cada consulta entra<br>con el <span class="mark">vehículo<br>ya elegido</span>.</h1>'
   '<p class="sub">Diez accesos a WhatsApp en la misma página. Nadie más escribe «hola, ¿cuánto sale?».</p>'
   '<div class="cta">Te hacemos la demo gratis en 72 hs ' + ARROW + '</div>'),
]

def html():
    out = []
    for i, (cls, eye, body) in enumerate(SLIDES, 1):
        swipe = '<div class="swipe">Deslizá ' + ARROW + '</div>' if i < len(SLIDES) else ''
        out.append("""<section class="slide %s">
  <div class="eyebrow">%s</div>
  <div class="body-zone">%s</div>
  <div class="foot">
    <div class="brand"><img src="%s" alt=""><span>tunegocioenlasredes.com.ar</span></div>
    %s<div class="num">%02d / %02d</div>
  </div>
</section>""" % (cls, eye, body, LOGO, swipe, i, len(SLIDES)))
    return ("<!doctype html><html lang=\"es-AR\"><meta charset=\"utf-8\">"
            "<title>TNR — muestra de estilo IG</title><style>%s%s</style>%s</html>"
            % (fonts_css(), CSS, "\n".join(out)))

(D / 'index.html').write_text(html(), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
