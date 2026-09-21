#!/usr/bin/env python3
"""Caso Motos Roll — 4 slides.

Tres slides: foto real del taller (de la galeria del sitio), la captura anotada
de la seccion de seguros y el cierre. Se probo un cuarto slide de color pleno y
se saco: estiraba una idea que entra en tres.

Verificado en motosroll.com.ar el 20/09/2026: la seccion "Servicio para
aseguradoras" con presupuesto detallado, informe con fotos, respuesta rapida y
reparacion garantizada, su propio boton "Pedir presupuesto" y la linea
"Atendemos siniestros de motos de toda la zona oeste".
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, anotada, cta, fondo

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/motos-roll-ituzaingo-seguros-celular.webp', 'image/webp')
TALLER = img('trabajos/motos-roll-ituzaingo-taller-foto.webp', 'image/webp')

SLIDES = [
    ('foto', '',
     fondo(TALLER, 'Una moto sobre el elevador en el taller de Motos Roll')
     + h('El trabajo que<br>mejor paga no<br><span class="mark">estaba escrito</span>.', 'lg')),

    ('mist', 'Caso real · Motos Roll · Ituzaingó',
     anotada(CELU, [
         ('Presupuestos para las aseguradoras',
          'Mano de obra y repuestos discriminados, en el formato que pide la compañía. Con su propio botón.'),
         ('Informe con fotos de cada daño',
          'Para que la aseguradora autorice la reparación sin idas y vueltas.'),
         ('“Atendemos siniestros de toda la zona oeste”',
          'Ahora está escrito en la página, y no sólo en la cabeza del mecánico.'),
     ], 'Sección de seguros de Motos Roll en el celular')),

    ('', '',
     h('Ahora cualquiera<br>que chocó la moto<br><span class="mark">lo encuentra</span>.', 'md')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Motos Roll', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
