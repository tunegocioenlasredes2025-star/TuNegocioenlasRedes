#!/usr/bin/env python3
"""El detalle — por que en la web de TonCars hay diez botones de WhatsApp.

Pilar "el detalle": una decision chiquita de un trabajo real, explicada. Es el
tipo de posteo que no puede copiar nadie, porque la decision la tomamos nosotros.

El dato de los diez accesos y el de la consulta que entra con el vehiculo ya
elegido salen de la ficha del caso en index.html.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, sub, split, vs, cta

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/toncars-automotores-web-celular.webp', 'image/webp')

SLIDES = [
    ('', 'El detalle · Desarrollo web',
     h('En la web de TonCars<br>hay <span class="mark">diez botones</span><br>de WhatsApp.', 'md')
     + sub('No es un error. Es la decisión que más cambió las consultas que le entran.')),

    ('mist', 'La idea que suena bien',
     h('«Con un botón alcanza.<br>El que quiere escribir,<br>lo busca.»', 'md')
     + sub('Suena razonable. Es la frase que más consultas hace perder.')),

    ('', 'Por qué no',
     h('Nadie decide escribir<br>al principio.<br>Decide en el <span class="mark">medio</span>.', 'md')
     + sub('La persona se convence mirando una unidad puntual: el año, el kilometraje, si le toman el suyo en parte de pago. Y eso pasa scrolleando, lejos del encabezado.')),

    ('navy', 'La regla',
     split(h('El botón va<br>donde aparece<br>la <span class="blue">decisión</span>.', 'sm')
           + sub('No donde nos queda cómodo a nosotros.'),
           CELU, 'Web de TonCars en el celular')),

    ('mist', 'El detalle que importa',
     h('Los diez botones<br>no dicen<br>lo <span class="mark">mismo</span>.', 'md')
     + sub('El de la ficha de un auto abre el chat con ese vehículo ya escrito en el mensaje. El del encabezado no puede hacer eso: todavía no sabe qué está mirando.')),

    ('', 'Qué cambia',
     h('Cambia el mensaje<br>que te entra.', 'md')
     + vs('«Hola, ¿cuánto sale?»',
          'El modelo y el año ya escritos, y la pregunta concreta')),

    ('mist', 'La regla, en una línea',
     h('Un botón por momento<br>de decisión.<br>No uno por página.', 'md')
     + sub('Si la persona tuvo que volver hasta arriba para escribirte, ya la perdiste.')),

    ('navy', 'Probá esto hoy',
     h('Abrí tu web<br>y contá los <span class="blue">botones</span>.', 'md')
     + sub('Si hay uno solo y está arriba de todo, escribinos. Te mostramos cómo quedaría la tuya andando en 72 hs, gratis.')
     + cta('Escribinos')),
]

(D / 'index.html').write_text(page('TNR — Diez botones de WhatsApp', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
