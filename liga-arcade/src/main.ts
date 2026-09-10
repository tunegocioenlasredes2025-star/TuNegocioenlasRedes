import Phaser from 'phaser';
import { BootScene } from '@game/scenes/BootScene';
import { MatchScene } from '@game/scenes/MatchScene';
import { HudScene } from '@game/scenes/HudScene';
import { DPR, stats } from '@game/state';
import { tryLockLandscape } from '@platform/Orientation';

performance.mark('liga-boot-start');

function viewport(): { w: number; h: number } {
  const vv = window.visualViewport;
  const w = Math.round((vv?.width ?? window.innerWidth));
  const h = Math.round((vv?.height ?? window.innerHeight));
  return { w, h };
}

const { w, h } = viewport();

const game = new Phaser.Game({
  type: Phaser.AUTO,
  parent: 'game',
  width: w * DPR,
  height: h * DPR,
  backgroundColor: '#0b1d0f',
  scale: { mode: Phaser.Scale.NONE, autoCenter: Phaser.Scale.NO_CENTER, zoom: 1 / DPR },
  render: { antialias: true, antialiasGL: true, roundPixels: false, powerPreference: 'high-performance', pixelArt: false },
  fps: { target: 60, min: 30, smoothStep: true },
  input: { activePointers: 4, touch: { capture: true } },
  disableContextMenu: true,
  banner: false,
  scene: [BootScene, MatchScene, HudScene],
});

function applyCanvasSize(): void {
  const v = viewport();
  game.scale.resize(v.w * DPR, v.h * DPR);
  const canvas = game.canvas;
  canvas.style.width = `${v.w}px`;
  canvas.style.height = `${v.h}px`;
}
window.addEventListener('resize', applyCanvasSize);
window.visualViewport?.addEventListener('resize', applyCanvasSize);
window.addEventListener('orientationchange', () => setTimeout(applyCanvasSize, 250));
applyCanvasSize();

void tryLockLandscape();

game.events.once('ready', () => {
  performance.mark('liga-boot-ready');
  stats.bootToMenuMs = performance.measure('liga-boot', 'liga-boot-start', 'liga-boot-ready').duration;
  document.getElementById('boot')?.remove();
});
