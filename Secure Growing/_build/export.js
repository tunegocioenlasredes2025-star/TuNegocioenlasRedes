// Exporta cada pieza a PDF vectorial (una página por slide) y PNG @2x por slide.
// Uso: node export.js [filtro]
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const filtro = process.argv[2] || '';
(async () => {
  const b = await chromium.launch();
  const informe = [];
  for (const dir of ['carruseles', 'estaticas']) {
    const files = fs.readdirSync(path.join(ROOT, dir)).filter(f => f.endsWith('.html') && f.includes(filtro));
    for (const f of files) {
      const base = f.replace(/\.html$/, '');
      const url = 'file://' + path.join(ROOT, dir, f);
      const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
      await p.goto(url); await p.evaluate(() => document.fonts.ready);
      // --- chequeo de desbordes y zona segura (media screen)
      const qa = await p.evaluate(() => {
        const out = [];
        document.querySelectorAll('.slide').forEach((s, i) => {
          const r = s.getBoundingClientRect();
          const items = s.querySelectorAll('*');
          let maxBottom = 0, maxRight = 0, minTop = 1e9;
          items.forEach(el => {
            if (el.closest('.firma') || el.closest('.pag') || el.closest('.marca')) return;
            const e = el.getBoundingClientRect(); if (e.width === 0 || e.height === 0) return;
            maxBottom = Math.max(maxBottom, e.bottom - r.top); maxRight = Math.max(maxRight, e.right - r.left);
          });
          const firma = s.querySelector('.firma').getBoundingClientRect();
          const contenido = [...s.children].filter(c => !c.classList.contains('firma') && !c.classList.contains('pag'));
          let contBottom = 0; contenido.forEach(c => { const e = c.getBoundingClientRect(); contBottom = Math.max(contBottom, e.bottom - r.top); });
          out.push({ slide: i + 1, scrollH: s.scrollHeight, contBottom: Math.round(contBottom), firmaTop: Math.round(firma.top - r.top),
                     maxRight: Math.round(maxRight), overflow: s.scrollHeight > 1350 || maxRight > 1080 - 64 || contBottom > (firma.top - r.top) - 24 });
        });
        return out;
      });
      // --- PNG @2x por slide
      const outDir = path.join(ROOT, dir, base); fs.mkdirSync(outDir, { recursive: true });
      const n = qa.length;
      for (let i = 0; i < n; i++) {
        const el = (await p.$$('.slide'))[i];
        await el.screenshot({ path: path.join(outDir, String(i + 1).padStart(2, '0') + '.png') });
      }
      // --- PDF vectorial
      await p.emulateMedia({ media: 'print' });
      await p.pdf({ path: path.join(ROOT, dir, base + '.pdf'), printBackground: true, preferCSSPageSize: true });
      await p.close();
      informe.push({ pieza: dir + '/' + base, slides: n, qa });
      console.log(dir + '/' + base, n, 'slides', qa.some(q => q.overflow) ? 'DESBORDE: ' + JSON.stringify(qa.filter(q => q.overflow)) : 'ok');
    }
  }
  fs.writeFileSync(path.join(__dirname, 'qa-layout.json'), JSON.stringify(informe, null, 1));
  await b.close();
})();
