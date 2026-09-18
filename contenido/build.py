#!/usr/bin/env python3
"""Render de los carruseles de TNR: PNG 2x para publicar + PDF editable para Canva.

Dos decisiones que costaron encontrar y conviene no tocar:

1. Las fuentes que se embeben son las instancias ESTATICAS de
   contenido/fuentes-para-canva/, no las variables que usa la web. Chromium no
   puede meter una fuente variable adentro de un PDF: la reemplaza en silencio
   por la del sistema y el archivo llega a Canva con otra tipografia.

2. El PDF se imprime slide por slide y despues se unen las paginas. Imprimiendo
   todo de una, Chromium agrega una pagina en blanco antes de la primera y otra
   despues de la ultima.

Uso:  python3 contenido/build.py contenido/carruseles/<carpeta>
"""
import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

FACES = [('Bricolage Grotesque', 800, 'BricolageGrotesque-ExtraBold.woff2'),
         ('Figtree', 400, 'Figtree-Regular.woff2'),
         ('Figtree', 700, 'Figtree-Bold.woff2')]


def b64(rel):
    return base64.b64encode((ROOT / rel).read_bytes()).decode()


def fonts_css():
    """Las tres caras de la marca, embebidas. El HTML abre sin internet."""
    return "\n".join(
        "@font-face{font-family:'%s';font-style:normal;font-weight:%d;"
        "src:url(data:font/woff2;base64,%s) format('woff2');}"
        % (fam, weight, b64('contenido/fuentes-para-canva/' + f))
        for fam, weight, f in FACES)


def img(rel, mime):
    return "data:%s;base64,%s" % (mime, b64(rel))


# Un titular con <br> a mano se puede partir igual si la linea no entra a lo
# ancho, y eso arruina el ritmo del slide sin que salte a la vista. Esto compara
# los renglones que se dibujaron contra los que pide el copy.
CHEQUEO_DE_LINEAS = """
() => {
  const avisos = [];
  document.querySelectorAll('.slide').forEach((sl, i) => {
    sl.querySelectorAll('h1').forEach(h => {
      const pedidas = h.innerHTML.split(/<br\\s*\\/?>/i).length;
      // por altura y no con getClientRects(): un <span class="mark"> adentro del
      // titular parte el rango en varios rects dentro del mismo renglon
      const lh = parseFloat(getComputedStyle(h).lineHeight);
      const reales = Math.round(h.getBoundingClientRect().height / lh);
      if (reales > pedidas) avisos.push({slide: i + 1, pedidas, reales,
        texto: h.textContent.trim().slice(0, 52)});
    });
  });
  return avisos;
}
"""


def render(folder):
    from playwright.sync_api import sync_playwright
    from pypdf import PdfReader, PdfWriter

    d = pathlib.Path(folder).resolve()
    out = d / 'png'
    out.mkdir(exist_ok=True)
    pdf_pages = []

    with sync_playwright() as p:
        exe = CHROME if pathlib.Path(CHROME).exists() else None
        b = p.chromium.launch(executable_path=exe,
                              args=['--no-sandbox', '--font-render-hinting=none'])
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto((d / 'index.html').as_uri())
        pg.wait_for_timeout(1200)

        avisos = pg.evaluate(CHEQUEO_DE_LINEAS)
        for a in avisos:
            print('  ! slide %(slide)s: el titular se corta en %(reales)s lineas y el copy '
                  'pide %(pedidas)s -> %(texto)s' % a)

        slides = pg.query_selector_all('.slide')
        for i, s in enumerate(slides, 1):
            s.screenshot(path=str(out / ('slide-%02d.png' % i)))

        for i in range(len(slides)):
            pg.eval_on_selector_all(
                '.slide',
                '(els, k) => els.forEach((e, j) => e.style.display = j === k ? "flex" : "none")', i)
            tmp = d / ('_p%02d.pdf' % i)
            pg.pdf(path=str(tmp), width='1080px', height='1350px', print_background=True,
                   margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'})
            pdf_pages.append(tmp)
        b.close()

    w = PdfWriter()
    for f in pdf_pages:
        w.append(str(f))
        f.unlink()
    w.write(str(d / 'editable-canva.pdf'))
    w.close()

    n = len(PdfReader(str(d / 'editable-canva.pdf')).pages)
    print('paginas del PDF:', n)
    assert n == len(slides), 'el PDF quedo con %d paginas para %d slides' % (n, len(slides))

    hoja_de_contacto(out)
    print('%d slides -> %s' % (len(slides), out))


def hoja_de_contacto(out):
    """Todas las slides en una imagen, para revisar el ritmo de un vistazo."""
    from PIL import Image
    fs = sorted(out.glob('slide-*.png'))
    ims = [Image.open(f).resize((520, 650)) for f in fs]
    cols = min(len(ims), 4)
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (520 * cols, 650 * rows), 'white')
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * 520, (i // cols) * 650))
    sheet.save(out / 'contacto.png')


if __name__ == '__main__':
    render(sys.argv[1])
