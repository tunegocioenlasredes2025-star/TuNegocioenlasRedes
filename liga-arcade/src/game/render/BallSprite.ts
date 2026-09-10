import Phaser from 'phaser';
import type { Ball } from '@core/physics/Ball';
import { projectX, projectY, sizeAt } from './Projection';

export const BALL_TEX = 'ball';
const TEX_SIZE = 40;
/** Diámetro visual de la pelota en metros (exagerado para lectura en pantalla chica). */
const BALL_VISUAL_M = 0.6;

export function generateBallTexture(scene: Phaser.Scene): void {
  if (scene.textures.exists(BALL_TEX)) return;
  const g = scene.add.graphics();
  g.setVisible(false);
  const c = TEX_SIZE / 2, r = TEX_SIZE / 2 - 1;
  g.fillStyle(0xffffff, 1);
  g.fillCircle(c, c, r);
  g.fillStyle(0x1e1e22, 1);
  const patches: Array<[number, number]> = [[0, 0], [0.62, 0.05], [-0.6, 0.1], [0.2, 0.62], [-0.25, 0.6], [0.22, -0.6], [-0.2, -0.62]];
  for (const [px, py] of patches) g.fillCircle(c + px * r, c + py * r, r * 0.2);
  g.lineStyle(2, 0x2a2a2e, 1);
  g.strokeCircle(c, c, r - 1);
  g.generateTexture(BALL_TEX, TEX_SIZE, TEX_SIZE);
  g.destroy();

  const s = scene.add.graphics();
  s.setVisible(false);
  s.fillStyle(0x000000, 1);
  s.fillEllipse(TEX_SIZE / 2, TEX_SIZE / 2, TEX_SIZE - 2, (TEX_SIZE - 2) * 0.55);
  s.generateTexture('ball-shadow', TEX_SIZE, TEX_SIZE);
  s.destroy();
}

/** Pelota + sombra proyectadas. La sombra queda en el piso; la pelota sube con z. */
export class BallView {
  readonly sprite: Phaser.GameObjects.Image;
  readonly shadow: Phaser.GameObjects.Image;
  private roll = 0;

  constructor(scene: Phaser.Scene) {
    this.shadow = scene.add.image(0, 0, 'ball-shadow').setAlpha(0.35);
    this.sprite = scene.add.image(0, 0, BALL_TEX);
  }

  /** @param ix,iy,iz posición interpolada para render. */
  update(ball: Ball, ix: number, iy: number, iz: number, dt: number): void {
    const sx = projectX(ix, iy);
    const ground = projectY(iy, 0);
    const top = projectY(iy, iz);
    const px = sizeAt(iy, BALL_VISUAL_M);
    const scale = px / TEX_SIZE;

    this.shadow.setPosition(sx, ground);
    const shadowScale = scale * Math.max(0.55, 1 - iz * 0.12);
    this.shadow.setScale(shadowScale);
    this.shadow.setAlpha(Math.max(0.12, 0.38 - iz * 0.05));
    this.shadow.setDepth(ground - 0.5);

    this.sprite.setPosition(sx, top - px * 0.5);
    this.sprite.setScale(scale * (1 + Math.min(iz, 4) * 0.04));
    this.sprite.setDepth(ground + 0.4);

    // Rotación acorde a la velocidad para que se lea que rueda.
    const speed = ball.speed();
    this.roll += speed * dt * 2.2 * Math.sign(ball.vel.x || 1);
    this.sprite.setRotation(this.roll);
  }
}
