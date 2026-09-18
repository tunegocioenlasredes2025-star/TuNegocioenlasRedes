#!/usr/bin/env python3
"""Sistema visual de TNR para Instagram, en un solo lugar.

Traslado de los tokens de styles.css (rediseno v3) al lienzo de 1080x1350.
Cada carrusel vive en carruseles/<nombre>/make.py y solo escribe el copy: el
molde, los colores y las tipografias salen de aca.
"""
from build import fonts_css, img

# La flecha va en SVG y no como caracter: U+2192 no entra en el subset latin de
# Figtree, caeria en la fuente del sistema y esa no se embebe en el PDF.
ARROW = ('<svg class="arw" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'
         '<path d="M4 12h14M12 5l7 7-7 7"/></svg>')

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --paper:#FFFFFF; --mist:#F2F6FC; --mist-2:#E7EEF9; --line:#DFE7F2;
  --ink:#0A1B33; --ink-2:#46526B; --muted:#6B7690;
  --navy:#003878; --blue:#1657D0; --sky:#00A8E8; --hl:#A8E1F8;
  --display:'Bricolage Grotesque',sans-serif; --font:'Figtree',sans-serif;
  --safe:88px;
}
body{background:#DDE5F0;display:flex;flex-direction:column;align-items:center;gap:28px;
  padding:28px;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--paper);
  color:var(--ink);font-family:var(--font);display:flex;flex-direction:column;padding:var(--safe)}
.slide.mist{background:var(--mist)}
.slide.navy{background:var(--navy);color:#fff}

/* etiqueta superior: el eyebrow de la web, con el guion celeste */
.eyebrow{display:flex;align-items:center;gap:16px;font-size:22px;font-weight:700;
  letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.dash{width:40px;height:5px;border-radius:5px;background:var(--sky);flex:none}
.navy .eyebrow{color:#8FD8F5}

.body-zone{flex:1;display:flex;flex-direction:column;justify-content:center;
  text-align:left;padding:48px 0;min-height:0}
h1{font-family:var(--display);font-weight:800;letter-spacing:-.03em;line-height:1.02;
  text-align:left;color:inherit}
.xl{font-size:112px} .lg{font-size:92px} .md{font-size:74px} .sm{font-size:60px}
p.sub{font-size:36px;line-height:1.42;color:var(--ink-2);margin-top:36px;max-width:850px;text-align:left}
.navy p.sub{color:#B9CFE8}

/* marcador celeste detras de la palabra clave: la firma de la marca */
.mark{box-shadow:inset 0 -.36em 0 var(--hl);padding:0 .06em;
  -webkit-box-decoration-break:clone;box-decoration-break:clone}
.navy .mark{box-shadow:inset 0 -.36em 0 rgba(0,168,232,.45)}
.blue{color:var(--blue)} .navy .blue{color:#63C8F2}

/* dos columnas: texto + captura real del cliente */
.split{display:flex;gap:60px;align-items:center}
.split-text{flex:1;min-width:0}
.split p.sub{font-size:31px;margin-top:28px}
.shot{flex:none;width:360px;height:720px;border-radius:28px;overflow:hidden;
  box-shadow:0 34px 80px -30px rgba(0,0,0,.6);border:1px solid rgba(255,255,255,.16)}
.shot img{width:100%;height:100%;object-fit:cover;object-position:top center;display:block}
/* el borde y la sombra del marco se invierten segun el fondo del slide */
.slide:not(.navy) .shot{border-color:rgba(10,27,51,.14);
  box-shadow:0 30px 70px -28px rgba(10,27,51,.45)}

/* lista numerada: los pasos de un proceso */
ol.pasos{margin-top:52px;display:flex;flex-direction:column;gap:30px}
ol.pasos .pcol{display:block}
ol.pasos li{display:flex;align-items:baseline;gap:26px;font-size:38px;line-height:1.24;
  font-weight:700;color:var(--ink)}
.navy ol.pasos li{color:#fff}
ol.pasos b{font-family:var(--display);font-size:46px;font-weight:800;color:var(--blue);
  flex:none;width:72px;letter-spacing:-.02em}
.navy ol.pasos b{color:#63C8F2}
ol.pasos .pt{font-style:normal}
ol.pasos .pa{font-weight:400;color:var(--ink-2);display:block;font-size:30px;margin-top:6px}
.navy ol.pasos .pa{color:#B9CFE8}

/* comparacion antes / despues */
.vs{margin-top:54px;display:flex;flex-direction:column;gap:22px}
.vs div{border-radius:20px;padding:32px 36px;font-size:34px;line-height:1.3}
.vs .antes{background:var(--mist-2);color:var(--ink-2)}
.vs .ahora{background:var(--blue);color:#fff;font-weight:700}
.navy .vs .antes{background:rgba(255,255,255,.1);color:#B9CFE8}
.navy .vs .ahora{background:var(--sky);color:#062A4D}
.vs em{display:block;font-style:normal;font-size:21px;font-weight:700;letter-spacing:.16em;
  text-transform:uppercase;opacity:.75;margin-bottom:10px}

/* pie fijo: isotipo, desliza, numero */
.foot{display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:14px}
.brand img{width:46px;height:46px;display:block}
.brand span,.num{font-size:21px;font-weight:700;color:var(--muted)}
.num{letter-spacing:.18em}
.navy .brand span,.navy .num{color:#8FA9C8}
.swipe{display:inline-flex;flex:none;align-items:center;gap:14px;font-size:24px;font-weight:700;
  letter-spacing:.14em;text-transform:uppercase;color:var(--blue)}
.navy .swipe{color:#8FD8F5}
.arw{width:.9em;height:.9em;flex:none}

.cta{display:inline-flex;align-self:flex-start;align-items:center;gap:16px;background:var(--blue);
  color:#fff;font-size:30px;font-weight:700;padding:28px 44px;border-radius:999px;margin-top:44px;
  box-shadow:0 18px 40px -16px rgba(22,87,208,.6)}

/* Impresion a PDF. Va al final a proposito: arriba esta body{padding:28px}, que
   separa los slides en el navegador, y si estas reglas fueran antes perderian
   por orden de cascada y cada slide se pasaria de pagina. build.py imprime un
   slide por vez, asi que aca no hace falta ningun salto de pagina. */
@page{size:11.25in 14.0625in;margin:0}
@media print{
  html,body{display:block;margin:0;padding:0;gap:0;width:1080px}
  .slide{break-inside:avoid}
}
"""


def h(texto, size='lg'):
    return '<h1 class="%s">%s</h1>' % (size, texto)


def sub(texto):
    return '<p class="sub">%s</p>' % texto


def split(texto_html, imagen, alt=''):
    return ('<div class="split"><div class="split-text">%s</div>'
            '<div class="shot"><img src="%s" alt="%s"></div></div>' % (texto_html, imagen, alt))


def pasos(items):
    """items: [(numero, titulo, aclaracion)]"""
    lis = ''.join('<li><b>%s</b><div class="pcol"><i class="pt">%s</i>'
                  '<span class="pa">%s</span></div></li>' % i for i in items)
    return '<ol class="pasos">%s</ol>' % lis


def vs(antes, ahora):
    return ('<div class="vs"><div class="antes"><em>Antes</em><span>%s</span></div>'
            '<div class="ahora"><em>Ahora</em><span>%s</span></div></div>' % (antes, ahora))


def cta(texto):
    return '<div class="cta"><span>%s</span>%s</div>' % (texto, ARROW)


def eyebrow(texto):
    return '<div class="eyebrow"><i class="dash"></i><span>%s</span></div>' % texto


def page(titulo, slides):
    """slides: [(clase_de_fondo, eyebrow, cuerpo_html)]"""
    logo = img('logo-256.png', 'image/png')
    total = len(slides)
    out = []
    for i, (bg, eye, body) in enumerate(slides, 1):
        swipe = '<div class="swipe">Deslizá %s</div>' % ARROW if i < total else ''
        out.append(
            '<section class="slide %s">\n'
            '  %s\n'
            '  <div class="body-zone">%s</div>\n'
            '  <div class="foot">\n'
            '    <div class="brand"><img src="%s" alt=""><span>tunegocioenlasredes.com.ar</span></div>\n'
            '    %s<div class="num">%02d / %02d</div>\n'
            '  </div>\n'
            '</section>' % (bg, eyebrow(eye), body, logo, swipe, i, total))
    return ('<!doctype html><html lang="es-AR"><meta charset="utf-8">'
            '<title>%s</title><style>%s%s</style>%s</html>'
            % (titulo, fonts_css(), CSS, "\n".join(out)))
