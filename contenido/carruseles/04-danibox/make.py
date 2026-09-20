#!/usr/bin/env python3
"""Caso Dani BOX — 4 slides, con el molde nuevo.

Dos variantes que no estaban en los carruseles anteriores: el dato gigante
(slide 2) y la captura anotada (slide 3). Hook y cierre van sin bajada y sin
etiqueta, y el pie queda minimo: asi los edito Mateo a mano en Canva.

Verificado en dani-box.vercel.app el 20/09/2026: 16 turnos por semana
(4 los lunes, miercoles y viernes; 2 los martes y jueves; sabado y domingo sin
clases), cada turno de una hora y media, y 5 accesos a WhatsApp, cada uno con
su mensaje ya escrito. El hook es el titular del hero de la web. Los anos quedan en 25,
como dice el sitio, hasta que Dani confirme si son 26.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import img, render
from sistema import page, h, dato, split, anotada, cta

D = pathlib.Path(__file__).resolve().parent
CELU = img('trabajos/danibox-castelar-horarios-celular.webp', 'image/webp')
OPIN = img('trabajos/danibox-castelar-opiniones-celular.webp', 'image/webp')

SLIDES = [
    ('', '',
     h('Acá se aprende<br>a boxear y a<br><span class="mark">bancar al de<br>al lado</span>.', 'lg')),

    ('navy', 'Caso real · Dani BOX · Club Castelar',
     split(dato('4,4', 'de puntaje<br>en Google.',
                'Las opiniones de los alumnos van en la web copiadas tal cual, con nombre y con el lugar donde las escribieron.'),
           OPIN, 'Opiniones de alumnos en la web de Dani BOX')),

    ('mist', 'Qué construimos',
     anotada(CELU, [
         ('Los 16 turnos, día por día',
          'Con la hora de inicio y la de fin. Cada uno dura una hora y media.'),
         ('Cinco accesos a WhatsApp',
          'Cada uno con el mensaje ya escrito: probar una clase, elegir turno, sumarse a entrenar.'),
         ('También lo que no hay',
          'Sábado y domingo dice “sin clases”, para que nadie llegue y encuentre todo cerrado.'),
     ], 'Horarios de Dani BOX en el celular')),

    ('', '',
     h('Por WhatsApp queda<br>sólo lo que<br><span class="mark">necesita charla</span>.', 'md')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Dani BOX', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
