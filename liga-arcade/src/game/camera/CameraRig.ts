import Phaser from 'phaser';
import type { CameraTuning } from '@core/Tuning';
import { damp, clamp } from '@core/math/scalar';
import { projectX, projectY, cameraBounds } from '@game/render/Projection';

/** Sigue la pelota con anticipación según su velocidad; zoom suave según la acción. */
export class CameraRig {
  private x = 0;
  private y = 0;
  private zoom: number;
  private shake = 0;

  constructor(private readonly cam: Phaser.Cameras.Scene2D.Camera, private readonly t: CameraTuning, private readonly dpr: number) {
    const b = cameraBounds();
    cam.setBounds(b.x, b.y, b.width, b.height);
    this.zoom = t.zoomMin;
    cam.setZoom(this.zoom * dpr);
  }

  snapTo(bx: number, by: number): void {
    this.x = projectX(bx, by); this.y = projectY(by, 0);
    this.cam.centerOn(this.x, this.y);
  }

  kick(strength: number): void { this.shake = Math.min(1, this.shake + strength); }

  update(bx: number, by: number, bz: number, vx: number, vy: number, dt: number): void {
    const speed = Math.hypot(vx, vy);
    const ahead = Math.min(1, speed / 25) * this.t.lookAhead;
    const tx = projectX(bx + (speed > 0 ? (vx / speed) * ahead : 0), by);
    const ty = projectY(by + (speed > 0 ? (vy / speed) * ahead * 0.6 : 0), bz * 0.5);
    this.x = damp(this.x, tx, this.t.followLambda, dt);
    this.y = damp(this.y, ty, this.t.followLambda, dt);
    // Más zoom cuando la pelota va lenta o está alta; menos cuando corre rápido.
    const targetZoom = clamp(this.t.zoomMax - (speed / 30) * (this.t.zoomMax - this.t.zoomMin), this.t.zoomMin, this.t.zoomMax);
    this.zoom = damp(this.zoom, targetZoom, 2.5, dt);
    this.cam.setZoom(this.zoom * this.dpr);
    let ox = 0, oy = 0;
    if (this.shake > 0) {
      ox = (Math.random() - 0.5) * 8 * this.shake; oy = (Math.random() - 0.5) * 8 * this.shake;
      this.shake = Math.max(0, this.shake - dt * 4);
    }
    this.cam.centerOn(this.x + ox, this.y + oy);
  }
}
