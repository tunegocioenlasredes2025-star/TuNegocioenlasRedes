import Phaser from 'phaser';
import { PITCH, CENTER_X, CENTER_Y } from '@core/pitch/Pitch';
import { projectX, projectY, projectedBounds } from './Projection';

const GRASS_A = 0x3f9a4a;
const GRASS_B = 0x35893f;
const GRASS_OUT = 0x2f7a39;
const LINE = 0xf2f7f2;
/** Césped exterior dibujado más allá del margen jugable, para que la cámara nunca muestre el fondo. */
const OUTER_X = 34;
const OUTER_Y = 16;

/**
 * Dibuja la cancha proyectada una sola vez en una RenderTexture: césped a franjas, líneas
 * y marcas. Después es una imagen estática = un draw call.
 */
export function createPitch(scene: Phaser.Scene): Phaser.GameObjects.Image {
  const b = projectedBounds();
  const g = scene.add.graphics();
  g.setVisible(false);

  const pt = (x: number, y: number): Phaser.Math.Vector2 => new Phaser.Math.Vector2(projectX(x, y) - b.x, projectY(y) - b.y);
  const quad = (x0: number, x1: number, y0: number, y1: number): Phaser.Math.Vector2[] => [pt(x0, y0), pt(x1, y0), pt(x1, y1), pt(x0, y1)];

  // Fondo exterior.
  g.fillStyle(GRASS_OUT, 1);
  g.fillPoints(quad(-OUTER_X, PITCH.LENGTH + OUTER_X, -OUTER_Y, PITCH.WIDTH + OUTER_Y), true);

  // Franjas de césped (a lo ancho de la cancha, como cortadas por la cortadora).
  const stripes = 14;
  const sw = PITCH.LENGTH / stripes;
  for (let i = 0; i < stripes; i++) {
    g.fillStyle(i % 2 === 0 ? GRASS_A : GRASS_B, 1);
    g.fillPoints(quad(i * sw, (i + 1) * sw, 0, PITCH.WIDTH), true);
  }

  // Líneas.
  const lineWidth = 3;
  g.lineStyle(lineWidth, LINE, 0.95);
  const poly = (pts: Phaser.Math.Vector2[], close: boolean): void => {
    g.beginPath();
    const first = pts[0];
    if (!first) return;
    g.moveTo(first.x, first.y);
    for (let i = 1; i < pts.length; i++) { const p = pts[i]; if (p) g.lineTo(p.x, p.y); }
    if (close) g.closePath();
    g.strokePath();
  };
  const rect = (x0: number, x1: number, y0: number, y1: number): void => poly(quad(x0, x1, y0, y1), true);
  const arc = (cx: number, cy: number, r: number, a0: number, a1: number, steps = 40): Phaser.Math.Vector2[] => {
    const out: Phaser.Math.Vector2[] = [];
    for (let i = 0; i <= steps; i++) {
      const a = a0 + ((a1 - a0) * i) / steps;
      out.push(pt(cx + Math.cos(a) * r, cy + Math.sin(a) * r));
    }
    return out;
  };

  rect(0, PITCH.LENGTH, 0, PITCH.WIDTH);
  poly([pt(CENTER_X, 0), pt(CENTER_X, PITCH.WIDTH)], false);
  poly(arc(CENTER_X, CENTER_Y, PITCH.CENTER_CIRCLE_RADIUS, 0, Math.PI * 2, 64), true);

  const paHalf = PITCH.PENALTY_AREA_WIDTH / 2;
  const gaHalf = PITCH.GOAL_AREA_WIDTH / 2;
  for (const side of [0, 1] as const) {
    const x0 = side === 0 ? 0 : PITCH.LENGTH;
    const dir = side === 0 ? 1 : -1;
    rect(x0, x0 + dir * PITCH.PENALTY_AREA_LENGTH, CENTER_Y - paHalf, CENTER_Y + paHalf);
    rect(x0, x0 + dir * PITCH.GOAL_AREA_LENGTH, CENTER_Y - gaHalf, CENTER_Y + gaHalf);
    // Semicírculo del área (la "D").
    const spotX = x0 + dir * PITCH.PENALTY_SPOT;
    const edgeX = x0 + dir * PITCH.PENALTY_AREA_LENGTH;
    const cosA = (edgeX - spotX) / PITCH.CENTER_CIRCLE_RADIUS;
    const half = Math.acos(Math.max(-1, Math.min(1, cosA)));
    const base = side === 0 ? 0 : Math.PI;
    poly(arc(spotX, CENTER_Y, PITCH.CENTER_CIRCLE_RADIUS, base - half, base + half, 24), false);
    // Punto penal y centro.
    g.fillStyle(LINE, 0.95);
    const sp = pt(spotX, CENTER_Y);
    g.fillCircle(sp.x, sp.y, lineWidth);
    // Arcos de córner.
    for (const cy of [0, PITCH.WIDTH]) {
      const a0 = side === 0 ? (cy === 0 ? 0 : -Math.PI / 2) : (cy === 0 ? Math.PI / 2 : Math.PI);
      poly(arc(x0, cy, PITCH.CORNER_RADIUS, a0, a0 + Math.PI / 2, 8), false);
    }
  }
  const c = pt(CENTER_X, CENTER_Y);
  g.fillCircle(c.x, c.y, lineWidth);

  const tex = scene.textures.addDynamicTexture('pitch', Math.ceil(b.width), Math.ceil(b.height));
  if (!tex) throw new Error('No se pudo crear la textura de la cancha');
  tex.draw(g, 0, 0);
  g.destroy();

  const img = scene.add.image(b.x, b.y, 'pitch').setOrigin(0, 0);
  img.setDepth(-1000);
  return img;
}
