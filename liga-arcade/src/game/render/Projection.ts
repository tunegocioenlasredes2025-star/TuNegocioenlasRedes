import { PITCH, CENTER_X } from '@core/pitch/Pitch';

/**
 * Proyección 2.5D estilo DLS: cámara elevada mirando la cancha con perspectiva.
 * El mundo es plano (metros). La proyección se "hornea" una vez: la cancha queda como un
 * trapecio en un espacio 2D fijo ("espacio proyectado", en píxeles) y la cámara de Phaser
 * simplemente se desplaza y hace zoom sobre ese espacio.
 *
 *   k(y)  = 1 / (1 + a·(W − y)/W)      escala horizontal según profundidad (lejos = menor)
 *   sx    = cx + (x − cx)·k(y)·PX
 *   sy    = PX·V·(W/a)·[ln(1+a) − ln(1 + a·(W − y)/W)]   integral de k → filas más altas de cerca
 *   sz    = z·k(y)·PX·H                 altura sube en pantalla escalada por profundidad
 */
export const PX = 16;            // píxeles por metro en la banda cercana
const A = 0.30;                  // fuerza de la perspectiva (0 = ortográfica)
const V = 0.80;                  // compresión vertical del plano de juego
const H = 0.95;                  // factor de altura (z) en pantalla
const W = PITCH.WIDTH;
const LN1A = Math.log(1 + A);

export function depthScale(y: number): number {
  return 1 / (1 + (A * (W - y)) / W);
}

export function projectX(x: number, y: number): number {
  return CENTER_X * PX + (x - CENTER_X) * depthScale(y) * PX;
}

export function projectY(y: number, z = 0): number {
  const ground = PX * V * (W / A) * (LN1A - Math.log(1 + (A * (W - y)) / W));
  return ground - z * depthScale(y) * PX * H;
}

export interface ScreenPoint { x: number; y: number }

export function project(x: number, y: number, z: number, out: ScreenPoint): ScreenPoint {
  out.x = projectX(x, y);
  out.y = projectY(y, z);
  return out;
}

/** Píxeles proyectados de un objeto de `meters` de alto en la profundidad y. */
export function sizeAt(y: number, meters: number): number {
  return meters * depthScale(y) * PX;
}

/** Límites del espacio proyectado (cancha + margen), para acotar la cámara. */
export function projectedBounds(): { x: number; y: number; width: number; height: number } {
  const mx = 34, my = 16;
  const left = projectX(-mx, W + my);
  const right = projectX(PITCH.LENGTH + mx, W + my);
  const top = projectY(-my, PITCH.GOAL_HEIGHT + 1);
  const bottom = projectY(W + my, 0);
  return { x: left, y: top, width: right - left, height: bottom - top };
}

/** Área que la cámara puede encuadrar: cancha + margen jugable. */
export function cameraBounds(): { x: number; y: number; width: number; height: number } {
  const m = PITCH.MARGIN;
  const left = projectX(-m - 4, W + m);
  const right = projectX(PITCH.LENGTH + m + 4, W + m);
  const top = projectY(-m - 2, PITCH.GOAL_HEIGHT + 2);
  const bottom = projectY(W + m + 2, 0);
  return { x: left, y: top, width: right - left, height: bottom - top };
}
