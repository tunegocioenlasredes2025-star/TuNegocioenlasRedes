#!/usr/bin/env python3
"""Muestra de estilo — caso TonCars, 4 slides.

Fue la prueba para validar el traslado de la web v3 a Instagram. Se deja como
referencia del molde minimo: hero, problema, captura y resultado.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, sub, split, cta

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/toncars-automotores-web-celular.webp', 'image/webp')

SLIDES = [
    ('', 'Caso real · TonCars · Ing. Maschwitz',
     h('El problema<br>no era la web.<br>Era el <span class="mark">primer<br>mensaje</span>.', 'lg')
     + sub('Cómo hicimos que cada consulta llegue con el auto ya elegido.')),

    ('mist', 'El problema',
     h('Un usado se vende<br>con la foto y el precio<br><span class="mark">a la vista</span>.', 'md')
     + sub('Si cada unidad vive en una publicación suelta, la persona compara en otra pestaña. Y no vuelve.')),

    ('navy', 'Qué construimos',
     split(h('Una ficha<br>por auto.<br>Con su propio<br><span class="blue">botón de<br>consulta</span>.', 'sm')
           + sub('Financiación, permuta, consignación y el paso a paso de la compra: escritos una vez, para siempre.'),
           CELU, 'Web de TonCars en el celular')),

    ('', 'Qué tiene hoy',
     h('Cada consulta entra<br>con el <span class="mark">vehículo<br>ya elegido</span>.')
     + sub('Diez accesos a WhatsApp en la misma página. Nadie más escribe «hola, ¿cuánto sale?».')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — muestra de estilo IG', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
