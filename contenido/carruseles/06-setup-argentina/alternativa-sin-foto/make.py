#!/usr/bin/env python3
"""Setup Argentina, version B: sin la foto de Agustin.

Por si a Agus le resulta invasivo aparecer en el gancho. En lugar de la cara,
el propio sitio: el slide 1 muestra la web en ingles y el 3 la version en
espanol, asi se ven las dos caras del mismo sitio. El resto del argumento es
el mismo que la version A (la carpeta de arriba).

Verificado en setupargentina.com y setupargentina.com/es/ el 21/09/2026.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from build import img, render
from sistema import page, h, sub, split, anotada, cta

D = pathlib.Path(__file__).resolve().parent
EN = img('trabajos/setup-argentina-sitio-ingles-celular.webp', 'image/webp')
ES = img('trabajos/setup-argentina-sitio-espanol-celular.webp', 'image/webp')

SLIDES = [
    ('', '',
     split(h('¿Por qué un<br>estudio argentino<br>tiene la web<br><span class="mark">en inglés</span>?', 'sm'),
           EN, 'Sitio de Setup Argentina en inglés, en el celular')),

    ('navy', 'Caso real · Setup Argentina',
     h('Porque sus<br>clientes están<br><span class="blue">afuera</span>.', 'lg')
     + sub('Arma empresas en Argentina para inversores del exterior. Por eso la web arranca en inglés, y por eso los anuncios de Google apuntan a Estados Unidos.')),

    ('mist', 'Qué construimos',
     anotada(ES, [
         ('La misma web, en español',
          'A un toque desde el botón de arriba, para los clientes de acá.'),
         ('Cada idioma con su dirección',
          'El inglés en la principal y el español en /es/, cada uno por separado.'),
         ('Un blog para sus propias notas',
          'Las escribe él; nosotros armamos el lugar para publicarlas.'),
     ], 'Sitio de Setup Argentina en español, en el celular')),

    ('', '',
     h('Tu web tiene que<br>hablar el idioma de<br><span class="mark">quien te compra</span>.', 'md')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Setup Argentina (sin foto)', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
