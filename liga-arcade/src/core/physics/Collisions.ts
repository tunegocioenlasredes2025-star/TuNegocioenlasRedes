import { PITCH, GOAL_TOP, GOAL_BOTTOM, type Side } from '@core/pitch/Pitch';
import type { BallTuning } from '@core/Tuning';
import type { Ball } from './Ball';

export type GoalHit = 'post' | 'bar' | 'net';

/**
 * Intersección continua del segmento p0→p1 con un círculo (centro c, radio r) en 2D.
 * Devuelve el t ∈ [0,1] del primer contacto, 0 si p0 ya está adentro, o -1 si no toca.
 */
function sweepCircle(p0x: number, p0y: number, p1x: number, p1y: number, cx: number, cy: number, r: number): number {
  const fx = p0x - cx, fy = p0y - cy;
  if (fx * fx + fy * fy < r * r) return 0;
  const dx = p1x - p0x, dy = p1y - p0y;
  const a = dx * dx + dy * dy;
  if (a < 1e-12) return -1;
  const b = 2 * (fx * dx + fy * dy);
  const c = fx * fx + fy * fy - r * r;
  const disc = b * b - 4 * a * c;
  if (disc < 0) return -1;
  const t = (-b - Math.sqrt(disc)) / (2 * a);
  return t >= 0 && t <= 1 ? t : -1;
}

/**
 * Colisiones de la pelota con postes, travesaño y red. Se llama después de `ball.step`.
 * Usa la posición previa para no atravesar postes a alta velocidad (tunneling).
 */
export function collideGoal(ball: Ball, side: Side, t: BallTuning): GoalHit | null {
  const lineX = side === 'home' ? 0 : PITCH.LENGTH;
  const inward = side === 'home' ? 1 : -1; // hacia la cancha
  const r = t.radius + PITCH.POST_RADIUS;

  // Postes: cilindros verticales en (lineX, GOAL_TOP) y (lineX, GOAL_BOTTOM).
  if (Math.min(ball.z, ball.prevZ) < PITCH.GOAL_HEIGHT + t.radius) {
    for (const py of [GOAL_TOP, GOAL_BOTTOM]) {
      const k = sweepCircle(ball.prev.x, ball.prev.y, ball.pos.x, ball.pos.y, lineX, py, r);
      if (k < 0) continue;
      const cxp = ball.prev.x + (ball.pos.x - ball.prev.x) * k;
      const cyp = ball.prev.y + (ball.pos.y - ball.prev.y) * k;
      let nx = cxp - lineX, ny = cyp - py;
      const d = Math.hypot(nx, ny);
      if (d < 1e-6) { nx = -ball.vel.x; ny = -ball.vel.y; const l = Math.hypot(nx, ny) || 1; nx /= l; ny /= l; }
      else { nx /= d; ny /= d; }
      const vn = ball.vel.x * nx + ball.vel.y * ny;
      if (vn < 0) {
        ball.vel.x -= (1 + t.postRestitution) * vn * nx;
        ball.vel.y -= (1 + t.postRestitution) * vn * ny;
        ball.spin *= 0.3;
      }
      ball.pos.x = lineX + nx * (r + 0.005);
      ball.pos.y = py + ny * (r + 0.005);
      return 'post';
    }
  }

  // Travesaño: cilindro horizontal a lo largo de y en (lineX, z = GOAL_HEIGHT). Plano x–z.
  if (ball.pos.y > GOAL_TOP - r && ball.pos.y < GOAL_BOTTOM + r) {
    const k = sweepCircle(ball.prev.x, ball.prevZ, ball.pos.x, ball.z, lineX, PITCH.GOAL_HEIGHT, r);
    if (k >= 0) {
      const cxp = ball.prev.x + (ball.pos.x - ball.prev.x) * k;
      const czp = ball.prevZ + (ball.z - ball.prevZ) * k;
      let nx = cxp - lineX, nz = czp - PITCH.GOAL_HEIGHT;
      const d = Math.hypot(nx, nz);
      if (d < 1e-6) { nx = -Math.sign(ball.vel.x) || 1; nz = 0; } else { nx /= d; nz /= d; }
      const vn = ball.vel.x * nx + ball.vz * nz;
      if (vn < 0) {
        ball.vel.x -= (1 + t.postRestitution) * vn * nx;
        ball.vz -= (1 + t.postRestitution) * vn * nz;
        ball.grounded = false;
      }
      ball.pos.x = lineX + nx * (r + 0.005);
      ball.z = PITCH.GOAL_HEIGHT + nz * (r + 0.005);
      return 'bar';
    }
  }

  // Red: región detrás de la línea, entre los postes, bajo el travesaño.
  const behind = (ball.pos.x - lineX) * inward; // negativo = detrás de la línea
  if (behind < 0 && ball.pos.y > GOAL_TOP && ball.pos.y < GOAL_BOTTOM && ball.z < PITCH.GOAL_HEIGHT) {
    const k = Math.max(0, 1 - t.netDamping * (1 / 60));
    ball.vel.scale(k);
    ball.vz *= k;
    ball.spin = 0;
    const depth = PITCH.GOAL_DEPTH;
    if (-behind > depth - t.radius) {
      ball.pos.x = lineX - inward * (depth - t.radius);
      if ((ball.vel.x * inward) < 0) ball.vel.x = 0;
    }
    if (ball.pos.y < GOAL_TOP + t.radius) { ball.pos.y = GOAL_TOP + t.radius; if (ball.vel.y < 0) ball.vel.y = 0; }
    if (ball.pos.y > GOAL_BOTTOM - t.radius) { ball.pos.y = GOAL_BOTTOM - t.radius; if (ball.vel.y > 0) ball.vel.y = 0; }
    if (ball.z > PITCH.GOAL_HEIGHT - t.radius) { ball.z = PITCH.GOAL_HEIGHT - t.radius; if (ball.vz > 0) ball.vz = 0; }
    return 'net';
  }
  return null;
}

/** Gol: la pelota cruzó completamente la línea entre los postes y bajo el travesaño. */
export function isGoal(ball: Ball, side: Side, t: BallTuning): boolean {
  const lineX = side === 'home' ? 0 : PITCH.LENGTH;
  const inward = side === 'home' ? 1 : -1;
  const behind = (ball.pos.x - lineX) * inward;
  return behind < -t.radius && ball.pos.y > GOAL_TOP && ball.pos.y < GOAL_BOTTOM && ball.z < PITCH.GOAL_HEIGHT;
}

/** Mantiene la pelota dentro del mundo (cancha + margen) con un rebote suave contra el borde. */
export function clampToWorld(ball: Ball): void {
  const m = PITCH.MARGIN;
  if (ball.pos.x < -m) { ball.pos.x = -m; ball.vel.x = Math.abs(ball.vel.x) * 0.3; }
  if (ball.pos.x > PITCH.LENGTH + m) { ball.pos.x = PITCH.LENGTH + m; ball.vel.x = -Math.abs(ball.vel.x) * 0.3; }
  if (ball.pos.y < -m) { ball.pos.y = -m; ball.vel.y = Math.abs(ball.vel.y) * 0.3; }
  if (ball.pos.y > PITCH.WIDTH + m) { ball.pos.y = PITCH.WIDTH + m; ball.vel.y = -Math.abs(ball.vel.y) * 0.3; }
}
