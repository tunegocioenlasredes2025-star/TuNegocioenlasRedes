# Estáticas de Instagram — InfoSeguridadAR

Generador de piezas 1080×1350 para el feed de [@infoseguridadar](https://www.instagram.com/infoseguridadar/),
con el mismo sistema visual de las publicaciones actuales. Ver `sistema-visual.md`.

## Cómo generar

```bash
cd estaticas/infoseguridadar
pip install playwright pillow
PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 generar.py
```

Salida en `out/`: un `.html` autónomo (fuentes y foto embebidas, abre sin internet)
y un `.png` de 2160×2700 por nota.

`python3 generar.py --solo-html` arma los HTML sin abrir el navegador.

## Cómo cargar una nota

Agregá una entrada en `notas.json`:

```json
{
  "categoria": "Instaladores",
  "etiqueta": "Nota nueva",
  "titular": "Certificarse ya no es un *extra*.",
  "bajada": "Aliara lanza capacitación oficial en Power Shock Lite, exclusiva para instaladores.",
  "marca_agua": "Capacitación",
  "foto": "02-aliara.jpg",
  "url": "https://infoseguridadit.com/..."
}
```

- `*palabra*` → esa palabra sale en verde. Usá **una sola** por titular.
- `foto` → nombre del archivo dentro de `fotos/`. Ideal horizontal, 1600 px de ancho o más.
- Si la foto no existe, la pieza usa una **portada tipográfica** de respaldo (fondo negro con
  degradado verde, grilla y la palabra de `marca_agua` calada). Sirve para maquetar, pero la
  foto de la nota siempre rinde más.

## Logo

Ahora mismo el logo está **reconstruido con CSS** (aproximación). Dejá el original como
`logo.png` (fondo transparente, 400 px de alto o más) en esta carpeta y el generador lo usa
automáticamente en lugar de la reconstrucción.
