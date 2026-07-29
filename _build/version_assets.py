# -*- coding: utf-8 -*-
"""
Estampa ?v=<hash> en los links a styles.css, fonts.css y main.js de todos los HTML.

Por qué: vercel.json cachea los assets un año como `immutable`. Sin un
identificador que cambie con el contenido, un visitante que ya estuvo en el
sitio seguiría viendo el CSS viejo durante meses después de cada cambio.
Con el hash del archivo en la URL, el cache largo es correcto y seguro.

Se ejecuta al final del build (ver build.py).
"""

import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

ASSETS = ["styles.css", "fonts.css", "main.js"]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8]


def main():
    versions = {}
    for a in ASSETS:
        f = ROOT / a
        if not f.exists():
            print(f"  aviso: falta {a}, se omite")
            continue
        versions[a] = digest(f)

    if not versions:
        return 1

    pattern = re.compile(
        r'(?P<attr>href|src)="/(?P<asset>' + "|".join(re.escape(a) for a in versions) + r')(?:\?v=[a-f0-9]+)?"'
    )

    def sub(m):
        a = m.group("asset")
        return f'{m.group("attr")}="/{a}?v={versions[a]}"'

    files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "blog").glob("*.html"))
    touched = 0
    for f in files:
        t = f.read_text(encoding="utf-8")
        new, n = pattern.subn(sub, t)
        if new != t:
            f.write_text(new, encoding="utf-8")
            touched += 1

    for a, v in versions.items():
        print(f"  {a:12} -> ?v={v}")
    print(f"  {touched}/{len(files)} HTML actualizados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
