# El PDF editable para Canva

Respuesta a "¿nos lo pasás en PDF y lo editamos en Canva?": **sí, funciona,
pero conviene usarlo para lo que sirve y no para todo.**

## Qué probamos y qué salió

El `editable-canva.pdf` que genera `build.py` está verificado:

| Chequeo | Resultado |
|---|---|
| Páginas | 4 para 4 slides, sin páginas en blanco de más |
| Medida | 11,25 × 14,07 pulgadas = 1080 × 1350 px exactos |
| Texto | Texto de verdad, no imagen. Cada renglón es un objeto suelto → cada uno entra a Canva como su propia caja editable |
| Tipografías | Bricolage Grotesque y Figtree **embebidas en el archivo** |

Los dos problemas que había y cómo se resolvieron, por si algún día hay que
tocar el build:

1. **Las tipografías salían cambiadas.** Chromium no puede meter una fuente
   *variable* adentro de un PDF; la reemplaza en silencio por la del sistema.
   Se resolvió generando instancias estáticas (`fuentes-para-canva/*.woff2`).
2. **Aparecían páginas en blanco.** El bloque `@media print` estaba escrito
   antes que `body` en la hoja de estilos y perdía por orden de cascada, así
   que el margen del navegador seguía vivo y cada slide se pasaba de página.
   Ahora va al final y se imprime un slide por vez.

## Cómo importarlo

1. **Subir las tipografías primero.** Canva Pro → Marca → Fuentes → subir los
   tres archivos de `contenido/fuentes-para-canva/*.ttf`. Sin esto Canva las
   reemplaza al editar y se cae todo el diseño.
   *(Si no hay Canva Pro, no se pueden subir fuentes: ahí el PDF sirve para
   mover textos, no para editarlos conservando la tipografía.)*
2. Archivo → Importar → el `editable-canva.pdf`.
3. Elegir **"Editar"**, no "Aplanar".
4. Revisar el primer slide: cada línea de titular es una caja aparte. Si se
   edita una línea larga, hay que reacomodar las de abajo a mano.

## Mi recomendación, honesta

El ida y vuelta por Canva tiene un costo que se paga en cada posteo: los
titulares entran cortados en una caja por renglón, y eso hace que cambiar una
palabra obligue a reacomodar tres líneas. Para retoques chicos va bien. Para
rehacer un carrusel entero, es más trabajo del que parece.

Propongo los tres a la vez, y que cada uno se use para lo suyo:

| Entrega | Para qué |
|---|---|
| `png/slide-XX.png` | **Publicar.** 2160×2700, ya está. El 90% de las veces no hace falta tocar nada |
| `editable-canva.pdf` | **Retocar.** Cambiar una palabra, mover algo, hacer una versión |
| El copy en texto plano | **Reescribir.** Si hay que cambiar el mensaje, se cambia acá y se vuelve a generar |

Y una cosa más, para más adelante: cuando el sistema esté firme después de 3 o
4 carruseles, conviene **armar los 6 layouts una sola vez como plantilla de
Canva.** Ahí editar deja de ser importar un PDF y pasa a ser cambiar el texto
sobre un molde. Es medio día de trabajo que se recupera en un mes.

Mientras tanto, el PDF de la muestra está listo: probalo, importalo, y decime
si el resultado adentro de Canva te sirve. Con eso decidimos si seguimos por
ese camino o armamos la plantilla directamente.
