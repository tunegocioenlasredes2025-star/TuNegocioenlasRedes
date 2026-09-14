import { Ball } from '@core/physics/Ball';
import { PlayerBody } from '@core/physics/PlayerBody';
import { applyKick, type KickType } from '@core/physics/Kick';
import { collideGoal, isGoal, clampToWorld } from '@core/physics/Collisions';
import { Possession } from './Possession';
import { consumeReleases, type InputState } from './InputState';
import { TUNING, type Tuning } from '@core/Tuning';
import { CENTER_X, CENTER_Y, PITCH, isInsidePitch, type Side } from '@core/pitch/Pitch';

export type SimEvent =
  | { type: 'kick'; kind: KickType; power: number }
  | { type: 'goal'; side: Side }
  | { type: 'out' }
  | { type: 'post' | 'bar' | 'net' }
  | { type: 'bounce' };

/**
 * Simulación de la Fase 1: un jugador, una pelota, dos arcos.
 * Paso fijo (`FIXED_DT`). Determinista: mismo input → mismo resultado.
 */
export const FIXED_DT = 1 / 60;

export class MatchSim {
  readonly ball: Ball;
  readonly player: PlayerBody;
  readonly events: SimEvent[] = [];
  goals: { home: number; away: number } = { home: 0, away: 0 };
  /** Segundos que faltan para reanudar tras gol/out. 0 = en juego. */
  restartTimer = 0;
  tick = 0;

  private readonly possession: Possession;
  private lastBounces = 0;

  constructor(private readonly t: Tuning = TUNING) {
    this.ball = new Ball(t.ball);
    this.player = new PlayerBody(t.player);
    this.possession = new Possession(t.player);
    this.kickoff();
  }

  kickoff(): void {
    this.ball.reset(CENTER_X, CENTER_Y);
    this.player.reset(CENTER_X - 3, CENTER_Y, 0);
    this.restartTimer = 0;
    this.lastBounces = 0;
  }

  step(input: InputState, dt: number = FIXED_DT): void {
    this.tick++;
    this.events.length = 0;

    if (this.restartTimer > 0) {
      this.restartTimer -= dt;
      if (this.restartTimer <= 0) this.kickoff();
      consumeReleases(input);
      return;
    }

    this.player.step(input.moveX, input.moveY, input.sprint, dt);
    const controlled = this.possession.step(this.player, this.ball, dt);

    if (controlled) {
      const kick = this.pickKick(input);
      if (kick) {
        const stick = this.stickSide(input);
        const fx = this.player.facingX(), fy = this.player.facingY();
        // Dirección del toque: hacia donde apunta el joystick si lo está usando, si no hacia donde mira.
        const useStick = input.moveX !== 0 || input.moveY !== 0;
        const len = useStick ? Math.hypot(input.moveX, input.moveY) : 1;
        const dx = useStick ? input.moveX / len : fx;
        const dy = useStick ? input.moveY / len : fy;
        applyKick(this.ball, kick.kind, this.t.kick, { dirX: dx, dirY: dy, power: kick.power, stickSide: stick });
        this.possession.release(this.player);
        this.events.push({ type: 'kick', kind: kick.kind, power: kick.power });
      }
    }

    if (!this.player.hasBall) {
      this.ball.step(dt);
      const hit = collideGoal(this.ball, 'home', this.t.ball) ?? collideGoal(this.ball, 'away', this.t.ball);
      if (hit) this.events.push({ type: hit });
      clampToWorld(this.ball);
      if (this.ball.bounces !== this.lastBounces) { this.lastBounces = this.ball.bounces; this.events.push({ type: 'bounce' }); }
    }

    if (isGoal(this.ball, 'away', this.t.ball)) {
      this.goals.home++;
      this.events.push({ type: 'goal', side: 'away' });
      this.restartTimer = 2.5;
    } else if (isGoal(this.ball, 'home', this.t.ball)) {
      this.goals.away++;
      this.events.push({ type: 'goal', side: 'home' });
      this.restartTimer = 2.5;
    } else if (!isInsidePitch(this.ball.pos.x, this.ball.pos.y) && this.isClearlyOut()) {
      this.events.push({ type: 'out' });
      this.restartTimer = 1.2;
    }

    consumeReleases(input);
  }

  private isClearlyOut(): boolean {
    const b = this.ball;
    const r = this.t.ball.radius;
    // Fuera por línea de fondo pero entre los postes es gol o red, no "out".
    const outX = b.pos.x < -r || b.pos.x > PITCH.LENGTH + r;
    const outY = b.pos.y < -r || b.pos.y > PITCH.WIDTH + r;
    if (outY) return true;
    if (!outX) return false;
    const inGoalMouth = b.pos.y > CENTER_Y - PITCH.GOAL_WIDTH / 2 && b.pos.y < CENTER_Y + PITCH.GOAL_WIDTH / 2 && b.z < PITCH.GOAL_HEIGHT;
    return !inGoalMouth;
  }

  private pickKick(input: InputState): { kind: KickType; power: number } | null {
    if (input.shotRelease >= 0) return { kind: 'shot', power: input.shotRelease };
    if (input.passRelease >= 0) return { kind: 'pass', power: input.passRelease };
    if (input.lobRelease >= 0) return { kind: 'lob', power: input.lobRelease };
    return null;
  }

  /** Componente lateral del joystick respecto a la orientación del jugador (−1..1). */
  private stickSide(input: InputState): number {
    const len = Math.hypot(input.moveX, input.moveY);
    if (len < 0.2) return 0;
    const fx = this.player.facingX(), fy = this.player.facingY();
    return (fx * input.moveY - fy * input.moveX) / len;
  }
}
