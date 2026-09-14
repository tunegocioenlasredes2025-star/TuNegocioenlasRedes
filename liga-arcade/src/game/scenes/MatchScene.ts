import Phaser from 'phaser';
import { MatchSim, FIXED_DT, type SimEvent } from '@core/match/MatchSim';
import { TUNING } from '@core/Tuning';
import { CENTER_X, CENTER_Y, PITCH } from '@core/pitch/Pitch';
import { createPitch } from '@game/render/PitchRenderer';
import { createGoal } from '@game/render/GoalRenderer';
import { BallView } from '@game/render/BallSprite';
import { frameName, dirIndex, FRAME_H, FOOT_Y, RUN_FRAMES, type Anim } from '@game/render/PlayerSprites';
import { projectX, projectY, sizeAt } from '@game/render/Projection';
import { CameraRig } from '@game/camera/CameraRig';
import { input, stats, DPR } from '@game/state';

/** Altura visual del jugador en metros (un poco exagerada para lectura). */
const PLAYER_HEIGHT_M = 2.1;
const MAX_STEPS_PER_FRAME = 4;

export class MatchScene extends Phaser.Scene {
  private sim!: MatchSim;
  private ballView!: BallView;
  private player!: Phaser.GameObjects.Image;
  private playerShadow!: Phaser.GameObjects.Image;
  private rig!: CameraRig;
  private accumulator = 0;
  // Estado previo para interpolar el render entre ticks.
  private prevBall = { x: 0, y: 0, z: 0 };
  private prevPlayer = { x: 0, y: 0 };
  private runPhase = 0;
  private kickTimer = 0;
  private lastFacingDir = 0;

  constructor() { super('Match'); }

  create(): void {
    this.sim = new MatchSim(TUNING);
    createPitch(this);
    createGoal(this, 'home');
    createGoal(this, 'away');
    this.ballView = new BallView(this);
    this.playerShadow = this.add.image(0, 0, 'ball-shadow').setAlpha(0.3);
    this.player = this.add.image(0, 0, 'kit-home', frameName('kit-home', 0, 'idle', 0)).setOrigin(0.5, FOOT_Y / FRAME_H);
    this.rig = new CameraRig(this.cameras.main, TUNING.camera, DPR);
    this.rig.snapTo(CENTER_X, CENTER_Y);
    this.snapshot();

    this.game.events.on(Phaser.Core.Events.POST_RENDER, this.onPostRender, this);
    this.events.once(Phaser.Scenes.Events.SHUTDOWN, () => this.game.events.off(Phaser.Core.Events.POST_RENDER, this.onPostRender, this));
  }

  getSim(): MatchSim { return this.sim; }

  private snapshot(): void {
    const b = this.sim.ball, p = this.sim.player;
    this.prevBall.x = b.pos.x; this.prevBall.y = b.pos.y; this.prevBall.z = b.z;
    this.prevPlayer.x = p.pos.x; this.prevPlayer.y = p.pos.y;
  }

  override update(_time: number, deltaMs: number): void {
    const dt = Math.min(deltaMs / 1000, 0.1);
    this.accumulator += dt;
    let steps = 0;
    const t0 = performance.now();
    while (this.accumulator >= FIXED_DT && steps < MAX_STEPS_PER_FRAME) {
      this.snapshot();
      this.sim.step(input, FIXED_DT);
      this.handleEvents(this.sim.events);
      this.accumulator -= FIXED_DT;
      steps++;
    }
    if (steps === MAX_STEPS_PER_FRAME) this.accumulator = 0; // evitar espiral de la muerte
    stats.simMs = steps > 0 ? (performance.now() - t0) / steps : stats.simMs;

    const alpha = this.accumulator / FIXED_DT;
    this.render(alpha, dt);
  }

  private handleEvents(events: SimEvent[]): void {
    for (const e of events) {
      if (e.type === 'kick') { this.kickTimer = 0.22; this.rig.kick(e.power * 0.25); }
      else if (e.type === 'post' || e.type === 'bar') this.rig.kick(0.5);
      else if (e.type === 'goal') this.game.events.emit('goal', this.sim.goals);
      else if (e.type === 'out') this.game.events.emit('out');
    }
  }

  private render(alpha: number, dt: number): void {
    const b = this.sim.ball, p = this.sim.player;
    const bx = this.prevBall.x + (b.pos.x - this.prevBall.x) * alpha;
    const by = this.prevBall.y + (b.pos.y - this.prevBall.y) * alpha;
    const bz = this.prevBall.z + (b.z - this.prevBall.z) * alpha;
    const px = this.prevPlayer.x + (p.pos.x - this.prevPlayer.x) * alpha;
    const py = this.prevPlayer.y + (p.pos.y - this.prevPlayer.y) * alpha;

    this.ballView.update(b, bx, by, bz, dt);

    // Jugador: frame según dirección y animación.
    const speed = p.speed();
    let anim: Anim = 'idle';
    let frame = 0;
    if (this.kickTimer > 0) {
      this.kickTimer -= dt;
      anim = 'kick'; frame = this.kickTimer > 0.12 ? 0 : 1;
    } else if (speed > 0.4) {
      anim = 'run';
      this.runPhase += dt * (speed / TUNING.player.runSpeed) * 9;
      frame = Math.floor(this.runPhase) % RUN_FRAMES;
    } else {
      this.runPhase = 0;
    }
    const dir = speed > 0.4 || this.kickTimer > 0 ? dirIndex(p.facing) : this.lastFacingDir;
    this.lastFacingDir = dir;
    this.player.setFrame(frameName('kit-home', dir, anim, frame));

    const sx = projectX(px, py);
    const ground = projectY(py, 0);
    const scale = sizeAt(py, PLAYER_HEIGHT_M) / FRAME_H;
    this.player.setPosition(sx, ground).setScale(scale).setDepth(ground);
    this.playerShadow.setPosition(sx, ground + 1).setScale(scale * 1.1, scale * 0.9).setDepth(ground - 0.6);

    this.rig.update(bx, by, bz, b.vel.x, b.vel.y, dt);
  }

  private onPostRender(): void {
    if (stats.pendingInputStamp >= 0) {
      const latency = performance.now() - stats.pendingInputStamp;
      stats.pendingInputStamp = -1;
      this.game.events.emit('input-latency', latency);
    }
  }

  /** Para tests de humo: coordenadas de la pelota. */
  ballWorld(): { x: number; y: number; z: number } { return { x: this.sim.ball.pos.x, y: this.sim.ball.pos.y, z: this.sim.ball.z }; }
  pitchLength(): number { return PITCH.LENGTH; }
}
