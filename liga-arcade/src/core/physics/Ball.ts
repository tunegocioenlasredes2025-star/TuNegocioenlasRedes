import { Vec2 } from '@core/math/Vec2';
import type { BallTuning } from '@core/Tuning';

/**
 * Pelota con altura real. Posición horizontal en metros (x, y), altura z en metros.
 * `spin` es efecto lateral: positivo curva hacia la izquierda de la dirección de avance.
 * Integración semi-implícita a paso fijo; sin allocaciones.
 */
export class Ball {
  readonly pos = new Vec2();
  readonly vel = new Vec2();
  /** Posición al inicio del último `step` (para colisiones continuas contra postes). */
  readonly prev = new Vec2();
  prevZ = 0;
  z = 0;
  vz = 0;
  spin = 0;
  /** Cantidad de piques desde el último toque (para animación y sonido). */
  bounces = 0;
  /** True si está rodando/apoyada, false si está en el aire. */
  grounded = true;

  private readonly tmp = new Vec2();

  constructor(private readonly t: BallTuning) {}

  reset(x: number, y: number): void {
    this.pos.set(x, y);
    this.prev.set(x, y);
    this.vel.set(0, 0);
    this.z = 0; this.prevZ = 0; this.vz = 0; this.spin = 0; this.bounces = 0; this.grounded = true;
  }

  speed(): number { return this.vel.length(); }

  /** Impulso instantáneo: velocidad horizontal, elevación vertical y efecto. */
  kick(dirX: number, dirY: number, speed: number, elevationRad: number, spin: number): void {
    const horiz = speed * Math.cos(elevationRad);
    this.vel.set(dirX * horiz, dirY * horiz);
    this.vz = speed * Math.sin(elevationRad);
    if (this.vz > 0.05) { this.grounded = false; if (this.z < 0.01) this.z = 0.01; }
    this.spin = spin;
    this.bounces = 0;
  }

  step(dt: number): void {
    const t = this.t;
    this.prev.copy(this.pos);
    this.prevZ = this.z;
    const speed = this.vel.length();

    if (this.grounded) {
      // Rodando: desaceleración constante por fricción de rodadura.
      if (speed > 0) {
        const newSpeed = Math.max(0, speed - t.rollingDecel * dt);
        if (newSpeed < t.stopSpeed) this.vel.set(0, 0);
        else this.vel.scale(newSpeed / speed);
      }
      this.z = 0; this.vz = 0;
    } else {
      // En el aire: gravedad + drag cuadrático + Magnus.
      this.vz -= t.gravity * dt;
      if (speed > 0) {
        const drag = t.airDrag * speed; // a = k·v·|v| → factor sobre v
        this.vel.scale(Math.max(0, 1 - drag * dt));
        if (Math.abs(this.spin) > 1e-3) {
          // Fuerza perpendicular a la velocidad, proporcional a spin·|v|.
          // vel.perp() ya tiene módulo |v|: fuerza ∝ spin·|v|.
          this.tmp.copy(this.vel).perp().scale(this.spin * t.spinMagnus * dt);
          this.vel.add(this.tmp);
        }
      }
    }

    // Efecto también actúa rodando (más suave), y decae con el tiempo.
    if (this.grounded && Math.abs(this.spin) > 1e-3 && speed > 0.5) {
      this.tmp.copy(this.vel).perp().scale(this.spin * t.spinMagnus * 0.35 * dt);
      this.vel.add(this.tmp);
    }
    this.spin *= Math.max(0, 1 - t.spinDecay * dt);

    this.pos.addScaled(this.vel, dt);
    if (!this.grounded) {
      this.z += this.vz * dt;
      if (this.z <= 0) this.land();
    }
  }

  private land(): void {
    const t = this.t;
    this.z = 0;
    const bounceVz = -this.vz * t.bounceRestitution;
    this.vel.scale(t.bounceHorizontalKeep);
    this.bounces++;
    if (bounceVz > t.minBounceVz) {
      this.vz = bounceVz;
    } else {
      this.vz = 0;
      this.grounded = true;
    }
  }
}
