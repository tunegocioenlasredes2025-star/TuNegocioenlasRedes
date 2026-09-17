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

## Archivos

- `build.py` — render a PNG 2x + PDF vectorial
- `carruseles/<nombre>/make.py` — copy y estructura de cada carrusel
- `carruseles/<nombre>/index.html` — standalone, se puede abrir en el navegador
