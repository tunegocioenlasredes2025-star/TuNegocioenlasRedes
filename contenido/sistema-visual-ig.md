# Sistema visual — Instagram

Traslado literal del rediseño v3 de la web (`styles.css`). Mismos tokens,
mismas tipografías, misma firma. Quien ve el feed y después entra al sitio
tiene que sentir que es el mismo lugar.

## Paleta

```css
--paper:  #FFFFFF   /* fondo principal */
--mist:   #F2F6FC   /* fondo alternativo, para que el grid respire */
--ink:    #0A1B33   /* titulares */
--ink-2:  #46526B   /* bajadas */
--muted:  #6B7690   /* pie */
--navy:   #003878   /* slide de impacto, 1 cada 4 */
--blue:   #1657D0   /* etiquetas, botones, palabra destacada */
--sky:    #00A8E8   /* solo decoración: el guion de la etiqueta. NUNCA texto */
--hl:     #A8E1F8   /* marcador detrás de la palabra clave — la firma */
```

**El cambio grande: el feed pasa de oscuro a claro.** No es un capricho
estético, son tres razones:
1. La web es blanca. Hoy el feed y el sitio parecen dos marcas distintas.
2. El azul marino sobre negro es el uniforme de las agencias de marketing.
   Un feed blanco con un marcador celeste se reconoce de lejos en la grilla.
3. Las capturas de las webs de los clientes son casi todas oscuras. Sobre
   fondo blanco resaltan; sobre fondo negro desaparecen.

## Tipografía

| Rol | Fuente | Peso | Detalles |
|---|---|---|---|
| Titular | Bricolage Grotesque | 800 | `line-height: 1.02`, `letter-spacing: -.03em` |
| Bajada | Figtree | 400 | `line-height: 1.42`, color `--ink-2` |
| Etiqueta / pie | Figtree | 700 | mayúsculas, `letter-spacing: .16em` |

Van embebidas en base64 dentro del HTML: el archivo abre y renderiza igual
sin internet, y el PNG sale siempre con la tipografía correcta.

Escalas de titular sobre 1080×1350: `112px` (hero) · `92px` · `74px` ·
`60px` (slides con imagen al costado).

## Reglas de armado

1. **Todo alineado a la izquierda.** Sin excepciones. Nada centrado.
2. **Margen de seguridad de 88px** en los cuatro lados.
3. **Una idea por slide.** Si necesita dos párrafos, son dos slides.
4. **El marcador celeste se usa una vez por slide.** Dos marcas en el mismo
   titular anulan las dos.
5. **Ritmo de fondos:** blanco → gris claro → blanco → navy. El slide navy es
   el golpe: va donde está el giro o el dato, nunca en el hero.
6. **El pie es fijo:** isotipo + `tunegocioenlasredes.com.ar` a la izquierda,
   `01 / 08` a la derecha, `DESLIZÁ →` al medio salvo en el último.
7. **Fotos de banco: no.** Captura real de cliente, foto propia, o tipografía
   sola. Un slide tipográfico bien armado le gana a una foto de Unsplash.
8. **Sin números en la esquina, sin degradés, sin sombras sobre el texto.**
   Lo que se lee tiene que leerse en el celular de alguien de 55 años.

## Estructura de carrusel (caso real)

| Slide | Etiqueta | Función |
|---|---|---|
| 01 | CASO REAL · [negocio] · [barrio] | Hook. La tensión, sin resolver |
| 02 | EL PROBLEMA | El problema del rubro, en una frase |
| 03 | LO QUE PASABA | El costo concreto de ese problema |
| 04 | QUÉ CONSTRUIMOS | Navy + captura del cliente. La decisión |
| 05 | EL DETALLE | Una sola decisión chiquita, bien explicada |
| 06 | QUÉ TIENE HOY | El resultado verificable |
| 07 | — | CTA: demo gratis en 72 hs |

## Chequeo automático de titulares

Un titular con saltos de línea puestos a mano se puede partir igual si la línea
no entra a lo ancho, y eso arruina el ritmo del slide sin que salte a la vista.
`build.py` compara los renglones que se dibujaron contra los que pide el copy y
avisa en la consola:

```
! slide 2: el titular se corta en 5 lineas y el copy pide 3 -> Nadie compra una cortina...
```

Cuando aparece, se baja un escalón de tamaño (`xl` → `lg` → `md` → `sm`) o se
reescribe la línea más larga. Como referencia: en `lg` entran unos 19 caracteres
por línea, en `md` unos 24.

## Archivos

- `sistema.py` — la paleta, las tipografías, el molde de slide y los bloques
  (`h`, `sub`, `split`, `pasos`, `vs`, `cta`). **Un solo lugar:** si hay que
  cambiar un color o un tamaño, se cambia acá y cambian todos los carruseles
- `build.py` — render a PNG 2x + PDF vectorial + hoja de contacto
- `fuentes-para-canva/` — las tres caras estáticas: `.woff2` para el HTML,
  `.ttf` para subir a Canva
- `carruseles/<nombre>/make.py` — solo el copy y el orden de los slides
- `carruseles/<nombre>/caption.txt` — el texto del posteo
- `carruseles/<nombre>/index.html` — standalone, se abre en cualquier navegador

## Cómo se arma uno nuevo

Copiar un `make.py` existente, cambiar la lista `SLIDES` y correr:

```
python3 contenido/build.py contenido/carruseles/<carpeta>
```
