/** Vector 2D mutable. Sin allocaciones en el hot path: todos los métodos operan in-place. */
export class Vec2 {
  constructor(public x = 0, public y = 0) {}

  set(x: number, y: number): this { this.x = x; this.y = y; return this; }
  copy(v: Readonly<Vec2>): this { this.x = v.x; this.y = v.y; return this; }
  clone(): Vec2 { return new Vec2(this.x, this.y); }
  add(v: Readonly<Vec2>): this { this.x += v.x; this.y += v.y; return this; }
  sub(v: Readonly<Vec2>): this { this.x -= v.x; this.y -= v.y; return this; }
  scale(s: number): this { this.x *= s; this.y *= s; return this; }
  addScaled(v: Readonly<Vec2>, s: number): this { this.x += v.x * s; this.y += v.y * s; return this; }
  length(): number { return Math.hypot(this.x, this.y); }
  lengthSq(): number { return this.x * this.x + this.y * this.y; }
  normalize(): this {
    const l = this.length();
    if (l > 1e-9) { this.x /= l; this.y /= l; } else { this.x = 0; this.y = 0; }
    return this;
  }
  /** Limita el módulo a `max` sin cambiar la dirección. */
  clampLength(max: number): this {
    const l2 = this.lengthSq();
    if (l2 > max * max) { const s = max / Math.sqrt(l2); this.x *= s; this.y *= s; }
    return this;
  }
  dot(v: Readonly<Vec2>): number { return this.x * v.x + this.y * v.y; }
  /** Producto cruz 2D (escalar). Positivo si v está a la izquierda de this. */
  cross(v: Readonly<Vec2>): number { return this.x * v.y - this.y * v.x; }
  angle(): number { return Math.atan2(this.y, this.x); }
  setAngle(angle: number, length = 1): this { this.x = Math.cos(angle) * length; this.y = Math.sin(angle) * length; return this; }
  distanceTo(v: Readonly<Vec2>): number { return Math.hypot(this.x - v.x, this.y - v.y); }
  distanceSqTo(v: Readonly<Vec2>): number { const dx = this.x - v.x; const dy = this.y - v.y; return dx * dx + dy * dy; }
  /** Rota 90° a la izquierda (perpendicular). */
  perp(): this { const x = this.x; this.x = -this.y; this.y = x; return this; }
  lerp(v: Readonly<Vec2>, t: number): this { this.x += (v.x - this.x) * t; this.y += (v.y - this.y) * t; return this; }
  isZero(eps = 1e-9): boolean { return Math.abs(this.x) < eps && Math.abs(this.y) < eps; }
}
