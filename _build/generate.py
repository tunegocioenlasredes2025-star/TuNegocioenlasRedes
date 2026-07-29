# -*- coding: utf-8 -*-
"""
Genera las landings de servicio, las locales y el blog.

Uso:  python _build/generate.py

Escribe archivos .html en la raíz del proyecto (y en blog/). Las URLs quedan
limpias gracias a "cleanUrls": true en vercel.json, así que /paginas-web.html
se sirve como /paginas-web.
"""

import os
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import pages_servicios
import pages_local
import pages_blog
import pages_misc


def write(path, html):
    """path: ruta limpia tipo '/paginas-web' o '/blog/slug'."""
    rel = path.lstrip("/") or "index"
    target = ROOT / (rel + ".html")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    return target, len(html)


def main():
    builders = []
    builders += [(f, "servicio") for f in pages_servicios.ALL]
    builders += [(f, "local") for f in pages_local.ALL]
    builders += [(f, "blog") for f in pages_blog.ALL]
    builders += [(f, "misc") for f in pages_misc.ALL]

    written = []
    for build, kind in builders:
        path, html = build()
        target, size = write(path, html)
        written.append((kind, path, target.relative_to(ROOT).as_posix(), size))

    w = max(len(p) for _, p, _, _ in written)
    for kind, path, rel, size in written:
        print(f"  {kind:9} {path:<{w}}  ->  {rel:<34} {size/1024:6.1f} KB")
    print(f"\n{len(written)} páginas generadas.")
    return [p for _, p, _, _ in written]


if __name__ == "__main__":
    main()
