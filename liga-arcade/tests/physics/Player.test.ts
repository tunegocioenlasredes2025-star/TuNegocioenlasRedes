import { describe, it, expect } from 'vitest';
import { MatchSim, FIXED_DT } from '@core/match/MatchSim';
import { createInputState } from '@core/match/InputState';
import { TUNING } from '@core/Tuning';
import { PITCH, CENTER_X, CENTER_Y } from '@core/pitch/Pitch';

describe('PlayerBody + Possession', () => {
  it('acelera al instante y llega a velocidad máxima de carrera', () => {
    const sim = new MatchSim();
    const input = createInputState();
    input.moveX = 1;
    sim.step(input);
    expect(sim.player.speed()).toBeGreaterThan(0.3);
    for (let i = 0; i < 90; i++) sim.step(input);
    // Con pelota corre al factor withBall; sin pelota al runSpeed.
    const expected = sim.player.hasBall ? TUNING.player.runSpeed * TUNING.player.withBallSpeedFactor : TUNING.player.runSpeed;
    expect(sim.player.speed()).toBeCloseTo(expected, 1);
  });

  it('frena al soltar el joystick', () => {
    const sim = new MatchSim();
    const input = createInputState();
    input.moveX = 1;
    for (let i = 0; i < 60; i++) sim.step(input);
    input.moveX = 0;
    for (let i = 0; i < 60; i++) sim.step(input);
    expect(sim.player.speed()).toBe(0);
  });

  it('toma la pelota al pasar cerca y la conduce adelante del pie', () => {
    const sim = new MatchSim();
    const input = createInputState();
    input.moveX = 1;
    for (let i = 0; i < 60; i++) sim.step(input);
    expect(sim.player.hasBall).toBe(true);
    const d = sim.player.pos.distanceTo(sim.ball.pos);
    expect(d).toBeGreaterThan(0.2);
    expect(d).toBeLessThan(1);
    expect(sim.ball.pos.x).toBeGreaterThan(sim.player.pos.x);
  });

  it('un tiro con potencia máxima desde el centro termina en gol', () => {
    const sim = new MatchSim();
    const input = createInputState();
    input.moveX = 1;
    for (let i = 0; i < 60; i++) sim.step(input);
    expect(sim.player.hasBall).toBe(true);
    input.moveX = 0;
    input.shotRelease = 0.7;
    sim.step(input);
    expect(sim.events.some((e) => e.type === 'kick')).toBe(true);
    expect(sim.player.hasBall).toBe(false);
    let goal = false;
    for (let i = 0; i < 60 * 6 && !goal; i++) {
      sim.step(input);
      if (sim.events.some((e) => e.type === 'goal')) goal = true;
    }
    expect(goal).toBe(true);
    expect(sim.goals.home).toBe(1);
  });

  it('tras el gol reinicia en el centro', () => {
    const sim = new MatchSim();
    const input = createInputState();
    sim.ball.reset(PITCH.LENGTH + 0.5, CENTER_Y);
    sim.player.reset(80, 10);
    sim.step(input);
    expect(sim.goals.home).toBe(1);
    for (let i = 0; i < 60 * 3; i++) sim.step(input);
    expect(sim.ball.pos.x).toBeCloseTo(CENTER_X);
    expect(sim.ball.pos.y).toBeCloseTo(CENTER_Y);
    expect(sim.restartTimer).toBe(0);
  });

  it('es determinista: misma secuencia de input → mismo estado', () => {
    const play = () => {
      const sim = new MatchSim();
      const input = createInputState();
      for (let i = 0; i < 600; i++) {
        input.moveX = Math.sin(i / 20); input.moveY = Math.cos(i / 33); input.sprint = i % 100 < 40;
        if (i % 150 === 149) input.shotRelease = 0.8;
        sim.step(input);
      }
      return [sim.ball.pos.x, sim.ball.pos.y, sim.ball.z, sim.player.pos.x, sim.player.pos.y, sim.goals.home];
    };
    expect(play()).toEqual(play());
  });

  it(`el paso fijo es ${FIXED_DT}`, () => { expect(FIXED_DT).toBeCloseTo(1 / 60); });
});
