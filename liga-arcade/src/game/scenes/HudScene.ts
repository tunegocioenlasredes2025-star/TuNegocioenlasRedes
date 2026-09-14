import Phaser from 'phaser';
import { VirtualJoystick } from '@game/input/VirtualJoystick';
import { ActionButtons } from '@game/input/ActionButtons';
import { DebugOverlay } from '@game/render/DebugOverlay';
import { TUNING } from '@core/Tuning';
import { input, DPR } from '@game/state';
import { readSafeInsets } from '@platform/SafeArea';

/** HUD: joystick, botones, marcador, cartel de gol y overlay de stats. Corre sobre la escena Match. */
export class HudScene extends Phaser.Scene {
  private joystick!: VirtualJoystick;
  private buttons!: ActionButtons;
  private overlay!: DebugOverlay;
  private score!: Phaser.GameObjects.Text;
  private banner!: Phaser.GameObjects.Text;
  private fpsToggle!: Phaser.GameObjects.Text;

  constructor() { super('Hud'); }

  create(): void {
    const ui = DPR;
    this.joystick = new VirtualJoystick(this, { zone: new Phaser.Geom.Rectangle(0, 0, 1, 1), radius: 58 * ui, deadZone: 0.12 }, input);
    this.buttons = new ActionButtons(this, input, ui, TUNING.kick.maxHoldSeconds);
    this.overlay = new DebugOverlay(this, ui, 0, 0);

    this.score = this.add.text(0, 0, '0 - 0', {
      fontFamily: 'system-ui, -apple-system, Roboto, Arial, sans-serif', fontSize: `${Math.round(18 * ui)}px`, fontStyle: 'bold',
      color: '#ffffff', backgroundColor: 'rgba(0,0,0,0.45)', padding: { x: 10 * ui, y: 4 * ui },
    }).setOrigin(0.5, 0).setDepth(200);

    this.banner = this.add.text(0, 0, '¡GOL!', {
      fontFamily: 'system-ui, -apple-system, Roboto, Arial, sans-serif', fontSize: `${Math.round(56 * ui)}px`, fontStyle: '900',
      color: '#ffffff', stroke: '#c62828', strokeThickness: 8 * ui,
    }).setOrigin(0.5).setDepth(300).setVisible(false);

    this.fpsToggle = this.add.text(0, 0, 'FPS', {
      fontFamily: 'system-ui, -apple-system, Roboto, Arial, sans-serif', fontSize: `${Math.round(10 * ui)}px`,
      color: '#9fd3ac', backgroundColor: 'rgba(0,0,0,0.35)', padding: { x: 6 * ui, y: 3 * ui },
    }).setOrigin(0, 0).setDepth(250).setInteractive({ useHandCursor: true });
    this.fpsToggle.on(Phaser.Input.Events.POINTER_DOWN, () => this.overlay.toggle());
    if (new URLSearchParams(location.search).has('stats')) this.overlay.setVisible(true);

    this.layout();
    this.scale.on(Phaser.Scale.Events.RESIZE, this.layout, this);
    this.game.events.on('goal', this.onGoal, this);
    this.game.events.on('out', this.onOut, this);
    this.game.events.on('input-latency', (ms: number) => this.overlay.recordLatency(ms));
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, () => {
      this.scale.off(Phaser.Scale.Events.RESIZE, this.layout, this);
      this.game.events.off('goal', this.onGoal, this);
      this.game.events.off('out', this.onOut, this);
    });
  }

  private layout(): void {
    const ui = DPR;
    const w = this.scale.width, h = this.scale.height;
    const s = readSafeInsets();
    const left = s.left * ui, right = w - s.right * ui, top = s.top * ui, bottom = h - s.bottom * ui;
    this.cameras.main.setViewport(0, 0, w, h);
    this.joystick.setZone(new Phaser.Geom.Rectangle(left, top, (right - left) * 0.5, bottom - top));
    this.buttons.layout(right, bottom);
    this.score.setPosition((left + right) / 2, top + 8 * ui);
    this.banner.setPosition((left + right) / 2, (top + bottom) / 2);
    this.fpsToggle.setPosition(left + 8 * ui, top + 8 * ui);
    this.overlay.setPosition(left + 8 * ui, top + 30 * ui);
  }

  private onGoal(goals: { home: number; away: number }): void {
    this.score.setText(`${goals.home} - ${goals.away}`);
    this.banner.setText('¡GOL!').setVisible(true).setScale(0.4).setAlpha(1);
    this.tweens.add({ targets: this.banner, scale: 1, duration: 260, ease: 'Back.Out' });
    this.tweens.add({ targets: this.banner, alpha: 0, delay: 1700, duration: 400, onComplete: () => this.banner.setVisible(false) });
  }

  private onOut(): void {
    this.banner.setText('AFUERA').setVisible(true).setScale(1).setAlpha(1);
    this.tweens.add({ targets: this.banner, alpha: 0, delay: 500, duration: 300, onComplete: () => this.banner.setVisible(false) });
  }

  override update(_t: number, delta: number): void {
    this.buttons.update();
    this.overlay.update(this.game, delta);
  }
}
