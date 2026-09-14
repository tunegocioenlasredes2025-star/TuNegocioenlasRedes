/* Liga Arcade service worker — generado en build */
const CACHE = 'liga-arcade-mtuyyk7p';
const DOC = "/juego";
const BASE = "/juego/";
const ASSETS = ["/juego/assets/phaser-DXXWZowi.js","/juego/assets/index-YerymNB1.js","/juego","/juego/manifest.webmanifest"];
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
