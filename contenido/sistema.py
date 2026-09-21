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
/* bloque de color a sangre: un solo titular gigante sobre celeste pleno.
   El texto va en tinta oscura: celeste con texto blanco no se lee. */
.slide.cielo{background:var(--sky);color:#062A4D}
.cielo .eyebrow{color:#063E63}
.cielo .dash{background:#062A4D}
.cielo .mark{box-shadow:inset 0 -.36em 0 rgba(255,255,255,.7)}
.cielo p.sub{color:#0B3A5B}
.cielo .brand span,.cielo .num{color:#0B3A5B}
.cielo .swipe{color:#062A4D}

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

/* dato gigante: el numero ocupa media pantalla y el resto es aire */
.dato{font-family:var(--display);font-weight:800;font-size:320px;line-height:.86;
  letter-spacing:-.05em;color:var(--blue)}
.navy .dato{color:#63C8F2}
.dato-txt{font-family:var(--display);font-weight:800;font-size:64px;line-height:1.08;
  letter-spacing:-.02em;margin-top:40px;max-width:860px}
.dato-pie{font-size:32px;line-height:1.4;color:var(--ink-2);margin-top:26px;max-width:820px}
.navy .dato-pie{color:#B9CFE8}

/* foto del cliente a sangre, con velo para que el titular se lea */
.slide.foto{color:#fff}
/* inset negativo: lo absoluto se posiciona contra la caja de padding del
   slide, y sin esto la foto queda con el margen de seguridad alrededor */
.bgimg{position:absolute;inset:calc(var(--safe) * -1);z-index:0}
.bgimg img{width:100%;height:100%;object-fit:cover;display:block}
.bgimg::after{content:'';position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(0,20,45,.42) 0%,rgba(0,20,45,.80) 58%,rgba(0,20,45,.92) 100%)}
.slide.foto .eyebrow,.slide.foto .foot{position:relative;z-index:1}
/* el :not(.bgimg) es clave: sin el, la foto deja de ser absoluta y empuja al titular */
.slide.foto .body-zone > :not(.bgimg){position:relative;z-index:1}
.slide.foto .eyebrow{color:#8FD8F5}
.slide.foto p.sub{color:#D6E4F5}
.slide.foto .mark{box-shadow:inset 0 -.36em 0 rgba(0,168,232,.55)}
.slide.foto .brand span{color:#C7D8EC}
.slide.foto .num{color:#C7D8EC}
.slide.foto .swipe{color:#8FD8F5}

/* el dato gigante tambien entra al lado de una captura, mas chico */
.split .dato{font-size:210px}
.split .dato-txt{font-size:44px;margin-top:26px}
.split .dato-pie{font-size:27px;margin-top:20px}

/* captura anotada: la pantalla del cliente con notas que senalan partes */
.annot{display:flex;gap:52px;align-items:center}
.annot .shot-lg{flex:none;width:452px;height:904px;border-radius:30px;overflow:hidden;
  transform:rotate(-2.2deg);box-shadow:0 34px 80px -30px rgba(10,27,51,.5);
  border:1px solid rgba(10,27,51,.14)}
.annot .shot-lg img{width:100%;height:100%;object-fit:cover;object-position:top center;display:block}
.navy .annot .shot-lg{border-color:rgba(255,255,255,.16);box-shadow:0 34px 80px -30px rgba(0,0,0,.6)}
.annot .notas{flex:1;min-width:0;display:flex;flex-direction:column;gap:56px}
.annot .nota{display:flex;align-items:flex-start;gap:20px;font-size:31px;line-height:1.26;
  font-weight:700;color:var(--ink)}
.annot .nota i{width:52px;height:4px;border-radius:4px;background:var(--sky);flex:none;margin-top:18px}
.annot .nota .ncol{display:block}
.annot .nota .nt{display:block}
.annot .nota em{display:block;font-style:normal;font-weight:400;font-size:27px;
  color:var(--ink-2);margin-top:8px}
.navy .annot .nota{color:#fff} .navy .annot .nota em{color:#B9CFE8}

/* pie fijo: isotipo, desliza, numero */
.foot{display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:14px}
.brand img{width:46px;height:46px;display:block}
/* sobre navy o sobre una foto, el isotipo azul no se lee: va en blanco */
.navy .brand img,.slide.foto .brand img{filter:brightness(0) invert(1);opacity:.92}
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


def dato(numero, texto, pie=''):
    """El numero gigante y una linea que lo explica. Sin bajada larga."""
    return ('<div class="dato">%s</div><div class="dato-txt">%s</div>%s'
            % (numero, texto, '<p class="dato-pie">%s</p>' % pie if pie else ''))


def anotada(imagen, notas, alt=''):
    """La captura del cliente, grande y apenas rotada, con notas que senalan partes.

    notas: [(titulo, aclaracion)] — dos o tres. Mas de tres no entran.
    """
    # el titulo va en su propio span: el exportador a PPTX necesita medirlos
    # por separado, si no el titulo y la aclaracion caen en el mismo renglon
    lis = ''.join('<div class="nota"><i></i><span class="ncol">'
                  '<span class="nt">%s</span>%s</span></div>'
                  % (t, '<em>%s</em>' % a if a else '') for t, a in notas)
    return ('<div class="annot"><div class="shot-lg"><img src="%s" alt="%s"></div>'
            '<div class="notas">%s</div></div>' % (imagen, alt, lis))


def fondo(imagen, alt=''):
    """Foto del cliente a sangre detras del titular. El slide va con clase 'foto'."""
    return '<div class="bgimg"><img src="%s" alt="%s"></div>' % (imagen, alt)


def eyebrow(texto):
    """Sin texto queda solo el guion celeste, que es como se ve mejor en el feed."""
    span = '<span>%s</span>' % texto if texto else ''
    return '<div class="eyebrow"><i class="dash"></i>%s</div>' % span


def page(titulo, slides, pie='min'):
    """slides: [(clase_de_fondo, eyebrow, cuerpo_html)]

    pie='min' deja el isotipo y el DESLIZA; 'completo' suma el dominio y la
    numeracion, que es como estaban los tres primeros carruseles.
    """
    logo = img('logo-256.png', 'image/png')
    total = len(slides)
    out = []
    for i, (bg, eye, body) in enumerate(slides, 1):
        swipe = '<div class="swipe">Deslizá %s</div>' % ARROW if i < total else ''
        dominio = '<span>tunegocioenlasredes.com.ar</span>' if pie == 'completo' else ''
        num = '<div class="num">%02d / %02d</div>' % (i, total) if pie == 'completo' else ''
        out.append(
            '<section class="slide %s">\n'
            '  %s\n'
            '  <div class="body-zone">%s</div>\n'
            '  <div class="foot">\n'
            '    <div class="brand"><img src="%s" alt="">%s</div>\n'
            '    %s%s\n'
            '  </div>\n'
            '</section>' % (bg, eyebrow(eye), body, logo, dominio, swipe, num))
    return ('<!doctype html><html lang="es-AR"><meta charset="utf-8">'
            '<title>%s</title><style>%s%s</style>%s</html>'
            % (titulo, fonts_css(), CSS, "\n".join(out)))
