import Phaser from 'phaser';
import type { InputState } from '@core/match/InputState';
import { stats } from '@game/state';

export type ButtonId = 'shot' | 'pass' | 'lob' | 'sprint';

interface ButtonDef { id: ButtonId; label: string; color: number; radius: number; charge: boolean }

interface ButtonView {
  def: ButtonDef;
  x: number; y: number;
  pointerId: number;
  heldSince: number;
  bg: Phaser.GameObjects.Graphics;
  ring: Phaser.GameObjects.Graphics;
  label: Phaser.GameObjects.Text;
}

const DEFS: ButtonDef[] = [
  { id: 'shot', label: 'TIRO', color: 0xe53935, radius: 46, charge: true },
  { id: 'pass', label: 'PASE', color: 0x1e88e5, radius: 40, charge: true },
  { id: 'lob', label: 'CENTRO', color: 0xfdd835, radius: 34, charge: true },
  { id: 'sprint', label: 'SPRINT', color: 0x43a047, radius: 34, charge: false },
];

/**
 * Botones contextuales a la derecha. Potencia por duración del toque con anillo visual.
 * Cada botón sigue a su propio puntero (multi-touch real).
 */
export class ActionButtons {
  private readonly views: ButtonView[] = [];
  private readonly maxHold: number;

  constructor(scene: Phaser.Scene, private readonly input: InputState, private readonly ui: number, maxHoldSeconds: number) {
    this.maxHold = maxHoldSeconds * 1000;
    for (const def of DEFS) {
      const bg = scene.add.graphics().setDepth(100);
      const ring = scene.add.graphics().setDepth(101);
      const label = scene.add.text(0, 0, def.label, {
        fontFamily: 'system-ui, -apple-system, Roboto, Arial, sans-serif', fontSize: `${Math.round(12 * ui)}px`,
        fontStyle: 'bold', color: '#ffffff',
      }).setOrigin(0.5).setDepth(102).setAlpha(0.9);
      this.views.push({ def, x: 0, y: 0, pointerId: -1, heldSince: 0, bg, ring, label });
    }
    scene.input.on(Phaser.Input.Events.POINTER_DOWN, this.onDown, this);
    scene.input.on(Phaser.Input.Events.POINTER_UP, this.onUp, this);
    scene.input.on(Phaser.Input.Events.GAME_OUT, this.onUp, this);
    scene.events.once(Phaser.Scenes.Events.SHUTDOWN, () => {
      scene.input.off(Phaser.Input.Events.POINTER_DOWN, this.onDown, this);
      scene.input.off(Phaser.Input.Events.POINTER_UP, this.onUp, this);
      scene.input.off(Phaser.Input.Events.GAME_OUT, this.onUp, this);
    });
  }

  /** Posiciona los botones respecto a la esquina inferior derecha útil (ya con safe area). */
  layout(right: number, bottom: number): void {
    const u = this.ui;
    const pos: Record<ButtonId, [number, number]> = {
      shot: [right - 64 * u, bottom - 64 * u],
      pass: [right - 150 * u, bottom - 44 * u],
      lob: [right - 118 * u, bottom - 138 * u],
      sprint: [right - 40 * u, bottom - 160 * u],
    };
    for (const v of this.views) {
      const p = pos[v.def.id];
      v.x = p[0]; v.y = p[1];
      v.bg.setPosition(v.x, v.y);
      v.ring.setPosition(v.x, v.y);
      v.label.setPosition(v.x, v.y);
      this.drawBg(v, false);
    }
  }

  private drawBg(v: ButtonView, pressed: boolean): void {
    const r = v.def.radius * this.ui;
    v.bg.clear();
    v.bg.fillStyle(v.def.color, pressed ? 0.75 : 0.42).fillCircle(0, 0, r);
    v.bg.lineStyle(2 * this.ui, 0xffffff, pressed ? 0.9 : 0.5).strokeCircle(0, 0, r);
  }

  private hit(v: ButtonView, x: number, y: number): boolean {
    const r = v.def.radius * this.ui * 1.15;
    return (x - v.x) ** 2 + (y - v.y) ** 2 <= r * r;
  }

  private onDown(p: Phaser.Input.Pointer): void {
    for (const v of this.views) {
      if (v.pointerId !== -1 || !this.hit(v, p.x, p.y)) continue;
      v.pointerId = p.id;
      v.heldSince = performance.now();
      stats.pendingInputStamp = v.heldSince;
      this.drawBg(v, true);
      this.setHeld(v.def.id, true);
      return;
    }
  }

  private onUp(p: Phaser.Input.Pointer): void {
    for (const v of this.views) {
      if (v.pointerId !== p.id) continue;
      v.pointerId = -1;
      this.drawBg(v, false);
      v.ring.clear();
      const power = Math.min(1, (performance.now() - v.heldSince) / this.maxHold);
      this.setHeld(v.def.id, false);
      if (v.def.charge) this.setRelease(v.def.id, Math.max(0.15, power));
      stats.pendingInputStamp = performance.now();
    }
  }

  private setHeld(id: ButtonId, held: boolean): void {
    if (id === 'shot') this.input.shotHeld = held;
    else if (id === 'pass') this.input.passHeld = held;
    else if (id === 'lob') this.input.lobHeld = held;
    else this.input.sprint = held;
  }

  private setRelease(id: ButtonId, power: number): void {
    if (id === 'shot') this.input.shotRelease = power;
    else if (id === 'pass') this.input.passRelease = power;
    else if (id === 'lob') this.input.lobRelease = power;
  }

  /** Dibuja el anillo de carga de los botones mantenidos. */
  update(): void {
    const now = performance.now();
    for (const v of this.views) {
      if (v.pointerId === -1 || !v.def.charge) continue;
      const power = Math.min(1, (now - v.heldSince) / this.maxHold);
      const r = v.def.radius * this.ui + 6 * this.ui;
      v.ring.clear();
      v.ring.lineStyle(5 * this.ui, 0xffffff, 0.95);
      v.ring.beginPath();
      v.ring.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * power, false);
      v.ring.strokePath();
    }
  }
}
