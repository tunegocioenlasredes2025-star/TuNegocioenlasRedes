# Sistema visual — InfoSeguridadAR (estáticas de Instagram)

Reconstruido a partir de las piezas publicadas en [@infoseguridadar](https://www.instagram.com/infoseguridadar/).
Todo lo de acá abajo está implementado en `generar.py`; para cambiar algo, tocá un solo lugar.

## Formato
- Lienzo **1080 × 1350** (4:5, el formato que más pantalla ocupa en el feed).
- Exporta a **2160 × 2700** (retina 2x). Instagram lo baja a 1440 sin artefactos.
- Márgenes: 56 px laterales, 52 arriba, 44 abajo.

## Paleta
| Token | Hex | Uso |
|---|---|---|
| `--negro` | `#000000` | Fondo. Negro puro, no gris. Es lo que hace que el verde pegue. |
| `--verde` | `#2BE06B` | Chip de categoría, palabra destacada del titular, línea, CTA, "AR" del logo. |
| `--blanco` | `#FFFFFF` | Titular y "NOTA NUEVA". |
| `--gris` | `#B6BDC1` | Bajada. Nunca blanco puro: si compite con el titular, se rompe la jerarquía. |
| `--gris-tenue` | `#6E7679` | `infoseguridadit.com` del pie. |

**Regla del verde:** una sola palabra verde por titular. Dos ya es ruido.

## Tipografía
Familia única: **Archivo** (variable, ejes `wght` 100–900 y `wdth` 62–125), embebida en base64.
Es una grotesca de noticiero: neutra, muy pesada en los extremos, levemente angosta. Misma
familia para todo = consistencia sin esfuerzo.

| Elemento | Peso / ancho | Tamaño | Interlínea |
|---|---|---|---|
| Chip categoría | 800 | 23 px, `+5.5%` tracking, mayúsculas | 1 |
| "NOTA NUEVA" | 700 | 23 px, `+7.5%` tracking, mayúsculas | 1 |
| Titular | **900 / ancho 92%** | 88 px (se autoajusta hasta 54) | 0.95 |
| Bajada | 400 | 30 px | 1.33 |
| CTA | 600 | 29 px | 1 |
| Sitio | 400 | 22 px | 1 |

El titular va **siempre alineado a la izquierda**, en caja baja (no mayúsculas) y **termina en punto**.
El punto final es lo que le da tono de afirmación y no de título de nota.

## Anatomía de la pieza (de arriba hacia abajo)
1. `CATEGORÍA` en chip verde + separador + `NOTA NUEVA`
2. Foto a todo el ancho, esquinas de 16 px
3. Titular
4. Bajada (máx. 2 líneas)
5. Aire
6. Logo alineado a la derecha
7. Línea verde de 2 px a todo el ancho
8. `⟶ Nota completa en el link de la bio` (verde, izquierda) · `infoseguridadit.com` (gris, derecha)

El ajuste es automático: si el titular es largo, achica; si sobra aire, la foto crece. Nunca desborda.

## Voz del titular
Fórmula: **afirmación corta + tensión + punto final.**
- 4 a 9 palabras. Si no entra en dos líneas, es muy largo.
- Dice una postura, no describe la nota. La nota se explica en la bajada.
- Nada de signos de exclamación ni emojis en la pieza.

Bajada: **quién + qué aporta**, en una oración. Casi siempre arranca con la marca o la fuente
("ONVIF presentó…", "Big Dipper analiza cómo…", "Walter R. Smith, CEO de EZER, explica…").
