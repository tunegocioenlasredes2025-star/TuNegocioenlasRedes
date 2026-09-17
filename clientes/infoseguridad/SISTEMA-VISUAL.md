# Sistema visual — infoseguridadAR

Sistema reconstruido midiendo el feed real de [@infoseguridadar](https://www.instagram.com/infoseguridadar/).
No es una reinterpretación: los valores de abajo salen de medir el post
"La democratización del IP" pixel por pixel y escalarlo a 1080.

**Modelo de publicación:** nota nueva en infoseguridadit.com → una estática
1080×1350 que invita a leerla en el link de la bio. Nada más.

---

## 1. Lienzo

| | |
|---|---|
| Medida | **1080 × 1350** (4:5, el formato que más pantalla ocupa en el feed) |
| Export | PNG retina 2× → 2160 × 2700 |
| Fondo | `#101214` — casi negro, **nunca** `#000` puro |
| Margen lateral | 44 px |
| Margen inferior | 76 px |

## 2. Paleta

| Rol | Hex | Uso |
|---|---|---|
| Fondo | `#101214` | lienzo |
| Verde de marca | `#7ED957` | píldora de rubro, palabra destacada, flecha y CTA |
| Blanco | `#FFFFFF` | titular |
| Gris bajada | `#B9C0C6` | bajada |
| Gris dominio | `#6E767C` | `infoseguridadit.com` |
| Tinta sobre verde | `#0B0D0E` | texto dentro de la píldora |

Un solo verde en toda la pieza. Si aparece un segundo acento, el sistema se rompe.

## 3. Tipografía

| Elemento | Fuente | Tamaño | Detalle |
|---|---|---|---|
| Titular | **Inter 900** | 67–113 px (automático) | `line-height: .91`, `letter-spacing: -.028em` |
| Bajada | **Inter 400** | 31 px | `line-height: 1.40` |
| Rubro / NOTA NUEVA | **JetBrains Mono 800** | 21 px | mayúsculas, `letter-spacing` .10 / .15em |
| CTA | **Inter 600** | 29 px | verde |
| Dominio | **Inter 500** | 21 px | gris |

El interlineado de `.91` es la firma de la marca: los renglones del titular casi
se tocan. Es lo que le da el golpe editorial.

Las fuentes van **embebidas en base64** dentro del HTML (`fonts_embedded.css`).
Nunca CDN: el render no depende de internet y el resultado es idéntico siempre.

## 4. Anatomía de la pieza

```
 0        ┌─────────────────────────────────┐
          │ [RUBRO] │ NOTA NUEVA            │  barra a 32 px del borde
 106 px   ├─────────────────────────────────┤
          │                                 │
          │          FOTO (bordes duros)    │  615 px de alto, full width
          │                                 │
 721 px   ├─────────────────────────────────┤
          │                                 │
          │ Titular con una palabra         │  bloque anclado abajo
          │ en verde.                       │
          │ Bajada de uno o dos renglones.  │
          │                                 │
          │ → Nota completa…    [logo]      │
          │                     dominio     │
 1350 px  └─────────────────────────────────┘
```

**La foto no sangra hasta arriba.** Arranca debajo de la barra de rubro y corta
con borde duro contra el fondo. Sin degradados ni viñetas: así es la marca.

## 5. Reglas de copy

- **Titular:** una afirmación, no el título de la nota. Cierra con punto o signo.
  Entre 40 y 90 caracteres. Una sola palabra (o dos) va en verde — la que carga
  el concepto, nunca un artículo ni un verbo auxiliar.
- **Bajada:** uno o dos renglones. Nombra la fuente (la marca, el entrevistado,
  el organismo) y el ángulo. Es la que da el contexto que el titular se guarda.
- **Rubro:** a quién le habla la nota — `INSTALADORES`, `DISTRIBUIDORES`,
  `INTEGRADORES`, `MONITOREO`, `INDUSTRIA`, `TECNOLOGÍA`.
- **CTA:** siempre "Nota completa en el link de la bio". No se toca.

## 6. Archivos

| Archivo | Qué es |
|---|---|
| `notas.json` | la cola de notas pendientes de subir |
| `plantilla.html` | el sistema visual en CSS |
| `generar.py` | arma el HTML y renderiza los PNG |
| `logo-infoseguridad.svg` | logo vectorial (ver abajo) |
| `fonts_embedded.css` | Inter + JetBrains Mono en base64 |
| `fotos/` | acá van las fotos de las notas |
| `salida/` | PNGs + `preview.html` + `contacto-hoja.png` |
| `copys.md` | los captions de Instagram |

## 7. Cómo sumar una nota

1. Poné la foto en `fotos/` (ideal 1080×615 o más grande, se recorta a `cover`).
2. Agregá el bloque en `notas.json`:

```json
{
  "id": "nombre-del-archivo",
  "rubro": "INSTALADORES",
  "sello": "NOTA NUEVA",
  "titular": "La afirmación que sostiene la nota.",
  "destacar": "afirmación",
  "bajada": "Quién lo dice y desde qué ángulo.",
  "foto": "mi-foto.jpg",
  "encuadre": "center"
}
```

3. `python3 generar.py` — o `python3 generar.py nombre-del-archivo` para una sola.

El titular se achica solo según el largo, así que no hay que tocar tamaños.
Si una nota no tiene foto, dejá `"foto": null` y sale en **modo tipográfico**
(fondo oscuro con trama técnica), que también es parte del sistema.

`encuadre` acepta cualquier `background-position` de CSS (`center`, `center top`,
`70% 30%`) para reencuadrar sin editar la foto.

## 8. El logo

El PNG original venía a 467×140 px: sirve para la web chica, no para imprimir ni
para escalar. Lo **revectoricé**: separé la capa verde de la blanca, tracé los
contornos y los guardé como SVG con las curvas reales.

`logo-infoseguridad.svg` ahora escala a cualquier tamaño sin perder un pixel, pesa
19 KB y toma el color de dos variables CSS (`--logo-verde`, `--logo-blanco`) por si
alguna vez hace falta una versión monocromática.

El verde quedó unificado en `#7ED957`. El archivo original tenía dos verdes
distintos (`#80D766` en el logo, `#82E85A` en las piezas) por compresión; en el
sistema va uno solo.
