import os, sys, glob
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
W = 540; H = 675
for d in sorted(glob.glob(os.path.join(ROOT, 'carruseles', 'carrusel-*/')) + glob.glob(os.path.join(ROOT, 'estaticas', 'estatica-*/'))):
    pngs = sorted(glob.glob(os.path.join(d, '*.png')))
    cols = 4 if len(pngs) > 1 else 1; rows = (len(pngs) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * W + (cols + 1) * 10, rows * H + (rows + 1) * 10), (40, 40, 40))
    for i, p in enumerate(pngs):
        im = Image.open(p).convert('RGB').resize((W, H), Image.LANCZOS)
        sheet.paste(im, (10 + (i % cols) * (W + 10), 10 + (i // cols) * (H + 10)))
    name = os.path.basename(os.path.dirname(d + '/'))
    sheet.save(os.path.join(OUT, name + '.png'))
    print(name, len(pngs))
