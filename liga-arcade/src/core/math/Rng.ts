/** RNG determinista (mulberry32). Misma semilla → misma secuencia. Necesario para tests y replays. */
export class Rng {
  private state: number;
  constructor(seed: number) { this.state = seed >>> 0; }

  /** [0, 1) */
  next(): number {
    let t = (this.state += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  }
  range(min: number, max: number): number { return min + (max - min) * this.next(); }
  int(min: number, maxInclusive: number): number { return Math.floor(this.range(min, maxInclusive + 1)); }
  /** Aproximación gaussiana (suma de 3 uniformes), media 0, desvío ~1. */
  gaussian(): number { return ((this.next() + this.next() + this.next()) - 1.5) * 2; }
  pick<T>(arr: readonly T[]): T {
    const v = arr[this.int(0, arr.length - 1)];
    if (v === undefined) throw new Error('Rng.pick: array vacío');
    return v;
  }
}
