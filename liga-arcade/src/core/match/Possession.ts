import { Vec2 } from '@core/math/Vec2';
import type { PlayerTuning } from '@core/Tuning';
import type { Ball } from '@core/physics/Ball';
import type { PlayerBody } from '@core/physics/PlayerBody';

/**
 * Control de la pelota por un jugador.
 * - Si la pelota llega baja y no demasiado rápida al radio de control, queda "pegada" delante del pie.
 * - Corriendo con la pelota: se lleva a `dribbleOffset` con un resorte (se siente elástica, no clavada).
 * - Sprintando: se la empuja adelante (`knockAhead`) y el jugador corre a buscarla, como en DLS.
 * - Tras patear, el jugador no puede recuperarla por `kickImmunitySeconds` (evita "morder" su propio tiro).
 */
export class Possession {
  private readonly target = new Vec2();
  private readonly tmp = new Vec2();
  private readonly rel = new Vec2();
  private knockCooldown = 0;
  private immunity = 0;

  constructor(private readonly t: PlayerTuning) {}

  /** Llamar cuando el jugador patea: suelta la pelota e inicia la inmunidad. */
  release(player: PlayerBody): void {
    player.hasBall = false;
    this.immunity = this.t.kickImmunitySeconds;
    this.knockCooldown = 0;
  }

  /** Devuelve true si el jugador tiene la pelota controlada en este tick. */
  step(player: PlayerBody, ball: Ball, dt: number): boolean {
    const t = this.t;
    this.knockCooldown = Math.max(0, this.knockCooldown - dt);
    this.immunity = Math.max(0, this.immunity - dt);
    const d = player.pos.distanceTo(ball.pos);

    if (player.hasBall) {
      if (d > t.ownershipRadius || ball.z > t.controlMaxBallZ) { player.hasBall = false; return false; }
    } else {
      if (this.immunity > 0) return false;
      if (d > t.controlRadius || ball.z > t.controlMaxBallZ) return false;
      this.rel.copy(ball.vel).sub(player.vel);
      const relSpeed = this.rel.length();
      // ¿La pelota viene hacia el jugador? Si se aleja, no hay contacto que evaluar.
      this.tmp.copy(ball.pos).sub(player.pos);
      const approaching = this.rel.dot(this.tmp) < 0;
      if (relSpeed > t.controlMaxRelSpeed) {
        if (approaching) ball.vel.scale(0.35); // le pega fuerte y no la para: rebote con pérdida
        return false;
      }
      player.hasBall = true;
      this.knockCooldown = 0;
    }

    const fx = player.facingX(), fy = player.facingY();
    if (player.sprinting) {
      if (d < t.dribbleOffset + 0.25 && this.knockCooldown <= 0) {
        const s = Math.max(player.speed(), 3) * t.knockAheadSpeedFactor;
        ball.vel.set(fx * s, fy * s);
        ball.z = 0; ball.vz = 0; ball.grounded = true; ball.spin = 0;
        this.knockCooldown = t.knockAheadDistance / s;
      }
      return true;
    }

    // Conducción: la pelota acompaña al jugador y un resorte la lleva delante del pie.
    ball.pos.addScaled(player.vel, dt);
    this.target.set(player.pos.x + fx * t.dribbleOffset, player.pos.y + fy * t.dribbleOffset);
    this.tmp.copy(this.target).sub(ball.pos);
    const pull = 1 - Math.exp(-t.dribbleSpringLambda * dt);
    ball.pos.addScaled(this.tmp, pull);
    ball.vel.copy(player.vel);
    ball.z = 0; ball.vz = 0; ball.grounded = true; ball.spin = 0;
    return true;
  }
}
