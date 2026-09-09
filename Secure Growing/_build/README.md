# _build — cómo regenerar las piezas

Todo sale de `../tokens.css` (valores) + `base.css` (reglas) + `build.py` (copy y estructura).

```
python3 build.py        # escribe los HTML en ../carruseles y ../estaticas
node export.js          # PDF vectorial (una página por slide) + PNG @2x por slide + chequeo de desbordes
python3 verify.py       # texto extraíble y fuentes TrueType (nunca Type3) en cada PDF
python3 sheet.py DIR    # hojas de contacto para revisar
```

Requiere Playwright (Chromium) en Node y `pypdf` + `Pillow` en Python.
Los PDF usan las instancias estáticas TTF de `../fonts/`: si se cambia una fuente, volver a
instanciarla con fontTools, porque Chromium embebe las fuentes variables como Type3 (curvas).
