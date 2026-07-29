# -*- coding: utf-8 -*-
"""
Genera sitemap.xml y robots.txt a partir de los .html que existen de verdad.

Uso:  python _build/seo_files.py

Así el sitemap no se desincroniza cuando se agrega o se borra una página.
"""

import pathlib
import datetime
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from chrome import SITE

TODAY = datetime.date.today().isoformat()

# ruta -> (prioridad, frecuencia)
PRIORITY = {
    "/":                              ("1.0", "weekly"),
    "/servicios":                     ("0.9", "monthly"),
    "/paginas-web":                   ("0.9", "monthly"),
    "/ia":                            ("0.9", "monthly"),
    "/marketing-digital-zona-oeste":  ("0.9", "monthly"),
    "/tiendas-online":                ("0.8", "monthly"),
    "/gestion-de-redes":              ("0.8", "monthly"),
    "/publicidad-digital":            ("0.8", "monthly"),
    "/automatizacion-whatsapp":       ("0.8", "monthly"),
    "/crm-para-pymes":                ("0.8", "monthly"),
    "/marketing-digital-ituzaingo":   ("0.8", "monthly"),
    "/marketing-digital-moron":       ("0.8", "monthly"),
    "/marketing-digital-castelar":    ("0.8", "monthly"),
    "/trabajos":                      ("0.8", "monthly"),
    "/contacto":                      ("0.7", "yearly"),
    "/blog":                          ("0.7", "weekly"),
    "/nosotros":                      ("0.6", "yearly"),
}
DEFAULT = ("0.7", "monthly")

# No entran al sitemap
EXCLUDE = {"/404"}


def discover():
    paths = []
    for f in sorted(ROOT.glob("*.html")) + sorted((ROOT / "blog").glob("*.html")):
        rel = f.relative_to(ROOT).as_posix()[:-5]
        path = "/" if rel == "index" else "/" + rel
        if path in EXCLUDE:
            continue
        paths.append(path)
    # ordenar por prioridad descendente, después alfabético
    return sorted(paths, key=lambda p: (-float(PRIORITY.get(p, DEFAULT)[0]), p))


def build_sitemap(paths):
    urls = []
    for p in paths:
        prio, freq = PRIORITY.get(p, DEFAULT)
        urls.append(
            "  <url>\n"
            f"    <loc>{SITE}{p}</loc>\n"
            f"    <lastmod>{TODAY}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n"
            f"    <priority>{prio}</priority>\n"
            "  </url>"
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(urls) + "\n</urlset>\n")


ROBOTS = f"""# robots.txt - Tu Negocio En Las Redes
# https://www.tunegocioenlasredes.com.ar

User-agent: *
Allow: /

# Sin trampas para el crawler: todo el sitio es indexable.
# Los archivos de build no se publican (ver .vercelignore).

Sitemap: {SITE}/sitemap.xml
"""


def main():
    paths = discover()
    (ROOT / "sitemap.xml").write_text(build_sitemap(paths), encoding="utf-8")
    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    print(f"sitemap.xml -> {len(paths)} URLs")
    for p in paths:
        prio = PRIORITY.get(p, DEFAULT)[0]
        print(f"  {prio}  {p}")
    print("robots.txt  -> ok")


if __name__ == "__main__":
    main()
