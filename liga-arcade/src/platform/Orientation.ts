/** Intenta bloquear landscape. En Safari iOS no está permitido: el overlay CSS "Girá el teléfono" cubre ese caso. */
export async function tryLockLandscape(): Promise<void> {
  try {
    const o = screen.orientation as ScreenOrientation & { lock?: (t: string) => Promise<void> };
    if (o && typeof o.lock === 'function') await o.lock('landscape');
  } catch {
    /* no soportado o no permitido: se resuelve con el overlay */
  }
}
