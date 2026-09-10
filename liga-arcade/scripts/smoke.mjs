// Test de humo: sirve la build, la abre en Chromium con viewport de iPhone, juega unos segundos y mide.
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { resolve, dirname, extname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, devices } from 'playwright';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..');
const outDir = process.env.SMOKE_OUT ?? resolve(root, 'liga-arcade', 'smoke-out');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.png': 'image/png', '.css': 'text/css' };

const server = createServer(async (req, res) => {
  try {
    let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    if (p.endsWith('/')) p += 'index.html';
    const file = join(root, p);
    const st = await stat(file);
    if (!st.isFile()) throw new Error('dir');
    res.writeHead(200, { 'content-type': MIME[extname(file)] ?? 'application/octet-stream' });
    res.end(await readFile(file));
  } catch {
    res.writeHead(404); res.end('not found');
  }
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const port = server.address().port;

const iphone = devices['iPhone 13 landscape'];
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const ctx = await browser.newContext({ ...iphone, viewport: { width: 844, height: 390 }, deviceScaleFactor: 2, hasTouch: true, isMobile: true });
const page = await ctx.newPage();
const errors = [];
page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
page.on('pageerror', (e) => errors.push(String(e)));

const t0 = Date.now();
await page.goto(`http://127.0.0.1:${port}/juego/?stats`, { waitUntil: 'load' });
await page.waitForSelector('#boot', { state: 'detached', timeout: 15000 });
const bootMs = Date.now() - t0;
await page.waitForTimeout(600);
await page.screenshot({ path: join(outDir, '01-inicio.png') });

// Toque para medir latencia: tap en botón de TIRO sin pelota (no hace nada, pero mide).
const cdp = await ctx.newCDPSession(page);
async function touch(id, type, x, y) {
  await cdp.send('Input.dispatchTouchEvent', { type, touchPoints: type === 'touchEnd' ? [] : [{ x, y, id }] });
}
// Joystick: apoyar a la izquierda y arrastrar hacia la derecha para ir a buscar la pelota.
await touch(1, 'touchStart', 160, 250);
for (let i = 1; i <= 8; i++) { await touch(1, 'touchMove', 160 + i * 10, 250); await page.waitForTimeout(16); }
await page.waitForTimeout(900);
await page.screenshot({ path: join(outDir, '02-corriendo.png') });
// Mantener TIRO 0.5 s y soltar con el joystick apuntando a la derecha.
await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: 240, y: 250, id: 1 }, { x: 844 - 64, y: 390 - 64, id: 2 }] });
await page.waitForTimeout(500);
await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [{ x: 240, y: 250, id: 1 }] });
await page.waitForTimeout(120);
await page.screenshot({ path: join(outDir, '03-tiro.png') });
await touch(1, 'touchEnd', 0, 0);

// Medir FPS durante 3 s mientras la pelota viaja.
const fpsSample = await page.evaluate(() => new Promise((res) => {
  let n = 0; const start = performance.now();
  const loop = () => { n++; if (performance.now() - start < 3000) requestAnimationFrame(loop); else res(n / ((performance.now() - start) / 1000)); };
  requestAnimationFrame(loop);
}));
await page.screenshot({ path: join(outDir, '04-final.png') });
const overlayText = await page.evaluate(() => document.querySelector('canvas') ? 'canvas ok' : 'sin canvas');

await browser.close();
server.close();

const report = { bootMs, fps: Math.round(fpsSample), overlayText, errors, viewport: '844x390@2x (iPhone 13 landscape)' };
console.log(JSON.stringify(report, null, 2));
if (errors.length > 0) { process.exitCode = 1; }
