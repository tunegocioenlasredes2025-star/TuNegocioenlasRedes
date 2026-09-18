#!/usr/bin/env python3
"""Caso real — Mundo Cortinas (Castelar).

Todo lo que se afirma sale de la ficha del caso en index.html, que se escribio
abriendo el sitio. Ningun numero inventado: los dos que aparecen (cuatro pasos,
seis accesos a WhatsApp) estan ahi.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, sub, split, pasos, cta

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/mundo-cortinas-web-celular.webp', 'image/webp')

SLIDES = [
    ('', 'Caso real · Mundo Cortinas · Castelar',
     h('Contestás lo mismo<br><span class="mark">todos los días</span>.', 'lg')
     + sub('Y no es atención al cliente: es trabajo que la web tendría que estar haciendo por vos.')),

    ('mist', 'El problema',
     h('Nadie compra una cortina<br>a medida sin que alguien<br>se lo <span class="mark">explique</span>.', 'md')
     + sub('La diferencia entre una black out y una sunscreen no se entiende mirando una foto.')),

    ('', 'Lo que pasaba',
     h('Si eso no está escrito,<br>la explicación arranca<br>de <span class="mark">cero</span> en cada consulta.', 'md')
     + sub('Y el que explica siempre es el dueño. En el mostrador, por teléfono y por WhatsApp. El mismo párrafo, todos los días.')),

    ('mist', 'Qué construimos',
     split(h('Una ficha<br>propia para<br>cada <span class="blue">tipo de<br>cortina</span>.', 'sm')
           + sub('Cada una con su página, su explicación y su botón de consulta.'),
           CELU, 'Web de Mundo Cortinas en el celular')),

    ('', 'El detalle',
     h('La paleta de telas,<br>para mirar <span class="mark">antes</span><br>de decidir.', 'md')
     + sub('Elegir la tela es la parte que más frena una compra. Ahora se mira en el celular, a las once de la noche, sin nadie esperando una respuesta.')),

    ('mist', 'Y el proceso, escrito',
     h('Cuatro pasos.<br>El que entra sabe<br>qué va a pasar.', 'md')
     + pasos([('01', 'Asesoramiento', 'Qué cortina va en ese ambiente'),
              ('02', 'Medición', 'En el lugar, sin cargo'),
              ('03', 'Fabricación', 'A medida'),
              ('04', 'Colocación', 'La ponen ellos')])),

    ('navy', 'Qué tiene hoy',
     h('La persona llega<br>sabiendo qué<br><span class="blue">producto quiere</span>.')
     + sub('Seis accesos a WhatsApp y el teléfono a la vista en el encabezado. La charla ya no arranca en el paso uno.')),

    ('navy', '¿Te pasa lo mismo?',
     h('¿Cuántas veces<br>por semana explicás<br>lo <span class="blue">mismo</span>?', 'md')
     + sub('Si la respuesta te dio un número, eso ya es una página de tu web. Te la mostramos andando en 72 hs, gratis.')
     + cta('Escribinos')),
]

(D / 'index.html').write_text(page('TNR — Mundo Cortinas', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
