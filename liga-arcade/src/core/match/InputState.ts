/**
 * Estado de input plano que el core lee cada tick. La capa de presentación lo escribe
 * directamente desde los eventos de puntero (sin colas) para minimizar latencia.
 */
export interface InputState {
  /** Dirección del joystick, módulo 0–1. */
  moveX: number;
  moveY: number;
  sprint: boolean;
  /** Botón de acción mantenido (cargando potencia). */
  shotHeld: boolean;
  passHeld: boolean;
  lobHeld: boolean;
  /** Flags de "soltó el botón" en este tick: potencia 0–1. -1 si no hubo release. */
  shotRelease: number;
  passRelease: number;
  lobRelease: number;
}

export function createInputState(): InputState {
  return {
    moveX: 0, moveY: 0, sprint: false,
    shotHeld: false, passHeld: false, lobHeld: false,
    shotRelease: -1, passRelease: -1, lobRelease: -1,
  };
}

/** Limpia los flags de un solo tick. Llamar al final de cada paso de simulación. */
export function consumeReleases(s: InputState): void {
  s.shotRelease = -1; s.passRelease = -1; s.lobRelease = -1;
}
