#!/usr/bin/env python3
"""Caso GICI — 4 slides. La prueba es una busqueda de Google.

Medido el 21/09/2026 con Chrome sin sesion (perfil nuevo en cada vuelta,
pws=0, gl=ar), tres veces cada busqueda. Posicion contando solo los sitios,
sin los anuncios ni el mapa:

  estudio contable ituzaingo ............... 1, 1, 1
  contador monotributo ituzaingo ........... 1, 1, 1
  contador para monotributistas ituzaingo .. 1, 1, 1
  contador pymes ituzaingo ................. 1, 1 (una vuelta no cargo)
  liquidacion de sueldos ituzaingo ......... 3, 2

OJO con lo que NO se puede decir: arriba de GICI hay 3 anuncios pagos y el
mapa con 4 estudios (GICI no esta en el mapa: le falta la ficha de Google).
Por eso el titular dice "arriba de Paginas Amarillas", que es literal, y el
dato gigante aclara que se cuentan los sitios, sin anuncios ni mapa.

Google ahora manda los links por /goto?url=, asi que para medir hay que leer el
dominio del texto visible del resultado (el <cite>), no del href.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, dato, ventana, buscador, cta

D = pathlib.Path(__file__).resolve().parent
SERP = img('trabajos/gici-google-primero.webp', 'image/webp')

SLIDES = [
    ('', '',
     h('Buscá esto<br>en <span class="mark">Google</span>.', 'lg')
     + buscador('estudio contable ituzaingo')),

    ('mist', 'Caso real · GICI · Ituzaingó',
     h('Sale arriba de<br><span class="mark">Páginas Amarillas</span>.', 'md')
     + ventana(SERP, 'google.com/search?q=estudio+contable+ituzaingo',
               'Resultado de Google con el sitio de GICI marcado')),

    ('navy', '',
     dato('#1', 'en cuatro de las cinco<br>búsquedas que medimos.',
          'Estudio contable, contador monotributo, contador para monotributistas y contador pymes, '
          'en Ituzaingó. Contando los sitios, sin los anuncios ni el mapa. Medido el 21/09, tres '
          'veces cada búsqueda, en un Chrome sin sesión.')),

    ('', '',
     h('¿Y a tu negocio<br>lo <span class="mark">encuentran</span>?', 'lg')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso GICI', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
