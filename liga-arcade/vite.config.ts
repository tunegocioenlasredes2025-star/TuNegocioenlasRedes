import { defineConfig, type Plugin } from 'vite';
import { fileURLToPath } from 'node:url';
import { resolve, dirname } from 'node:path';

const root = dirname(fileURLToPath(import.meta.url));

/**
 * Salida: `/juego/` en la raíz del repo, servido por Vercel junto al sitio.
 * `BASE_PATH=/` genera una build relativa para Capacitor (www/).
 */
const basePath = process.env['BASE_PATH'] ?? '/juego/';
const outDir = process.env['OUT_DIR'] ?? resolve(root, '..', 'juego');

/** Emite sw.js con la lista exacta de archivos generados para precache offline. */
function serviceWorkerPlugin(): Plugin {
  return {
    name: 'liga-arcade-sw',
    apply: 'build',
    generateBundle(_opts, bundle) {
      // Documento principal sin barra final (Vercel redirige /juego/ → /juego); en raíz queda '/'.
      const doc = basePath.length > 1 ? basePath.replace(/\/$/, '') : basePath;
      const files = Object.keys(bundle).filter((f) => f !== 'index.html' && f !== 'sw.js').map((f) => basePath + f);
      files.push(doc, basePath + 'manifest.webmanifest');
      const version = Date.now().toString(36);
      const sw = `/* Liga Arcade service worker — generado en build */
const CACHE = 'liga-arcade-${version}';
const DOC = ${JSON.stringify(doc)};
const BASE = ${JSON.stringify(basePath)};
const ASSETS = ${JSON.stringify(files)};
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
function isGamePath(p) { return p === DOC || p === BASE || p.startsWith(BASE); }
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== self.location.origin || !isGamePath(url.pathname)) return;
  if (e.request.mode === 'navigate') {
    e.respondWith(fetch(e.request).then((res) => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(DOC, copy)); }
      return res;
    }).catch(() => caches.match(DOC)));
    return;
  }
  e.respondWith(caches.match(e.request, { ignoreSearch: true }).then((hit) => hit ?? fetch(e.request).then((res) => {
    if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(e.request, copy)); }
    return res;
  })));
});
`;
      this.emitFile({ type: 'asset', fileName: 'sw.js', source: sw });
    },
  };
}

export default defineConfig({
  base: basePath,
  plugins: [serviceWorkerPlugin()],
  resolve: {
    alias: {
      '@core': resolve(root, 'src/core'),
      '@game': resolve(root, 'src/game'),
      '@platform': resolve(root, 'src/platform'),
      '@data': resolve(root, 'data'),
    },
  },
  build: {
    outDir,
    emptyOutDir: true,
    target: 'es2020',
    sourcemap: false,
    assetsInlineLimit: 0,
    chunkSizeWarningLimit: 1600,
    rollupOptions: {
      output: {
        manualChunks: { phaser: ['phaser'] },
      },
    },
  },
  server: { host: true, port: 5173 },
});
