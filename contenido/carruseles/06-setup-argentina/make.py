#!/usr/bin/env python3
"""Caso Setup Argentina — 4 slides.

Angulo: la venta no termina cuando entregas la web. Es el unico caso que prueba
el escalon mensual, que es justo lo que hay que empezar a vender.

La primera version la armo una sesion sin navegador, desde la hoja Clientes del
CRM. Esta la termino una con navegador el 21/09/2026 y verifico en el sitio:

  - setupargentina.com esta online, en ingles por defecto, con la version en
    espanol en /es/ y el aviso "This page is also available in Spanish"
  - el blog existe pero TODAVIA NO TIENE NOTAS ("The first articles are on
    their way"): por eso el copy dice que es para publicar, no que publica
  - la campana de Google Ads apunta a Estados Unidos (publicada el 06/09/2026,
    segun las notas del proyecto)

No se usa el "50+ foreign companies incorporated" del sitio: es un dato del
cliente que no podemos verificar. Tampoco se dice cuanto paga.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, pasos, anotada, cta

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/setup-argentina-sitio-ingles-celular.webp', 'image/webp')

SLIDES = [
    ('', '',
     h('Le entregamos<br>la web en julio.<br>En septiembre<br><span class="mark">seguimos</span>.', 'md')),

    ('mist', 'Caso real · Setup Argentina',
     h('Una cosa<br>llevó a la otra.', 'lg')
     + pasos([('01', 'La web', 'Julio'),
              ('02', 'El sitio completo, en inglés', 'Para los clientes de afuera, con la versión en español a un click'),
              ('03', 'El mantenimiento', 'Todos los meses, sin que haya que pedirlo'),
              ('04', 'Los anuncios en Google', 'Apuntados a Estados Unidos')])),

    ('', 'Qué construimos',
     anotada(CELU, [
         ('En inglés por defecto',
          'Es un estudio de Buenos Aires que les vende a inversores del exterior.'),
         ('El español, a un toque',
          'Y un aviso que se lo ofrece al que entra desde Argentina, sin cambiarle el idioma a la fuerza.'),
         ('Un blog para sus propias notas',
          'Las escribe él; nosotros armamos el lugar para publicarlas.'),
     ], 'Sitio de Setup Argentina en inglés, en el celular')),

    ('navy', '',
     h('El trabajo no<br>termina cuando<br><span class="blue">entregás</span>.', 'md')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Setup Argentina', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
