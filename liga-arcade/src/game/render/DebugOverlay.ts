import Phaser from 'phaser';
import { stats } from '@game/state';

/** Overlay de rendimiento: FPS promedio y 1% bajo, ms de simulación, draw calls, latencia de input, memoria. */
export class DebugOverlay {
  private readonly text: Phaser.GameObjects.Text;
  private readonly frames: number[] = [];
  private lastUpdate = 0;
  private latencySamples: number[] = [];

  constructor(scene: Phaser.Scene, ui: number, x: number, y: number) {
    this.text = scene.add.text(x, y, '', {
      fontFamily: 'ui-monospace, Menlo, Consolas, monospace', fontSize: `${Math.round(11 * ui)}px`, color: '#c8ffd0',
      backgroundColor: 'rgba(0,0,0,0.55)', padding: { x: 6 * ui, y: 4 * ui },
    }).setDepth(500).setVisible(false);
  }

  setVisible(v: boolean): void { this.text.setVisible(v); stats.overlayVisible = v; }
  toggle(): void { this.setVisible(!this.text.visible); }
  setPosition(x: number, y: number): void { this.text.setPosition(x, y); }

  recordLatency(ms: number): void {
    this.latencySamples.push(ms);
    if (this.latencySamples.length > 30) this.latencySamples.shift();
    stats.inputLatencyMs = ms;
    stats.inputLatencyAvgMs = this.latencySamples.reduce((a, b) => a + b, 0) / this.latencySamples.length;
  }

  update(game: Phaser.Game, deltaMs: number): void {
    this.frames.push(deltaMs);
    if (this.frames.length > 120) this.frames.shift();
    const now = performance.now();
    if (now - this.lastUpdate < 250) return;
    this.lastUpdate = now;
    const sorted = [...this.frames].sort((a, b) => b - a);
    const avg = this.frames.reduce((a, b) => a + b, 0) / this.frames.length;
    const worst = sorted[Math.floor(sorted.length * 0.01)] ?? avg;
    stats.fps = 1000 / avg;
    stats.fpsLow = 1000 / worst;
    stats.frameMs = avg;
    let objects = 0;
    for (const s of game.scene.getScenes(true)) objects += s.children.length;
    stats.drawCalls = objects;
    const mem = (performance as Performance & { memory?: { usedJSHeapSize: number } }).memory;
    if (!this.text.visible) return;
    const lines = [
      `FPS ${stats.fps.toFixed(0)}  1%low ${stats.fpsLow.toFixed(0)}  frame ${stats.frameMs.toFixed(1)}ms`,
      `sim ${stats.simMs.toFixed(2)}ms  objs ${stats.drawCalls}  ${game.renderer.type === Phaser.WEBGL ? 'WebGL' : 'Canvas'}`,
      `input ${stats.inputLatencyMs.toFixed(0)}ms (avg ${stats.inputLatencyAvgMs.toFixed(0)})  boot ${stats.bootToMenuMs.toFixed(0)}ms`,
      `${game.scale.width}x${game.scale.height}${mem ? `  heap ${(mem.usedJSHeapSize / 1048576).toFixed(0)}MB` : ''}`,
    ];
    this.text.setText(lines);
  }
}
