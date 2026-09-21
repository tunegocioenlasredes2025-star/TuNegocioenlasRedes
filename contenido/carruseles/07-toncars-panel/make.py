#!/usr/bin/env python3
"""Caso Ton Cars, el panel — 4 slides, sin celular.

Ya habia un carrusel de Ton Cars (00-muestra-estilo) con la captura en el
celular. Este cambia de estetica a proposito: foto real de un auto a sangre,
antes/despues en texto, y la web en computadora dentro de una ventana de
navegador.

Verificado el 21/09/2026:
  - toncars.com.ar/admin: "Desde aca cargas, editas y das de baja vehiculos del
    catalogo de la web. Los cambios se publican solos en 1 o 2 minutos."
  - toncars.com.ar/api/estado responde {"ok":true}: el panel esta andando
  - el catalogo tiene 17 fichas, cada una con precio y boton "Consultar" por
    WhatsApp
  - la foto de la Amarok es la del propio catalogo (con el cartel de TON CARS)
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, vs, ventana, cta, fondo

D = pathlib.Path(__file__).resolve().parent
AUTO = img('trabajos/toncars-amarok-foto.webp', 'image/webp')
CATALOGO = img('trabajos/toncars-catalogo-escritorio.webp', 'image/webp')

SLIDES = [
    ('foto', '',
     fondo(AUTO, 'Una Amarok en el local de Ton Cars')
     + h('Entra un auto.<br>A los dos minutos<br><span class="mark">ya está en la web</span>.', 'lg')),

    ('mist', 'Caso real · Ton Cars · Ing. Maschwitz',
     h('El catálogo<br>lo maneja él.', 'lg')
     + vs('Cada auto nuevo era un mensaje a la agencia, y esperar a que lo subieran.',
          'Gastón lo carga desde el panel, con fotos y precio, y se publica solo en uno o dos minutos.')),

    ('', 'Qué construimos',
     h('17 autos, cada uno<br>con su precio y su<br><span class="mark">botón de consulta</span>.', 'sm')
     + ventana(CATALOGO, 'toncars.com.ar/catalogo', 'Catálogo de Ton Cars en la computadora')),

    ('navy', '',
     h('Tu web no tendría<br>que depender<br>de <span class="blue">nosotros</span>.', 'md')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Ton Cars, el panel', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
