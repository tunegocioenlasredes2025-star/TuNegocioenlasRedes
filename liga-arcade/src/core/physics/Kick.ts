import type { KickProfile, KickTuning } from '@core/Tuning';
import { clamp01, lerp } from '@core/math/scalar';
import type { Ball } from './Ball';

export type KickType = 'shot' | 'pass' | 'lob';

const DEG = Math.PI / 180;

export interface KickParams {
  dirX: number; dirY: number;
  /** 0–1 por duración del toque. */
  power: number;
  /** Componente lateral del joystick respecto a la dirección del toque (−1..1) → efecto. */
  stickSide: number;
}

/** Traduce tipo de toque + potencia + joystick a velocidad, elevación y efecto. */
export function resolveKick(kind: KickType, t: KickTuning, p: KickParams): { speed: number; elevation: number; spin: number } {
  const prof: KickProfile = t[kind];
  const power = clamp01(p.power);
  const speed = lerp(prof.minSpeed, prof.maxSpeed, power);
  const elevationDeg = prof.elevationDeg !== undefined
    ? prof.elevationDeg
    : lerp(prof.minElevationDeg ?? 0, prof.maxElevationDeg ?? 0, power);
  return { speed, elevation: elevationDeg * DEG, spin: -p.stickSide * prof.spinFromStick };
}

export function applyKick(ball: Ball, kind: KickType, t: KickTuning, p: KickParams): void {
  const r = resolveKick(kind, t, p);
  ball.kick(p.dirX, p.dirY, r.speed, r.elevation, r.spin);
}
