import Phaser from 'phaser';

export interface KitColors {
  base: number;
  accent: number;
  shorts: number;
  socks: number;
  /** 'plain' | 'stripes' | 'band' | 'halves' */
  pattern: 'plain' | 'stripes' | 'band' | 'halves';
  skin: number;
  hair: number;
}

export const FRAME_W = 48;
export const FRAME_H = 64;
/** Fila de píxel donde apoyan los pies dentro del frame. */
export const FOOT_Y = 58;
export const DIRS = 8;
export const RUN_FRAMES = 6;

export type Anim = 'idle' | 'run' | 'kick' | 'slide';
const ANIM_FRAMES: Record<Anim, number> = { idle: 1, run: RUN_FRAMES, kick: 2, slide: 1 };
const ANIM_ORDER: Anim[] = ['idle', 'run', 'kick', 'slide'];
const FRAMES_PER_DIR = ANIM_ORDER.reduce((n, a) => n + ANIM_FRAMES[a], 0);

export function frameName(key: string, dir: number, anim: Anim, i: number): string {
  return `${key}/${dir}/${anim}/${i}`;
}

/** Índice de dirección (0 = derecha, sentido horario en pantalla) a partir de un ángulo en radianes. */
export function dirIndex(angle: number): number {
  const a = ((angle % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
  return Math.round(a / (Math.PI / 4)) % DIRS;
}

const DIR_VEC: ReadonlyArray<readonly [number, number]> = Array.from({ length: DIRS }, (_, i) => {
  const a = (i * Math.PI) / 4;
  return [Math.cos(a), Math.sin(a)] as const;
});

/**
 * Genera un atlas con todas las poses de un jugador para un kit dado. Sin PNGs externos.
 * Vista 3/4 elevada: cuerpo erguido, piernas y brazos oscilan según la dirección.
 */
export function generatePlayerAtlas(scene: Phaser.Scene, key: string, kit: KitColors): void {
  if (scene.textures.exists(key)) return;
  const cols = FRAMES_PER_DIR;
  const tex = scene.textures.addDynamicTexture(key, FRAME_W * cols, FRAME_H * DIRS);
  if (!tex) throw new Error(`No se pudo crear la textura ${key}`);
  const g = scene.add.graphics();
  g.setVisible(false);

  for (let dir = 0; dir < DIRS; dir++) {
    let col = 0;
    for (const anim of ANIM_ORDER) {
      for (let i = 0; i < ANIM_FRAMES[anim]; i++) {
        g.clear();
        drawFigure(g, kit, dir, anim, i);
        tex.draw(g, col * FRAME_W, dir * FRAME_H);
        col++;
      }
    }
  }
  for (let dir = 0; dir < DIRS; dir++) {
    let col = 0;
    for (const anim of ANIM_ORDER) {
      for (let i = 0; i < ANIM_FRAMES[anim]; i++) {
        tex.add(frameName(key, dir, anim, i), 0, col * FRAME_W, dir * FRAME_H, FRAME_W, FRAME_H);
        col++;
      }
    }
  }
  g.destroy();
}

function drawFigure(g: Phaser.GameObjects.Graphics, kit: KitColors, dir: number, anim: Anim, i: number): void {
  const [dx, dy] = DIR_VEC[dir] ?? [1, 0];
  const px = -dy, py = dx; // perpendicular en pantalla
  const cx = FRAME_W / 2;
  const facingAway = dy < -0.3;     // mira hacia arriba (lejos de la cámara)
  const facingCam = dy > 0.3;

  // Fase de animación.
  let swing = 0;           // −1..1: pierna izquierda adelante / atrás
  let bob = 0;             // rebote vertical del cuerpo
  let kickExt = 0;         // extensión de la pierna de pateo
  let slide = false;
  if (anim === 'run') {
    const ph = (i / RUN_FRAMES) * Math.PI * 2;
    swing = Math.sin(ph);
    bob = Math.abs(Math.cos(ph)) * 1.5;
  } else if (anim === 'kick') {
    kickExt = i === 0 ? -0.6 : 1.0;
  } else if (anim === 'slide') {
    slide = true;
  }

  const hipY = FOOT_Y - 18 - bob;
  const legSep = 4;

  // Posición de cada pie en pantalla (la componente vertical del avance se comprime por la vista elevada).
  const footOf = (side: 1 | -1, adv: number): [number, number] => [
    cx + px * legSep * side + dx * adv * 7,
    FOOT_Y + py * legSep * side * 0.5 + dy * adv * 3.5,
  ];
  const leftFoot = footOf(1, slide ? 0.4 : kickExt !== 0 ? kickExt : swing);
  const rightFoot = footOf(-1, slide ? 1.4 : kickExt !== 0 ? -0.3 : -swing);

  const drawLeg = (foot: [number, number]): void => {
    const [fx, fy] = foot;
    const kneeX = (cx + fx) / 2, kneeY = (hipY + fy) / 2;
    g.lineStyle(6, kit.skin, 1);
    g.beginPath(); g.moveTo(cx, hipY); g.lineTo(kneeX, kneeY); g.strokePath();
    g.lineStyle(6, kit.socks, 1);
    g.beginPath(); g.moveTo(kneeX, kneeY); g.lineTo(fx, fy - 2); g.strokePath();
    g.fillStyle(0x151515, 1);
    g.fillEllipse(fx, fy, 8, 5);
  };

  // Orden: pierna lejana, cuerpo, pierna cercana.
  const legs: Array<[number, number]> = [leftFoot, rightFoot].sort((a, b) => a[1] - b[1]);
  const far = legs[0], near = legs[1];
  if (far) drawLeg(far);

  const bodyTop = hipY - 20 + (slide ? 6 : 0);
  const bodyW = 20, bodyH = 20;
  const bodyX = cx - bodyW / 2;
  // Shorts.
  g.fillStyle(kit.shorts, 1);
  g.fillRoundedRect(cx - 10, hipY - 6, 20, 9, 3);
  // Camiseta con patrón.
  g.fillStyle(kit.base, 1);
  g.fillRoundedRect(bodyX, bodyTop, bodyW, bodyH, 5);
  g.fillStyle(kit.accent, 1);
  if (kit.pattern === 'stripes') {
    for (let s = 0; s < 3; s++) g.fillRect(bodyX + 2 + s * 7, bodyTop + 1, 3, bodyH - 2);
  } else if (kit.pattern === 'band') {
    g.fillRect(bodyX, bodyTop + 7, bodyW, 6);
  } else if (kit.pattern === 'halves') {
    g.fillRoundedRect(bodyX, bodyTop, bodyW / 2, bodyH, { tl: 5, bl: 5, tr: 0, br: 0 });
  }
  // Cuello.
  g.fillStyle(kit.accent, 1);
  g.fillRect(cx - 4, bodyTop, 8, 2);

  // Brazos: oscilan opuestos a las piernas.
  const armSwing = -swing;
  const arm = (side: 1 | -1, adv: number): void => {
    const sx = cx + px * 11 * side, sy = bodyTop + 4;
    const ex = sx + px * 3 * side + dx * adv * 8, ey = sy + 14 + dy * adv * 3;
    g.lineStyle(5, kit.base, 1);
    g.beginPath(); g.moveTo(sx, sy); g.lineTo((sx + ex) / 2, (sy + ey) / 2); g.strokePath();
    g.lineStyle(5, kit.skin, 1);
    g.beginPath(); g.moveTo((sx + ex) / 2, (sy + ey) / 2); g.lineTo(ex, ey); g.strokePath();
  };
  arm(1, armSwing); arm(-1, -armSwing);

  if (near) drawLeg(near);

  // Cabeza.
  const headY = bodyTop - 6 + (slide ? 3 : 0);
  g.fillStyle(kit.skin, 1);
  g.fillCircle(cx, headY, 7.5);
  g.fillStyle(kit.hair, 1);
  if (facingAway) {
    g.fillCircle(cx, headY, 7.5);
  } else if (facingCam) {
    g.fillEllipse(cx, headY - 4.5, 15, 7);
    // Ojos.
    g.fillStyle(0x1a1a1a, 1);
    g.fillCircle(cx - 2.5 + dx * 1.5, headY + 0.5, 1.2);
    g.fillCircle(cx + 2.5 + dx * 1.5, headY + 0.5, 1.2);
  } else {
    // Perfil: pelo cubre la mitad trasera.
    g.fillEllipse(cx - dx * 2.5, headY - 3, 13, 9);
    g.fillStyle(0x1a1a1a, 1);
    g.fillCircle(cx + dx * 4, headY + 0.5, 1.2);
  }
}
