# Verifica cada PDF: páginas, tamaño, texto extraíble y fuentes (nunca Type3).
import os, sys, glob, pypdf
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ok_all = True
for pdf in sorted(glob.glob(os.path.join(ROOT, '*', '*.pdf'))):
    r = pypdf.PdfReader(pdf)
    fonts, chars, bad = set(), 0, []
    for i, pg in enumerate(r.pages):
        t = pg.extract_text() or ''
        chars += len(t.strip())
        if len(t.strip()) < 20: bad.append(f'p{i+1}: texto vacío')
        w, h = float(pg.mediabox.width), float(pg.mediabox.height)
        if abs(w - 810) > 1 or abs(h - 1012.5) > 1.5: bad.append(f'p{i+1}: tamaño {w}x{h}pt')
        def walk(res, depth=0):
            if not res or depth > 3: return
            for k, v in (res.get('/Font') or {}).items():
                f = v.get_object(); st = f.get('/Subtype'); d = f.get('/DescendantFonts')
                fonts.add((str(f.get('/BaseFont')), str(st), str(d[0].get_object().get('/Subtype')) if d else ''))
                if st == '/Type3': bad.append(f'p{i+1}: fuente Type3 (curvas)')
            for k, v in (res.get('/XObject') or {}).items():
                x = v.get_object()
                if x.get('/Subtype') == '/Form': walk(x.get('/Resources'), depth + 1)
        walk(pg.get('/Resources'))
    fam = sorted({f[0].split('+')[-1] for f in fonts})
    status = 'OK' if not bad else 'FALLA ' + '; '.join(bad)
    ok_all &= not bad
    print(f'{os.path.relpath(pdf, ROOT)}: {len(r.pages)} pág, {chars} chars, fuentes {fam} -> {status}')
sys.exit(0 if ok_all else 1)
