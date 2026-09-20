#!/usr/bin/env python3
"""Caso MC E Bikes — 4 slides.

Angulo: una compra de dos millones no se decide en un chat. Todo lo que se
afirma esta verificado abriendo mc-ebikes.vercel.app el 20/09/2026: cuatro
modelos, precios de $1.890.000 a $2.590.000, 12 cuotas sin interes desde
$157.500, test ride en Castelar y service propio.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, sub, split, cta

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/mc-ebikes-castelar-tienda-celular.webp', 'image/webp')

SLIDES = [
    ('', 'Caso real · MC E Bikes · Castelar',
     h('Nadie compra<br>una bici de<br><span class="mark">$1.890.000</span><br>por un DM.', 'lg')
     + sub('Le armamos la tienda a MC E Bikes, que vende fat e-bikes en Castelar.')),

    ('mist', 'El problema',
     h('Una compra cara<br>no se decide<br>en un <span class="mark">chat</span>.', 'md')
     + sub('Antes de poner dos millones, la persona quiere ver la ficha entera: cuánta potencia tiene, cuánto dura la batería y en cuántas cuotas lo paga. Eso no entra en una respuesta de Instagram.')),

    ('navy', 'Qué construimos',
     split(h('Cuatro modelos.<br>Cada uno con<br>su ficha y<br><span class="blue">su precio</span>.', 'sm')
           + sub('Potencia, autonomía y velocidad de cada bici. Las 12 cuotas sin interés ya calculadas. Y una calculadora de ahorro que aclara, en la misma página, que es orientativa.'),
           CELU, 'Tienda de MC E Bikes en el celular')),

    ('', 'Qué tiene hoy',
     h('El que entra<br>ya sabe cuál quiere<br>y <span class="mark">cuánto paga</span>.', 'md')
     + sub('Desde $1.890.000, en 12 cuotas sin interés desde $157.500. Test ride en Castelar y service propio: lo mismo que contestaban veinte veces por mensaje.')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso MC E Bikes', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
