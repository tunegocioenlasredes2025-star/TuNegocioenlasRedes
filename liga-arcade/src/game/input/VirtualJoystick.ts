import Phaser from 'phaser';
import type { InputState } from '@core/match/InputState';

export interface JoystickOptions {
  /** Zona de la pantalla donde puede nacer (en px de juego). */
  zone: Phaser.Geom.Rectangle;
  radius: number;
  deadZone: number;
}

/**
 * Joystick flotante: nace donde apoya el dedo, la perilla sigue al dedo y la base se arrastra
 * si el dedo se aleja más del radio (para que nunca "se trabe" en un extremo).
 * Escribe directo en `InputState` en cada evento: cero latencia agregada.
 */
export class VirtualJoystick {
  private pointerId = -1;
  private readonly base: Phaser.GameObjects.Graphics;
  private readonly knob: Phaser.GameObjects.Graphics;
  private baseX = 0;
  private baseY = 0;

  constructor(scene: Phaser.Scene, private readonly opts: JoystickOptions, private readonly input: InputState) {
    this.base = scene.add.graphics().setDepth(100).setVisible(false);
    this.knob = scene.add.graphics().setDepth(101).setVisible(false);
    this.drawBase();
    this.drawKnob();

    scene.input.on(Phaser.Input.Events.POINTER_DOWN, this.onDown, this);
    scene.input.on(Phaser.Input.Events.POINTER_MOVE, this.onMove, this);
    scene.input.on(Phaser.Input.Events.POINTER_UP, this.onUp, this);
    scene.input.on(Phaser.Input.Events.GAME_OUT, this.onUp, this);
    scene.events.once(Phaser.Scenes.Events.SHUTDOWN, () => {
      scene.input.off(Phaser.Input.Events.POINTER_DOWN, this.onDown, this);
      scene.input.off(Phaser.Input.Events.POINTER_MOVE, this.onMove, this);
      scene.input.off(Phaser.Input.Events.POINTER_UP, this.onUp, this);
      scene.input.off(Phaser.Input.Events.GAME_OUT, this.onUp, this);
    });
  }

  setZone(zone: Phaser.Geom.Rectangle): void { this.opts.zone = zone; }
  isActive(): boolean { return this.pointerId !== -1; }

  private drawBase(): void {
    const r = this.opts.radius;
    this.base.clear();
    this.base.fillStyle(0xffffff, 0.10).fillCircle(0, 0, r);
    this.base.lineStyle(2, 0xffffff, 0.35).strokeCircle(0, 0, r);
  }
  private drawKnob(): void {
    const r = this.opts.radius * 0.42;
    this.knob.clear();
    this.knob.fillStyle(0xffffff, 0.55).fillCircle(0, 0, r);
    this.knob.lineStyle(2, 0xffffff, 0.8).strokeCircle(0, 0, r);
  }

  private onDown(p: Phaser.Input.Pointer): void {
    if (this.pointerId !== -1) return;
    if (!Phaser.Geom.Rectangle.Contains(this.opts.zone, p.x, p.y)) return;
    this.pointerId = p.id;
    this.baseX = p.x; this.baseY = p.y;
    this.base.setPosition(p.x, p.y).setVisible(true);
    this.knob.setPosition(p.x, p.y).setVisible(true);
    this.input.moveX = 0; this.input.moveY = 0;
  }

  private onMove(p: Phaser.Input.Pointer): void {
    if (p.id !== this.pointerId) return;
    let dx = p.x - this.baseX, dy = p.y - this.baseY;
    const r = this.opts.radius;
    const d = Math.hypot(dx, dy);
    if (d > r) {
      // La base sigue al dedo para que el cambio de dirección sea inmediato.
      const k = (d - r) / d;
      this.baseX += dx * k; this.baseY += dy * k;
      dx = p.x - this.baseX; dy = p.y - this.baseY;
      this.base.setPosition(this.baseX, this.baseY);
    }
    this.knob.setPosition(this.baseX + dx, this.baseY + dy);
    const mag = Math.min(1, Math.hypot(dx, dy) / r);
    if (mag < this.opts.deadZone) { this.input.moveX = 0; this.input.moveY = 0; return; }
    // Re-mapea la zona muerta para que 0 empiece justo después de ella.
    const m = (mag - this.opts.deadZone) / (1 - this.opts.deadZone);
    const a = Math.atan2(dy, dx);
    this.input.moveX = Math.cos(a) * m;
    this.input.moveY = Math.sin(a) * m;
  }

  private onUp(p: Phaser.Input.Pointer): void {
    if (p.id !== this.pointerId) return;
    this.pointerId = -1;
    this.base.setVisible(false);
    this.knob.setVisible(false);
    this.input.moveX = 0; this.input.moveY = 0;
  }
}
