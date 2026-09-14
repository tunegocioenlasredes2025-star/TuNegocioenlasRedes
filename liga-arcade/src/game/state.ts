import { createInputState, type InputState } from '@core/match/InputState';

/** Estado compartido entre escenas (HUD escribe input, Match lo lee). */
export const input: InputState = createInputState();

/** Métricas para el overlay de stats. */
export const stats = {
  fps: 0,
  fpsLow: 0,
  simMs: 0,
  frameMs: 0,
  drawCalls: 0,
  /** Marca de tiempo (performance.now) del último pointerdown pendiente de medir. */
  pendingInputStamp: -1,
  inputLatencyMs: 0,
  inputLatencyAvgMs: 0,
  bootToMenuMs: 0,
  overlayVisible: false,
};

/** Factor de píxeles por punto CSS con el que corre el canvas (tope 2 por performance). */
export const DPR = Math.min(2, Math.max(1, Math.round((window.devicePixelRatio || 1) * 2) / 2));
