# -*- coding: utf-8 -*-
"""Genera los HTML standalone de las piezas de Secure Growing a partir de tokens.css + base.css."""
import os, re, random, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENS = open(os.path.join(ROOT, 'tokens.css'), encoding='utf-8').read()
BASE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'base.css'), encoding='utf-8').read()

FONTS = """
@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:700;src:url('../fonts/BricolageGrotesque-Bold.ttf') format('truetype')}
@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:800;src:url('../fonts/BricolageGrotesque-ExtraBold.ttf') format('truetype')}
@font-face{font-family:'Instrument Sans';font-style:normal;font-weight:400;src:url('../fonts/InstrumentSans-Regular.ttf') format('truetype')}
@font-face{font-family:'Instrument Sans';font-style:normal;font-weight:500;src:url('../fonts/InstrumentSans-Medium.ttf') format('truetype')}
@font-face{font-family:'Instrument Sans';font-style:normal;font-weight:600;src:url('../fonts/InstrumentSans-SemiBold.ttf') format('truetype')}
"""

# isotipo (paths de assets/logo.svg de la landing, recortado al dibujo)
P1 = "M424.873 378.207C452.029 374.09 476.399 384.137 499.43 396.781C483.943 410.475 469.623 426.409 459.306 444.38C446.752 439.986 433.973 436.867 420.877 440.779C409.99 444.03 403.266 454.774 407.026 465.797C408.359 469.626 410.947 472.892 414.371 475.063C423.306 480.804 447.562 484.091 458.636 487.325C467.866 490.066 476.665 494.093 484.772 499.288C495.591 506.194 507.83 517.828 514.948 528.307C528.398 548.11 538.269 567.64 561.52 578.397C586.306 589.863 608.778 586.967 633.549 578.139C633.809 572.486 634.187 564.232 633.499 558.754C654.216 543.446 675.586 529.403 696.479 514.13L696.575 558.125L696.585 603.303C667.496 628.755 647.822 640.498 607.433 645.557C560.52 651.433 512.694 628.116 484.185 591.308C472.529 576.26 469.377 562.354 451.695 551.187C442.805 545.198 432.86 542.971 422.606 540.204C384.561 529.937 348.058 510.598 343.473 467.038C337.976 414.818 375.324 382.66 424.873 378.207Z"
P2 = "M587.349 378.215C622.365 374.213 663.731 391.933 688.248 416.619C672.371 429.276 658.531 441.983 643.284 455.195C613.323 431.509 567.002 433.863 538.944 459.649C524.946 473.814 519.586 484.041 515.812 503.435C499.521 488.177 486.573 477.861 464.8 470.348C481.273 422.335 529.226 383.588 579.734 378.791C582.256 378.551 584.821 378.377 587.349 378.215Z"
P3 = "M379.748 563.953C381.394 564.427 386.995 570.823 389.085 572.281C408.652 585.93 436.016 592.88 458.389 582.723C468.407 600.222 480.784 614.143 496.252 626.888C482.832 636.104 463.679 643.101 447.62 645.358C403.268 651.786 354.661 632.533 326.997 597.146C344.656 586.202 362.24 575.137 379.748 563.953Z"
P4 = "M634.62 484.986C654.327 487.337 667.755 492.004 682.724 504.872C671.297 512.104 660.043 519.194 648.882 526.859C641.519 531.915 630.86 537.811 624.402 543.546L621.294 541.865C610.158 535.545 594.249 528.16 580.967 530.603C578.758 531.009 575.449 532.851 573.371 533.934C575.771 530.511 579.126 526.074 582.316 523.385C598.109 510.071 617.057 495.786 634.62 484.986Z"

def iso(oscuro=True):
    c = 'var(--sg-hueso)' if oscuro else 'var(--sg-verde)'
    return (f'<svg viewBox="320 368 384 288" aria-hidden="true">'
            f'<path fill="{c}" d="{P1}"/><path fill="{c}" d="{P2}"/><path fill="{c}" d="{P3}"/>'
            f'<path fill="var(--sg-cobre)" d="{P4}"/></svg>')

def firma(oscuro=True):
    return f'<p class="firma">{iso(oscuro)}<span>@securegrowing</span></p>'

def slide(inner, fondo='verde', pag=None, total=None, ultimo=False):
    cls = 'slide' + ('' if fondo == 'verde' else ' ' + fondo)
    osc = fondo != 'hueso'
    p = ''
    if pag is not None and total:
        p = f'<p class="pag">{pag:02d} / {total:02d}</p>'
    elif pag == 'deslizá':
        p = '<p class="pag">DESLIZÁ</p>'
        inner = (f'<svg class="marca" viewBox="320 368 384 288" aria-hidden="true"><path d="{P1}"/><path d="{P2}"/><path d="{P3}"/><path d="{P4}"/></svg>' + inner)
    return f'<section class="{cls}">\n{inner}\n{firma(osc)}\n{p}\n</section>'

def doc(titulo, slides):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1080">
<title>{html.escape(titulo)}</title>
<style>
{TOKENS}
{FONTS}
{BASE}
</style>
</head>
<body>
{chr(10).join(slides)}
</body>
</html>
"""

def eyebrow(t): return f'<p class="eyebrow">{t}</p>'
def titulo(t, h1=False, cierre=False): return f'<h1 class="titulo{" h1" if h1 else ""}">{t}</h1>' if h1 else f'<h2 class="titulo{" cierre" if cierre else ""}">{t}</h2>'
def bajada(t, abajo=False): return f'<p class="bajada{" abajo" if abajo else ""}">{t}</p>'
def nota(t): return f'<p class="nota">{t}</p>'
def fuente(t): return f'<p class="fuente">{t}</p>'

# ------------------------------------------------------------------ elementos
def barras(vals, maxv, labels, off_from=None, ghost=None, dim_from=None, abajo=False):
    rows = []
    for i, (v, l) in enumerate(zip(vals, labels)):
        if off_from is not None and i >= off_from:
            rows.append(f'<div class="fila"><p class="bl">{l}</p><div class="b off" style="width:100%"></div><p class="bv dim">—</p></div>')
            continue
        w = max(v / maxv * 100, 3)
        if ghost:
            g = max(ghost[i] / maxv * 100, 2)
            rows.append(f'<div class="fila doble"><p class="bl">{l}</p><div class="b" style="width:{w:.1f}%"></div>'
                        f'<p class="bv">{v}</p><div class="b ghost" style="width:{g:.1f}%"></div></div>')
        else:
            dim = ' dim' if (dim_from is not None and i < dim_from) else ''
            rows.append(f'<div class="fila"><p class="bl">{l}</p><div class="b" style="width:{w:.1f}%"></div><p class="bv{dim}">{v}</p></div>')
    return f'<div class="dato barras{" abajo" if abajo else ""}">{"".join(rows)}</div>'

def timeline(pasos, on, now=None):
    out = []
    for i, (b, s) in enumerate(pasos):
        c = 'paso'
        if now is not None and i == now: c += ' now'
        elif i < on: c += ' on'
        out.append(f'<div class="{c}"><i></i><b>{b}</b><small>{s}</small></div>')
    return f'<div class="dato tl">{"".join(out)}</div>'

def grilla(n, on, chica=False):
    return f'<div class="dato grilla{" chica" if chica else ""}">' + ''.join(f'<i class="{"on" if i < on else ""}"></i>' for i in range(n)) + '</div>'

def tabla(filas, hasta, cols=('Vos', 'B', 'C'), estado=None):
    """filas: [(label, (a,b,c))]; hasta: filas visibles; estado 'q' en la columna Vos."""
    out = ['<div class="tabla">', f'<p class="th">Criterio</p>'] + [f'<p class="th">{c}</p>' for c in cols]
    for i, (l, vals) in enumerate(filas):
        vis = i < hasta
        now = (i == hasta - 1)
        out.append(f'<p class="rl{"" if vis else " dim"}">{l}</p>')
        for j, v in enumerate(vals):
            if not vis:
                out.append('<p class="c"><i class="no"></i></p>')
            else:
                k = 'q' if v == '?' else ('' if v else 'no')
                out.append(f'<p class="c{" now" if now and estado == "fila" else ""}"><i class="{k}"></i></p>')
    out.append('</div>')
    return '<div class="dato">' + ''.join(out) + '</div>'

def dos(izq, der, chico=False, med=False):
    k1, v1, d1 = izq; k2, v2, d2 = der
    ch = ' chico' if chico else (' med' if med else '')
    return (f'<div class="dato dos"><div><p class="k">{k1}</p><p class="v{ch}">{v1}</p><p class="d">{d1}</p></div>'
            f'<div class="sep"></div><div><p class="k acc">{k2}</p><p class="v acc{ch}">{v2}</p><p class="d acc">{d2}</p></div></div>')

def segmentos(n=14, on=14, fin=True):
    segs = ''.join(f'<i class="{"fin" if (fin and i == n - 1) else ("" if i < on else "off")}"></i>' for i in range(n))
    lbls = ''.join(f'<b>{i + 1}</b>' for i in range(n))
    return f'<div class="dato segs">{segs}</div><div class="segs-lbl">{lbls}</div>'

def escalera(items):
    out = ''.join(f'<div class="esc"><b>{v}</b><i style="height:{h}px"></i><small>{l}</small></div>' for v, h, l in items)
    return f'<div class="dato escalera">{out}</div>'

def comparativa(items):
    out = ''
    for l, v, vacia in items:
        if vacia:
            out += f'<div class="cb"><p class="cl">{l}</p><div class="bar vacia">{v}</div></div>'
        else:
            out += f'<div class="cb"><p class="cl">{l}</p><div class="bar" style="width:{v[1]}%">{v[0]}</div></div>'
    return f'<div class="dato comp">{out}</div>'

def pilas(items):
    out = ''.join(f'<div class="it"><p class="pill">{t}</p><p>{d}</p></div>' for t, d in items)
    return f'<div class="dato pilas">{out}</div>'

def red(seed=7, n=44, w=920, h=520):
    rnd = random.Random(seed)
    pts = []
    while len(pts) < n:
        x, y = rnd.uniform(30, w - 30), rnd.uniform(30, h - 30)
        if all((x - a) ** 2 + (y - b) ** 2 > 70 ** 2 for a, b in pts):
            pts.append((x, y))
    lines = set()
    for i, (x, y) in enumerate(pts):
        d = sorted(((x - a) ** 2 + (y - b) ** 2, j) for j, (a, b) in enumerate(pts) if j != i)[:3]
        for _, j in d:
            lines.add(tuple(sorted((i, j))))
    ls = ''.join(f'<line x1="{pts[i][0]:.0f}" y1="{pts[i][1]:.0f}" x2="{pts[j][0]:.0f}" y2="{pts[j][1]:.0f}" stroke="var(--sg-hueso-2)" stroke-width="2"/>' for i, j in lines)
    big = set(rnd.sample(range(n), 9))
    cs = ''.join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{16 if i in big else 9}" fill="{"var(--sg-cobre)" if i in big else "var(--sg-verde)"}"/>' for i, (x, y) in enumerate(pts))
    return f'<svg class="dato red" viewBox="0 0 {w} {h}" aria-hidden="true">{ls}{cs}</svg>'

def filas_num(items):
    out = ''.join(f'<div class="f"><p class="n">{n}</p><p class="t">{t}</p><p class="s">{s}</p></div>' for n, t, s in items)
    return f'<div class="dato filas">{out}</div>'

def numero(v, lbl=None, xl=False, solido=False):
    c = 'num' + (' xl' if xl else '') + (' solido' if solido else '')
    s = f'<p class="{c}">{v}</p>'
    if lbl: s += f'<p class="num-lbl">{lbl}</p>'
    return f'<div class="dato">{s}</div>'

# ================================================================== PIEZAS
PIEZAS = {}

# ---------- C01 vendedor sentado: cascada de barras
L = ['Contactos', 'Llamados', 'Reuniones', 'Cerrados']
T = 8
PIEZAS['carruseles/carrusel-01-vendedor-sentado'] = ('Tu vendedor cierra bien', [
    slide(eyebrow('Seguridad electrónica · Canal comercial') + titulo('Tu vendedor cierra bien. <span class="ac">El problema es lo poco que le llega.</span>', h1=True)
          + bajada('La cadena de venta completa, etapa por etapa, con los números que nadie te muestra a fin de mes.', abajo=True), 'verde', 'deslizá'),
    slide(eyebrow('La cadena') + titulo('Cuatro etapas. La mayoría mide una.')
          + bajada('Contactos que llegan, llamados, reuniones, cerrados. Si solo contás los cerrados, no sabés en cuál se pierde la venta.')
          + barras([0, 0, 0, 0], 100, L, off_from=0), 'hueso', 2, T),
    slide(eyebrow('Etapa 01 · Contactos') + titulo('Llegaron 100.')
          + bajada('Supongamos 100 en el mes, entre Google, redes, prospección y prensa del sector. Es el número que casi nadie anota.')
          + barras([100, 0, 0, 0], 100, L, off_from=1) + fuente('Ejemplo con proporciones ilustrativas.'), 'verde', 3, T),
    slide(eyebrow('Etapa 02 · Llamados') + titulo('El vendedor llamó a 60.')
          + bajada('Los otros 40 quedaron en la planilla. Nadie los tocó y nadie se enteró.')
          + barras([100, 60, 0, 0], 100, L, off_from=2, dim_from=1), 'verde', 4, T),
    slide(eyebrow('Etapa 03 · Reuniones') + titulo('Se sentaron 12.')
          + bajada('Uno de cada cinco llamados aceptó una reunión. Acá se ve si el contacto era bueno o era volumen.')
          + barras([100, 60, 12, 0], 100, L, off_from=3, dim_from=2), 'negro', 5, T),
    slide(eyebrow('Etapa 04 · Cerrados') + titulo('Cerró 3.')
          + bajada('Una de cada cuatro reuniones terminó en venta. El vendedor cierra bien. Le llegaron pocas.')
          + barras([100, 60, 12, 3], 100, L, dim_from=3), 'negro', 6, T),
    slide(eyebrow('La misma cadena, el doble de entrada') + titulo('Con 200 contactos, el mismo vendedor cierra 6.')
          + bajada('No hace falta que venda mejor. Hace falta que le llegue el doble, y que alguien mire dónde se caen los 40 que no llamó.')
          + barras([200, 120, 24, 6], 200, L, ghost=[100, 60, 12, 3]), 'hueso', 7, T),
    slide(eyebrow('Para hacer hoy') + titulo('Contá cuántos contactos le llegaron a tu vendedor este mes.', cierre=True)
          + bajada('Si no tenés el número, ese es el diagnóstico. Escribinos y lo armamos juntos en una reunión de veinte minutos.')
          + '<p class="btn">Reunión de 20 minutos</p>', 'verde', 8, T),
])

# ---------- C02 te googlean antes: timeline horizontal
PASOS = [('Le pasan tu nombre', 'Un colega, un proveedor'), ('Te googlea', 'Día 1'), ('Abre tu Instagram', 'Día 2'),
         ('Te compara con dos', 'Día 3'), ('Llama a uno', 'Día 5')]
T = 8
PIEZAS['carruseles/carrusel-02-te-googlean-antes'] = ('Te googlean antes de llamarte', [
    slide(eyebrow('Seguridad electrónica · Canal comercial') + titulo('Te googlean antes de llamarte. <span class="ac">Aunque vengan referidos.</span>', h1=True)
          + bajada('Lo que hace el que te compra en los días previos a levantar el teléfono. Cinco pasos que pasan sin que te enteres.', abajo=True), 'verde', 'deslizá'),
    slide(eyebrow('Paso 01') + titulo('El referido no llama primero. Busca primero.')
          + bajada('Un colega le pasó tu nombre. Lo primero que hace no es llamarte: es escribirlo en Google.')
          + timeline(PASOS, 0, now=0), 'hueso', 2, T),
    slide(eyebrow('Paso 02 · Día 1') + titulo('Te googlea.')
          + bajada('Mira el primer resultado. Si no sos vos, o si es una web de 2014, ya está comparando con otro.')
          + timeline(PASOS, 1, now=1), 'verde', 3, T),
    slide(eyebrow('Paso 03 · Día 2') + titulo('Abre tu Instagram.')
          + bajada('Mira la fecha de la última publicación. Si es de hace meses, lee que la empresa está parada. No importa que no sea cierto.')
          + timeline(PASOS, 2, now=2), 'verde', 4, T),
    slide(eyebrow('Paso 04 · Día 3') + titulo('Te compara con dos más.')
          + bajada('Tres pestañas abiertas. Web, redes, y a quién le contestaron primero el mensaje.')
          + timeline(PASOS, 3, now=3), 'negro', 5, T),
    slide(eyebrow('Paso 05 · Día 5') + titulo('Llama a uno.')
          + bajada('Al que le pareció más serio. Si no fuiste vos, nunca vas a saber que existió ese pedido.')
          + timeline(PASOS, 4, now=4), 'negro', 6, T),
    slide(eyebrow('El recorrido completo') + titulo('Cinco pasos. Ninguno te avisa.')
          + bajada('El teléfono suena recién en el quinto. Todo lo que define la venta pasa antes, en tu web y en tus redes.')
          + timeline(PASOS, 5), 'hueso', 7, T),
    slide(eyebrow('Para hacer hoy') + titulo('Googleá tu empresa en una ventana de incógnito.', cierre=True)
          + bajada('Mirá el primer resultado como si fueras el referido. Si no te convence a vos, mandanos la captura y te decimos qué cambiar primero.')
          + '<p class="btn">Reunión de 20 minutos</p>', 'verde', 8, T),
])

# ---------- C03 cuánto vale un abonado: número gigante + grilla 36
T = 8
PIEZAS['carruseles/carrusel-03-cuanto-vale-un-abonado'] = ('USD 252, eso vale un abonado', [
    slide(eyebrow('Seguridad electrónica · La cuenta') + titulo('USD 252. <span class="ac">Eso vale un abonado.</span>', h1=True)
          + bajada('La cuenta que cambia cómo mirás lo que invertís en vender. Con un abono de monitoreo de ejemplo; cambialo por el tuyo.', abajo=True), 'verde', 'deslizá'),
    slide(eyebrow('El abono') + titulo('Un abono de monitoreo: USD 7 por mes.')
          + bajada('Precio de un caso real del rubro. Parece poco. Por eso nadie hace la cuenta.')
          + numero('7', 'dólares por mes') + grilla(36, 1, chica=True)
          + fuente('Abono mensual de un cliente de Secure Growing, 2026.'), 'hueso', 2, T),
    slide(eyebrow('El tiempo') + titulo('Un abonado se queda 36 meses.')
          + bajada('Tres años en promedio. Algunos más, algunos menos. Cada punto es un mes que paga.')
          + numero('36', 'meses') + grilla(36, 36, chica=True), 'verde', 3, T),
    slide(eyebrow('La cuenta') + titulo('7 por 36 son 252.')
          + bajada('Cada abonado nuevo son USD 252 que entran en cuotas. Sin volver a venderle, sin volver a visitarlo.')
          + numero('252', 'dólares por abonado', xl=True), 'verde', 4, T),
    slide(eyebrow('El plan') + titulo('Cuatro abonados nuevos por mes pagan el plan.')
          + bajada('Plan base de Secure Growing: USD 900. Cuatro por 252 son 1.008. Un abonado nuevo por semana y el canal se paga solo.')
          + numero('4', 'abonados nuevos por mes') + fuente('Media kit de Secure Growing, plan Presencia.'), 'negro', 5, T),
    slide(eyebrow('Si vendés a instaladores') + titulo('Un instalador nuevo cada cuatro meses.')
          + bajada('Si sos central mayorista, tu cliente es el instalador y trae decenas de abonados. Con uno nuevo cada cuatro meses, el año está pagado.')
          + grilla(12, 12) + fuente('Cada punto es un mes. Tres instaladores nuevos en el año.'), 'negro', 6, T),
    slide(eyebrow('Lo que no se ve') + titulo('Un mes sin abonados nuevos vale cero. Durante tres años.')
          + bajada('Lo caro no es el plan. Es el mes que pasa sin que entre nadie: son 36 meses de cuota que no existen.')
          + numero('0', 'dólares en 36 meses', xl=True) + grilla(36, 0, chica=True), 'hueso', 7, T),
    slide(eyebrow('Para hacer hoy') + titulo('Hacé la cuenta con tu abono.', cierre=True)
          + bajada('Precio por mes, por meses promedio. Mandanos el resultado y te decimos cuántos abonados nuevos por mes necesitás para que el canal se pague solo.')
          + '<p class="btn">Reunión de 20 minutos</p>', 'verde', 8, T),
])

# ---------- C04 tres proveedores: tabla ranking
FIL = [('Web', (True, True, False)), ('Redes', (False, True, False)), ('Respuesta', (True, False, True)), ('Números', (False, True, False))]
COLS = ('A', 'B', 'C')
T = 8
PIEZAS['carruseles/carrusel-04-tres-proveedores'] = ('Te comparan contra dos más', [
    slide(eyebrow('Seguridad electrónica · Posicionamiento') + titulo('Te comparan contra dos más. <span class="ac">¿Cuál parece más serio?</span>', h1=True)
          + bajada('Lo que mira el que firma la compra cuando tiene tres presupuestos sobre la mesa. Cuatro filas, y el precio no es ninguna.', abajo=True), 'verde', 'deslizá'),
    slide(eyebrow('La tabla') + titulo('El precio se compara al final.')
          + bajada('Antes, se compara todo lo demás. Cuatro criterios que el comprador revisa sin decírtelo.')
          + tabla(FIL, 0, COLS), 'hueso', 2, T),
    slide(eyebrow('Fila 01') + titulo('La web.')
          + bajada('Carga en el celular. Dice a quién le vende. Termina en una reunión, no en un formulario que nadie lee.')
          + tabla(FIL, 1, COLS, estado='fila'), 'verde', 3, T),
    slide(eyebrow('Fila 02') + titulo('Las redes.')
          + bajada('Fecha de la última publicación. Si es de hace meses, el comprador lee que la empresa está parada.')
          + tabla(FIL, 2, COLS, estado='fila'), 'verde', 4, T),
    slide(eyebrow('Fila 03') + titulo('La respuesta.')
          + bajada('Cuánto tarda en volver el primer mensaje. Horas o días. El que contesta primero, se queda con la reunión.')
          + tabla(FIL, 3, COLS, estado='fila'), 'negro', 5, T),
    slide(eyebrow('Fila 04') + titulo('Los números.')
          + bajada('Cuántos clientes, desde cuándo, qué instalaron. Un dato concreto pesa más que veinte adjetivos.')
          + tabla(FIL, 4, COLS, estado='fila'), 'negro', 6, T),
    slide(eyebrow('El resultado') + titulo('Gana el que parece más seguro. No el más barato.')
          + bajada('B ganó tres filas de cuatro. ¿En cuál columna estás vos?')
          + tabla(FIL, 4, COLS), 'hueso', 7, T),
    slide(eyebrow('Para hacer hoy') + titulo('Abrí tu web y la de tus dos competidores en tres pestañas.', cierre=True)
          + bajada('Llená la tabla sin hacerte trampa. Si no ganás tres filas de cuatro, escribinos: la primera fila se arregla en dos semanas.')
          + '<p class="btn">Reunión de 20 minutos</p>', 'verde', 8, T),
])

# ---------- C05 nadie tiene el número: dos columnas contrapuestas
T = 8
PIEZAS['carruseles/carrusel-05-nadie-tiene-el-numero'] = ('Nadie tiene el número', [
    slide(eyebrow('Seguridad electrónica · El informe') + titulo('Se invirtió en redes, catálogo y expo. <span class="ac">Nadie tiene el número.</span>', h1=True)
          + bajada('Lo que te dicen a fin de mes, y lo que te tendrían que decir. Cinco comparaciones, con un mes de ejemplo.', abajo=True), 'verde', 'deslizá'),
    slide(eyebrow('Uno') + titulo('Alcance no es demanda.')
          + bajada('Las personas que pasaron por delante del posteo no son empresas que quieren comprar.')
          + dos(('Lo que te dicen', '48.000', 'personas alcanzadas'), ('Lo que tiene que decir el informe', '37', 'contactos que llegaron'))
          + fuente('Mes de ejemplo con cifras ilustrativas.'), 'hueso', 2, T),
    slide(eyebrow('Dos') + titulo('Seguidores no son clientes.')
          + bajada('Un seguidor nuevo puede ser un estudiante, un competidor o un bot. Una empresa que escribe es otra cosa.')
          + dos(('Lo que te dicen', '+120', 'seguidores nuevos'), ('Lo que tiene que decir el informe', '9', 'empresas que escribieron')), 'verde', 3, T),
    slide(eyebrow('Tres') + titulo('Un posteo no es una reunión.')
          + bajada('Publicar es trabajo. Que alguien pida hablar con tu vendedor es el resultado. Se cuentan por separado.')
          + dos(('Lo que te dicen', '12', 'piezas publicadas'), ('Lo que tiene que decir el informe', '4', 'reuniones agendadas')), 'verde', 4, T),
    slide(eyebrow('Cuatro') + titulo('La expo no se mide en tarjetas.')
          + bajada('Doscientas tarjetas repartidas. La pregunta es cuántas se llamaron la semana siguiente.')
          + dos(('Lo que se cuenta', '200', 'tarjetas repartidas'), ('Lo que tiene que decir el informe', '0', 'llamados hechos después')), 'negro', 5, T),
    slide(eyebrow('Cinco') + titulo('Un cierre no es suerte.')
          + bajada('Si sabés de dónde vino, lo podés repetir. Si no, fue un mes bueno y ya.')
          + dos(('Lo que te dicen', '1', 'venta cerrada'), ('Lo que tiene que decir el informe', '2 de 4', 'reuniones cerradas, de 9 empresas, de 37 contactos'), med=True), 'negro', 6, T),
    slide(eyebrow('El informe que pedimos') + titulo('Cuatro números por canal. Todos los meses.')
          + bajada('Cuántos llegaron, por dónde, cuántos se llamaron y qué pasó después. Entra en una hoja. Si no está, no hubo medición.')
          + dos(('Por canal', 'Google · Instagram · Prospección · Prensa', 'de dónde vino cada contacto'), ('Por etapa', 'Llegaron · Llamados · Reuniones · Cerrados', 'qué pasó con cada uno'), chico=True), 'hueso', 7, T),
    slide(eyebrow('Para hacer hoy') + titulo('Pedile a tu agencia las reuniones del mes pasado.', cierre=True)
          + bajada('Mandanos qué te contestaron. Si la respuesta fue alcance, ya sabés qué falta.')
          + '<p class="btn">Reunión de 20 minutos</p>', 'verde', 8, T),
])

# ================================================================== ESTÁTICAS
PIEZAS['estaticas/estatica-01-dos-semanas'] = ('Dos semanas', [
    slide(eyebrow('Diagnóstico · Seguridad electrónica') + titulo('Dos semanas. <span class="ac">Un informe con números, no con opiniones.</span>', h1=True)
          + bajada('Miramos tu canal comercial entero: web, redes, respuesta, prospección. El día 14 sale un documento con lo que está pasando y qué cambiar primero.')
          + segmentos(14, 14) + fuente('Cada bloque es un día. El último, el informe.'), 'verde'),
])
PIEZAS['estaticas/estatica-02-cinco-por-dia'] = ('Cinco por día', [
    slide(eyebrow('Prospección · Contactos a tu nombre') + titulo('Cinco por día. <span class="ac">Cien por mes.</span>', h1=True)
          + bajada('Empresas de seguridad electrónica que sí pueden comprarte, contactadas a tu nombre todos los días hábiles. Tu vendedor recibe la lista con quién respondió.')
          + escalera([('5', 36, 'por día'), ('25', 120, 'por semana'), ('100', 250, 'por mes')]), 'negro'),
])
PIEZAS['estaticas/estatica-03-se-conocen-todos'] = ('Se conocen todos', [
    slide(eyebrow('Mercado · Seguridad electrónica') + titulo('Entre 100 y 150 empresas. <span class="ac">Se conocen todas.</span>', h1=True)
          + bajada('Ese es el rubro de la seguridad electrónica que le vende a empresas. Lo que le pasa a una se sabe en las otras. Un vendedor que llama tarde, también.')
          + red() + fuente('Estimación de Secure Growing sobre centrales de monitoreo, integradores y distribuidores de Buenos Aires.'), 'hueso'),
])
PIEZAS['estaticas/estatica-04-dieciseis-notas'] = ('Dieciséis notas', [
    slide(eyebrow('Contenido · Lo que publica la prensa del sector') + titulo('16 notas en 12 días. <span class="ac">¿Cuántas publicaste vos?</span>', h1=True)
          + bajada('Eso publicó la revista del sector en dos semanas de agosto. En este rubro el contenido sobra: lanzamientos, normas, obras, expos. Lo que falta es un sistema para sacarlo.')
          + comparativa([('Revista del sector, 3 al 15 de agosto', ('16 notas', 100), False), ('Tu Instagram, mismo período', 'completá vos', True)])
          + fuente('InfoSeguridad, 3 al 15 de agosto de 2026. Conteo propio.'), 'verde'),
])
PIEZAS['estaticas/estatica-05-tres-cosas'] = ('Tres cosas', [
    slide(eyebrow('Secure Growing · Qué resolvemos') + titulo('Tres cosas. <span class="ac">Nada más que esas.</span>', h1=True)
          + pilas([('Más demanda calificada', 'Contactamos a las empresas que sí pueden comprarte. No mandamos volumen.'),
                   ('Posicionamiento técnico', 'Que cuando te comparen contra tres proveedores, el más serio seas vos.'),
                   ('Contenido que convierte', 'Le hablamos al que firma la compra, no al público general.')])
          + '<p class="btn">Reunión de 20 minutos</p>', 'verde'),
])

# ================================================================== escribir
for rel, (tit, slides) in PIEZAS.items():
    path = os.path.join(ROOT, rel + '.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(doc(tit, slides))
    print('ok', rel, len(slides), 'slides')
