// Genera los íconos PNG del juego sin dependencias: rasteriza una pelota sobre césped.
import { deflateSync } from 'node:zlib';
import { writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const root = dirname(fileURLToPath(import.meta.url));
const outDir = resolve(root, '..', 'public', 'icons');
mkdirSync(outDir, { recursive: true });

const crc32Table = new Int32Array(256).map((_, n) => {
  let c = n;
  for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
  return c;
});
function crc32(buf) {
  let c = -1;
  for (const b of buf) c = crc32Table[(c ^ b) & 0xff] ^ (c >>> 8);
  return (c ^ -1) >>> 0;
}
function chunk(type, data) {
  const len = Buffer.alloc(4); len.writeUInt32BE(data.length);
  const td = Buffer.concat([Buffer.from(type, 'ascii'), data]);
  const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(td));
  return Buffer.concat([len, td, crc]);
}
function png(size, pixel) {
  const raw = Buffer.alloc((size * 4 + 1) * size);
  for (let y = 0; y < size; y++) {
    raw[y * (size * 4 + 1)] = 0;
    for (let x = 0; x < size; x++) {
      const [r, g, b, a] = pixel(x + 0.5, y + 0.5);
      const o = y * (size * 4 + 1) + 1 + x * 4;
      raw[o] = r; raw[o + 1] = g; raw[o + 2] = b; raw[o + 3] = a;
    }
  }
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(size, 0); ihdr.writeUInt32BE(size, 4);
  ihdr[8] = 8; ihdr[9] = 6; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  return Buffer.concat([
    Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]),
    chunk('IHDR', ihdr), chunk('IDAT', deflateSync(raw, { level: 9 })), chunk('IEND', Buffer.alloc(0)),
  ]);
}

function icon(size, rounded) {
  const c = size / 2;
  const R = size * 0.34;
  const patches = [[0, 0], [0.62, 0], [-0.62, 0], [0.19, 0.6], [-0.19, 0.6], [0.19, -0.6], [-0.19, -0.6]];
  return png(size, (x, y) => {
    const dx = x - c, dy = y - c;
    const corner = size * 0.2;
    // Fondo: césped a franjas, esquinas redondeadas si se pide.
    if (rounded) {
      const ax = Math.abs(dx) - (c - corner), ay = Math.abs(dy) - (c - corner);
      if (ax > 0 && ay > 0 && ax * ax + ay * ay > corner * corner) return [0, 0, 0, 0];
    }
    const stripe = Math.floor(x / (size / 6)) % 2 === 0;
    let col = stripe ? [46, 125, 50] : [56, 142, 60];
    // Línea blanca de área
    if (Math.abs(dy - size * 0.32) < size * 0.012 && Math.abs(dx) < size * 0.42) col = [235, 245, 236];
    const d = Math.hypot(dx, dy);
    if (d < R) {
      // Pelota con sombreado y parches oscuros.
      const shade = 1 - Math.max(0, (dx * 0.5 + dy * 0.7) / R) * 0.35;
      let ball = [250, 250, 250];
      for (const [px, py] of patches) {
        const pd = Math.hypot(dx / R - px, dy / R - py);
        if (pd < 0.22) { ball = [30, 30, 34]; break; }
      }
      col = ball.map((v) => Math.round(v * shade));
      if (d > R - size * 0.012) col = [20, 30, 22];
    } else if (d < R + size * 0.02) {
      col = [15, 40, 18];
    }
    return [col[0], col[1], col[2], 255];
  });
}

writeFileSync(resolve(outDir, 'icon-192.png'), icon(192, false));
writeFileSync(resolve(outDir, 'icon-512.png'), icon(512, false));
writeFileSync(resolve(outDir, 'apple-touch-icon.png'), icon(180, false));
console.log('íconos generados en', outDir);
