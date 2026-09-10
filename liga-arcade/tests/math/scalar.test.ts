import { describe, it, expect } from 'vitest';
import { angleDelta, rotateToward, clamp, moveToward, damp } from '@core/math/scalar';
import { Vec2 } from '@core/math/Vec2';
import { Rng } from '@core/math/Rng';

describe('scalar', () => {
  it('angleDelta toma el camino corto', () => {
    expect(angleDelta(0, Math.PI / 2)).toBeCloseTo(Math.PI / 2);
    expect(angleDelta(0, -Math.PI / 2)).toBeCloseTo(-Math.PI / 2);
    expect(angleDelta(Math.PI * 0.9, -Math.PI * 0.9)).toBeCloseTo(Math.PI * 0.2);
  });
  it('rotateToward respeta el máximo', () => {
    expect(rotateToward(0, Math.PI, 0.1)).toBeCloseTo(0.1);
    expect(rotateToward(0, 0.05, 0.1)).toBeCloseTo(0.05);
  });
  it('clamp y moveToward', () => {
    expect(clamp(5, 0, 3)).toBe(3);
    expect(moveToward(0, 10, 3)).toBe(3);
    expect(moveToward(9, 10, 3)).toBe(10);
  });
  it('damp converge sin pasarse', () => {
    let v = 0;
    for (let i = 0; i < 300; i++) v = damp(v, 1, 8, 1 / 60);
    expect(v).toBeGreaterThan(0.99);
    expect(v).toBeLessThanOrEqual(1);
  });
});

describe('Vec2', () => {
  it('normalize, perp y clampLength', () => {
    const v = new Vec2(3, 4);
    expect(v.length()).toBe(5);
    v.normalize();
    expect(v.length()).toBeCloseTo(1);
    const p = new Vec2(1, 0).perp();
    expect(p.x).toBeCloseTo(0); expect(p.y).toBeCloseTo(1);
    const c = new Vec2(10, 0).clampLength(2);
    expect(c.x).toBeCloseTo(2);
  });
});

describe('Rng', () => {
  it('es determinista por semilla y queda en [0,1)', () => {
    const a = new Rng(42), b = new Rng(42);
    for (let i = 0; i < 100; i++) {
      const x = a.next();
      expect(x).toBe(b.next());
      expect(x).toBeGreaterThanOrEqual(0); expect(x).toBeLessThan(1);
    }
  });
});
