import { describe, it, expect } from 'vitest';
import { Ball } from '@core/physics/Ball';
import { TUNING } from '@core/Tuning';
import { collideGoal, isGoal } from '@core/physics/Collisions';
import { PITCH, CENTER_Y, GOAL_TOP } from '@core/pitch/Pitch';

const DT = 1 / 60;
function run(ball: Ball, seconds: number, each?: () => void): void {
  const n = Math.round(seconds / DT);
  for (let i = 0; i < n; i++) { ball.step(DT); each?.(); }
}

describe('Ball', () => {
  it('rodando desacelera y se detiene', () => {
    const b = new Ball(TUNING.ball);
    b.reset(50, 34);
    b.kick(1, 0, 10, 0, 0);
    expect(b.grounded).toBe(true);
    run(b, 1);
    expect(b.speed()).toBeLessThan(10);
    expect(b.speed()).toBeGreaterThan(0);
    run(b, 10);
    expect(b.speed()).toBe(0);
    expect(b.pos.x).toBeGreaterThan(50);
  });

  it('un tiro elevado describe una parábola y vuelve al piso', () => {
    const b = new Ball(TUNING.ball);
    b.reset(50, 34);
    b.kick(1, 0, 20, Math.PI / 6, 0);
    expect(b.grounded).toBe(false);
    let maxZ = 0;
    run(b, 0.6, () => { maxZ = Math.max(maxZ, b.z); });
    expect(maxZ).toBeGreaterThan(2);
    run(b, 6);
    expect(b.grounded).toBe(true);
    expect(b.z).toBe(0);
    expect(b.bounces).toBeGreaterThanOrEqual(1);
  });

  it('el pique pierde energía: cada rebote es más bajo', () => {
    const b = new Ball(TUNING.ball);
    b.reset(50, 34);
    b.kick(0, 0, 12, Math.PI / 2, 0);
    const peaks: number[] = [];
    let lastZ = 0, rising = true;
    run(b, 8, () => {
      if (rising && b.z < lastZ) { peaks.push(lastZ); rising = false; }
      if (!rising && b.z > lastZ) rising = true;
      lastZ = b.z;
    });
    expect(peaks.length).toBeGreaterThanOrEqual(3);
    for (let i = 1; i < peaks.length; i++) expect(peaks[i]!).toBeLessThan(peaks[i - 1]!);
  });

  it('el efecto curva hacia la izquierda con spin positivo y hacia la derecha con negativo', () => {
    const left = new Ball(TUNING.ball); left.reset(20, 34); left.kick(1, 0, 25, 0.15, 6);
    const right = new Ball(TUNING.ball); right.reset(20, 34); right.kick(1, 0, 25, 0.15, -6);
    run(left, 1.2); run(right, 1.2);
    // perp() de (1,0) es (0,1): "izquierda" en nuestro sistema es +y.
    expect(left.pos.y).toBeGreaterThan(34.3);
    expect(right.pos.y).toBeLessThan(33.7);
    expect(Math.abs(left.pos.y - 34)).toBeCloseTo(Math.abs(right.pos.y - 34), 3);
  });

  it('sin fuerzas laterales, un tiro recto se mantiene recto', () => {
    const b = new Ball(TUNING.ball); b.reset(20, 34); b.kick(1, 0, 25, 0.2, 0);
    run(b, 2);
    expect(b.pos.y).toBeCloseTo(34, 6);
  });
});

describe('Arco', () => {
  it('detecta gol solo cuando la pelota cruzó completa la línea entre los postes', () => {
    const b = new Ball(TUNING.ball);
    b.reset(PITCH.LENGTH + 0.05, CENTER_Y);
    expect(isGoal(b, 'away', TUNING.ball)).toBe(false);
    b.reset(PITCH.LENGTH + 0.2, CENTER_Y);
    expect(isGoal(b, 'away', TUNING.ball)).toBe(true);
    b.reset(PITCH.LENGTH + 0.2, GOAL_TOP - 0.5);
    expect(isGoal(b, 'away', TUNING.ball)).toBe(false);
    b.reset(PITCH.LENGTH + 0.2, CENTER_Y); b.z = PITCH.GOAL_HEIGHT + 0.5;
    expect(isGoal(b, 'away', TUNING.ball)).toBe(false);
  });

  it('un tiro al poste rebota hacia la cancha', () => {
    const b = new Ball(TUNING.ball);
    b.reset(PITCH.LENGTH - 0.3, GOAL_TOP);
    b.kick(1, 0, 20, 0, 0);
    let hit: string | null = null;
    for (let i = 0; i < 20 && !hit; i++) { b.step(DT); hit = collideGoal(b, 'away', TUNING.ball); }
    expect(hit).toBe('post');
    expect(b.vel.x).toBeLessThan(0);
  });

  it('un tiro al travesaño rebota hacia abajo/afuera', () => {
    const b = new Ball(TUNING.ball);
    b.reset(PITCH.LENGTH - 2, CENTER_Y);
    b.z = PITCH.GOAL_HEIGHT - 0.02; b.vz = 0; b.grounded = false;
    b.vel.set(20, 0);
    let hit: string | null = null;
    for (let i = 0; i < 20 && !hit; i++) { b.step(DT); hit = collideGoal(b, 'away', TUNING.ball); }
    expect(hit).toBe('bar');
    expect(b.vel.x).toBeLessThan(0);
  });

  it('la red frena la pelota y no la deja atravesar el fondo', () => {
    const b = new Ball(TUNING.ball);
    b.reset(PITCH.LENGTH - 1, CENTER_Y);
    b.kick(1, 0, 30, 0.05, 0);
    for (let i = 0; i < 120; i++) { b.step(DT); collideGoal(b, 'away', TUNING.ball); }
    expect(b.pos.x).toBeLessThanOrEqual(PITCH.LENGTH + PITCH.GOAL_DEPTH);
    expect(b.speed()).toBeLessThan(1);
    expect(isGoal(b, 'away', TUNING.ball)).toBe(true);
  });
});
