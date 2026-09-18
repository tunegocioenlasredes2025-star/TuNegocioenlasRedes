# Editar los carruseles en Canva

**Importá el `.pptx`, no el `.pdf`.** Los dos están en la carpeta de cada
carrusel, pero hacen cosas distintas.

## Por qué el PDF se veía mal

Lo probaste y salieron tres cosas rotas. Las tres tienen la misma causa: Canva
importa PDF con un parser propio que reconstruye lo que puede.

| Lo que se veía | Por qué pasaba | Estado |
|---|---|---|
| El marcador celeste, como un **rectángulo negro** | Estaba hecho con un `linear-gradient` de CSS, y eso sale del PDF como un objeto `/Pattern`. Canva no lo interpreta y lo pinta negro | **Arreglado.** Ahora es una sombra interior sólida: en el PDF sale como un rectángulo relleno común |
| Las palabras **pegadas**: "DiezaccesosaWhatsApp" | Chromium escribe los espacios entre palabras como corrimientos de posición, no como el carácter espacio. Canva los ignora | **Sin arreglo posible desde el PDF.** Lo resuelve el PPTX |
| La **tipografía cambiada** | Canva sustituye cualquier fuente que no esté en tu kit de marca, aunque venga embebida en el archivo | Se resuelve subiendo las fuentes (abajo) |

## El camino bueno: PPTX

Canva importa PowerPoint como **elementos nativos**: cada texto entra como caja
de texto editable, cada fondo como forma, cada imagen como imagen. Las palabras
conservan sus espacios porque van escritas como texto de verdad.

### Los dos pasos

1. **Subí las tipografías primero.** Canva → Marca → Fuentes → subir los tres
   archivos de `contenido/fuentes-para-canva/*.ttf`. Necesitás Canva Pro.
   Hacelo **antes** de importar: si Canva no las encuentra, sustituye por una
   más ancha y los renglones se corren.
2. **Importá el `editable-canva.pptx`.** Archivo → Importar.

### Qué vas a poder tocar y qué no

- ✅ Todos los textos, uno por uno, con su tipografía, tamaño y color.
- ✅ Los fondos, los botones y las cajas de comparación: son formas con relleno.
- ✅ El marcador celeste: es un rectángulo suelto detrás de la palabra. Si
  editás el texto y cambia de largo, ese rectángulo hay que estirarlo a mano.
- ⚠️ Las capturas de los clientes entran como imagen plana, ya recortada.
- ⚠️ Los titulares vienen **sin ajuste automático de línea**, a propósito: los
  cortes de renglón los decidió el copy. Si escribís de más, el texto se pasa
  de largo en vez de reacomodarse solo. Es intencional — avisa que hay que
  reescribir más corto.

## Cómo se genera

```
python3 contenido/build.py contenido/carruseles/<carpeta>
```

Sale todo junto: los PNG para publicar, el PPTX para editar, el PDF de respaldo
y la hoja de contacto.

El PPTX no se escribe a mano: `pptx_export.py` abre el HTML en el navegador,
mide cada elemento con su estilo ya calculado y arma el archivo con esas
medidas. El HTML sigue siendo la única fuente, así que el PPTX nunca se
desincroniza del diseño.

## Lo que todavía no pude probar

No tengo forma de abrir un PPTX en esta máquina: LibreOffice está instalado sin
el módulo de presentaciones y no se puede instalar. Lo que sí verifiqué:

- Las 42 partes XML del archivo están bien formadas y python-pptx lo reabre.
- Las posiciones coinciden con el navegador **al píxel** (probado contra la
  etiqueta, el titular, la bajada y el número de slide).
- Los textos conservan los espacios, con `xml:space="preserve"` en cada corrida.
- Las tipografías quedan nombradas como Bricolage Grotesque y Figtree.

Falta el último paso, que es tuyo: importalo y decime cómo entra. Si algo queda
corrido, con una captura lo ajusto.

## El PDF, ahora

Sigue ahí y ya no tiene los rectángulos negros. Sirve para mirar, mandar por
WhatsApp o imprimir. Para editar, PPTX.
