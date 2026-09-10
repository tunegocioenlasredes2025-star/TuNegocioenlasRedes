/** Insets del notch / barra de inicio, leídos de las variables CSS definidas en index.html. */
export interface SafeInsets { top: number; right: number; bottom: number; left: number }

export function readSafeInsets(): SafeInsets {
  const cs = getComputedStyle(document.documentElement);
  const px = (v: string): number => { const n = parseFloat(v); return Number.isFinite(n) ? n : 0; };
  return {
    top: px(cs.getPropertyValue('--sat')),
    right: px(cs.getPropertyValue('--sar')),
    bottom: px(cs.getPropertyValue('--sab')),
    left: px(cs.getPropertyValue('--sal')),
  };
}
