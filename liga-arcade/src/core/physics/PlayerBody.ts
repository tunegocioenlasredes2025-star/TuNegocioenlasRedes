import { Vec2 } from '@core/math/Vec2';
import type { PlayerTuning } from '@core/Tuning';
import { rotateToward } from '@core/math/scalar';

/**
 * Cuerpo de un jugador: posición, velocidad y orientación.
 * El movimiento tiene inercia (aceleración/desaceleración) para que se sienta con peso
 * pero responda al instante: el primer frame ya acelera fuerte.
 */
export class PlayerBody {
  readonly pos = new Vec2();
  readonly vel = new Vec2();
  /** Orientación en radianes (hacia dónde mira). */
  facing = 0;
  sprinting = false;
  hasBall = false;

  private readonly desired = new Vec2();
  private readonly tmp = new Vec2();

  constructor(private readonly t: PlayerTuning) {}

  reset(x: number, y: number, facing = 0): void {
    this.pos.set(x, y); this.vel.set(0, 0); this.facing = facing; this.sprinting = false; this.hasBall = false;
  }

  speed(): number { return this.vel.length(); }
  facingX(): number { return Math.cos(this.facing); }
  facingY(): number { return Math.sin(this.facing); }

  /**
   * @param moveX,moveY dirección de input (módulo 0–1).
   */
  step(moveX: number, moveY: number, sprint: boolean, dt: number): void {
    const t = this.t;
    this.sprinting = sprint && (moveX !== 0 || moveY !== 0);
    let maxSpeed = this.sprinting ? t.sprintSpeed : t.runSpeed;
    if (this.hasBall) maxSpeed *= t.withBallSpeedFactor;

    this.desired.set(moveX, moveY);
    const mag = Math.min(1, this.desired.length());
    if (mag > 0) {
      this.desired.normalize().scale(maxSpeed * mag);
      // Girar hacia la dirección del input (rápido: el control tiene que sentirse inmediato).
      this.facing = rotateToward(this.facing, this.desired.angle(), t.turnRateRad * dt);
    }

    // Acelerar hacia la velocidad deseada.
    this.tmp.copy(this.desired).sub(this.vel);
    const diff = this.tmp.length();
    if (diff > 0) {
      const rate = mag > 0 ? t.accel : t.decel;
      const stepLen = Math.min(diff, rate * dt);
      this.vel.addScaled(this.tmp.scale(1 / diff), stepLen);
    }
    this.pos.addScaled(this.vel, dt);
  }
}
