import tuningJson from '@data/tuning.json';

export interface BallTuning {
  gravity: number; airDrag: number; rollingDecel: number; stopSpeed: number;
  bounceRestitution: number; bounceHorizontalKeep: number; minBounceVz: number;
  spinMagnus: number; spinDecay: number; postRestitution: number; netDamping: number; radius: number;
}
export interface KickProfile {
  minSpeed: number; maxSpeed: number; spinFromStick: number;
  minElevationDeg?: number; maxElevationDeg?: number; elevationDeg?: number;
}
export interface KickTuning { shot: KickProfile; pass: KickProfile; lob: KickProfile; maxHoldSeconds: number }
export interface PlayerTuning {
  radius: number; runSpeed: number; sprintSpeed: number; accel: number; decel: number; turnRateRad: number;
  withBallSpeedFactor: number; controlRadius: number; controlMaxBallZ: number; controlMaxRelSpeed: number;
  dribbleOffset: number; knockAheadDistance: number; knockAheadSpeedFactor: number; ownershipRadius: number;
  kickImmunitySeconds: number; dribbleSpringLambda: number;
}
export interface CameraTuning { lookAhead: number; followLambda: number; zoomMin: number; zoomMax: number }
export interface Tuning { ball: BallTuning; kick: KickTuning; player: PlayerTuning; camera: CameraTuning }

/** Constantes de juego. Se cargan del JSON para poder afinar sin tocar código. */
export const TUNING: Tuning = tuningJson as Tuning;
