/**
 * Geometría de la cancha en METROS. Origen (0,0) en la esquina superior izquierda.
 * x crece hacia la derecha (arco visitante), y crece hacia abajo (banda cercana a la cámara).
 * Arco local en x = 0, arco visitante en x = LENGTH.
 */
export const PITCH = {
  LENGTH: 105,
  WIDTH: 68,
  GOAL_WIDTH: 7.32,
  GOAL_HEIGHT: 2.44,
  GOAL_DEPTH: 2.0,
  POST_RADIUS: 0.06,
  PENALTY_AREA_LENGTH: 16.5,
  PENALTY_AREA_WIDTH: 40.32,
  GOAL_AREA_LENGTH: 5.5,
  GOAL_AREA_WIDTH: 18.32,
  PENALTY_SPOT: 11,
  CENTER_CIRCLE_RADIUS: 9.15,
  CORNER_RADIUS: 1,
  /** Margen fuera de la cancha que sigue siendo "mundo" (para que la pelota no desaparezca). */
  MARGIN: 6,
} as const;

export const CENTER_X = PITCH.LENGTH / 2;
export const CENTER_Y = PITCH.WIDTH / 2;
export const GOAL_TOP = CENTER_Y - PITCH.GOAL_WIDTH / 2;
export const GOAL_BOTTOM = CENTER_Y + PITCH.GOAL_WIDTH / 2;

export type Side = 'home' | 'away';

/** x de la línea de gol de cada lado. */
export function goalLineX(side: Side): number {
  return side === 'home' ? 0 : PITCH.LENGTH;
}

export function isInsidePitch(x: number, y: number): boolean {
  return x >= 0 && x <= PITCH.LENGTH && y >= 0 && y <= PITCH.WIDTH;
}

/** True si el punto está dentro del área grande del lado indicado. */
export function isInPenaltyArea(x: number, y: number, side: Side): boolean {
  const halfW = PITCH.PENALTY_AREA_WIDTH / 2;
  if (y < CENTER_Y - halfW || y > CENTER_Y + halfW) return false;
  return side === 'home' ? x <= PITCH.PENALTY_AREA_LENGTH : x >= PITCH.LENGTH - PITCH.PENALTY_AREA_LENGTH;
}
