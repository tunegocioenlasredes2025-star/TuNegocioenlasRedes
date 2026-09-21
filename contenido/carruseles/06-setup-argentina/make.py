#!/usr/bin/env python3
"""Caso Setup Argentina — 3 slides.

Angulo: la venta no termina cuando entregas la web. Es el unico caso que prueba
el escalon mensual, que es justo lo que hay que empezar a vender.

OJO CON LA FUENTE. A diferencia de MC E Bikes y Motos Roll, esto NO esta
verificado abriendo el sitio del cliente: quien lo escribio no tenia navegador.
Todo sale de la hoja Clientes de comercial/TNR-datos-para-el-analisis.xlsx,
cargada desde el CRM:

  - cierre 07/2026, ultimo movimiento 09/2026
  - web, despues web con blog, despues mantenimiento mensual, despues Google Ads
  - los anuncios apuntan a Estados Unidos
  - sigue activo y muy conforme

Nada de lo que dice el carrusel menciona cuanto paga: eso es informacion del
cliente y no se publica.

ANTES DE PUBLICAR hay que cerrar dos cosas (ver el NO-PUBLICAR de esta carpeta):
que Setup autorice, y confirmar con Mateo que los anuncios son a Estados Unidos.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from build import render
from sistema import page, h, sub, pasos, cta

D = pathlib.Path(__file__).resolve().parent

SLIDES = [
    ('', 'Caso real · Setup Argentina',
     h('Le entregamos<br>la web en julio.<br>En septiembre<br><span class="mark">seguimos</span>.', 'md')
     + sub('Lo que pasó en el medio es lo que casi ninguna agencia cuenta.')),

    ('mist', 'Cómo siguió',
     h('Una cosa<br>llevó a la otra.', 'lg')
     + pasos([('01', 'La web', 'Julio'),
              ('02', 'Una segunda web, con blog', 'Para publicar sus propias notas'),
              ('03', 'El mantenimiento', 'Todos los meses, sin que haya que pedirlo'),
              ('04', 'Los anuncios', 'Campañas de Google apuntadas a Estados Unidos')])),

    ('navy', '',
     h('El trabajo no<br>termina cuando<br><span class="blue">entregás</span>.', 'md')
     + sub('Empieza ahí. Una web nuestra no es un archivo que te mandamos y chau.')
     + cta('Te hacemos la demo gratis en 72 hs')),
]

(D / 'index.html').write_text(page('TNR — caso Setup Argentina', SLIDES), encoding='utf-8')
print('html: %.0f KB' % ((D / 'index.html').stat().st_size / 1024))
render(D)
