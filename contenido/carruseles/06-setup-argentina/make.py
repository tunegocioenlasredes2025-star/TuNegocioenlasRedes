#!/usr/bin/env python3
"""Caso Setup Argentina — 4 slides.

Angulo: un estudio argentino con la web en ingles. La pregunta se hace sola y
la respuesta es la estrategia: sus clientes estan afuera, y por eso tambien los
anuncios de Google apuntan a Estados Unidos.

La primera version contaba una cronologia ("le entregamos la web en julio, en
septiembre seguimos") y a Mateo no le gusto: contaba fechas, no una idea.

Verificado en setupargentina.com el 21/09/2026:
  - la foto de Agustin Sofia esta publicada en /about/ ("founder of SetUp
    Argentina")
  - el sitio sale en ingles por defecto, con el espanol en /es/ y el aviso
    "This page is also available in Spanish"
  - dice que hace constitucion de sociedades, impuestos y contabilidad "for
    foreign investors and local companies alike"
  - el blog esta armado pero todavia sin notas: el copy dice "para publicar"
  - la campana de Google Ads apunta a Estados Unidos (publicada el 06/09/2026)

No se usa el "50+ foreign companies incorporated" del sitio: es un dato del
cliente que no podemos verificar. Tampoco se dice cuanto paga.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, sub, anotada, cta, fondo

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/setup-argentina-sitio-ingles-celular.webp', 'image/webp')
AGUS = img('trabajos/setup-argentina-agustin-foto.webp', 'image/webp')

SLIDES = [
    ('foto', '',
     fondo(AGUS, 'Agustín Sofía, fundador de Setup Argentina')
     + h('¿Por qué Agustín<br>tiene la web<br><span class="mark">en inglés</span>?', 'lg')),

    ('navy', 'Caso real · Setup Argentina',
     h('Porque sus<br>clientes están<br><span class="blue">afuera</span>.', 'lg')
     + sub('Arma empresas en Argentina para inversores del exterior. Por eso la web arranca en inglés, y por eso los anuncios de Google apuntan a Estados Unidos.')),

    ('', 'Qué construimos',
     anotada(CELU, [
         ('En inglés por defecto',
          'Lo primero que ve un inversor de afuera es su idioma.'),
         ('El español, a un toque',
          'Y un aviso que se lo ofrece al que entra desde Argentina, sin cambiarle el idioma a la fuerza.'),
         ('Un blog para sus propias notas',
          'Las escribe él; nosotros armamos el lugar para publicarlas.'),
     ], 'Sitio de Setup Argentina en inglés, en el celular')),

    ('', '',
     h('Tu web tiene que<br>hablar el idioma de<br><span class="mark">quien te compra</span>.', 'md')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Setup Argentina', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
