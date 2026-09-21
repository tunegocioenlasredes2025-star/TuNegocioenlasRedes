#!/usr/bin/env python3
"""Caso Motos Roll — 4 slides.

Estilo nuevo: el slide 2 es un bloque de color a sangre, celeste pleno con una
sola frase. El 3 reusa la captura anotada.

Verificado en motosroll.com.ar el 20/09/2026: la seccion "Servicio para
aseguradoras" con presupuesto detallado, informe con fotos, respuesta rapida y
reparacion garantizada, su propio boton "Pedir presupuesto" y la linea
"Atendemos siniestros de motos de toda la zona oeste".
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, anotada, cta

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/motos-roll-ituzaingo-seguros-celular.webp', 'image/webp')

SLIDES = [
    ('', '',
     h('El taller ya hacía<br>un trabajo que<br><span class="mark">nadie sabía</span>.', 'lg')),

    ('cielo', 'Caso real · Motos Roll · Ituzaingó',
     h('Si no está<br>escrito,<br>no existe.', 'xl')),

    ('', 'Qué construimos',
     anotada(CELU, [
         ('La sección de seguros, con su propio botón',
          'Presupuesto con la mano de obra y los repuestos discriminados, en el formato que pide la compañía.'),
         ('Informe con fotos de cada daño',
          'Para que la aseguradora autorice la reparación sin idas y vueltas.'),
         ('“Atendemos siniestros de toda la zona oeste”',
          'Escrito en la página, no en la cabeza del mecánico.'),
     ], 'Sección de seguros de Motos Roll en el celular')),

    ('', '',
     h('Ahora el que tuvo<br>un siniestro<br><span class="mark">lo encuentra</span>.', 'lg')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Motos Roll', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
