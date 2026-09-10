import Phaser from 'phaser';
import { generatePlayerAtlas, type KitColors } from '@game/render/PlayerSprites';
import { generateBallTexture } from '@game/render/BallSprite';

export const HOME_KIT: KitColors = {
  base: 0x0d47a1, accent: 0xffd600, shorts: 0x0d47a1, socks: 0xffd600, pattern: 'band', skin: 0xd9a066, hair: 0x2b1b0e,
};

/** Genera todas las texturas procedurales y arranca el partido. Sin assets externos. */
export class BootScene extends Phaser.Scene {
  constructor() { super('Boot'); }

  create(): void {
    generateBallTexture(this);
    generatePlayerAtlas(this, 'kit-home', HOME_KIT);
    this.scene.start('Match');
    this.scene.launch('Hud');
  }
}
