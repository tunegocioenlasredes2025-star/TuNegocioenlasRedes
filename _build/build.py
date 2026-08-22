# -*- coding: utf-8 -*-
"""
Build completo del sitio.

    python _build/build.py

Orden (importa):
  1. generate.py       genera landings, blog y 404
  2. seo_files.py      sitemap.xml + robots.txt a partir de los HTML reales
  3. llms_file.py      llms.txt para modelos de lenguaje
  4. version_assets.py estampa ?v=<hash> en css/js para que el cache largo sea seguro
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import generate
import seo_files
import llms_file
import version_assets


def main():
    print("== 1/4  Generando páginas ==")
    generate.main()

    print("\n== 2/4  sitemap.xml y robots.txt ==")
    seo_files.main()

    print("\n== 3/4  llms.txt ==")
    llms_file.main()

    print("\n== 4/4  Versionando assets ==")
    version_assets.main()

    print("\nBuild completo.")


if __name__ == "__main__":
    main()
