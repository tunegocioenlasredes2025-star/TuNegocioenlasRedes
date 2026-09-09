const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file:///home/user/TuNegocioenlasRedes/Secure%20Growing/carruseles/carrusel-03-cuanto-vale-un-abonado.html');
  await p.evaluate(() => document.fonts.ready); await p.emulateMedia({ media: 'print' });
  const els = await p.$$('.slide'); await els[3].screenshot({ path: process.argv[2] + '/print-c03-04.png' });
  await p.goto('file:///home/user/TuNegocioenlasRedes/Secure%20Growing/carruseles/carrusel-01-vendedor-sentado.html');
  await p.evaluate(() => document.fonts.ready); await p.emulateMedia({ media: 'screen' });
  const e2 = await p.$$('.slide'); await e2[0].screenshot({ path: process.argv[2] + '/screen-c01-01.png' });
  await b.close();
})();
