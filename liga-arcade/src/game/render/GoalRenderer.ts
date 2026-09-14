import Phaser from 'phaser';
import { PITCH, GOAL_TOP, GOAL_BOTTOM, type Side } from '@core/pitch/Pitch';
import { projectX, projectY } from './Projection';

const POST = 0xffffff;
const NET = 0xe8eef0;

/**
 * Arco proyectado: postes, travesaño y red como Graphics estáticos.
 * Devuelve dos capas: `back` (red y poste lejano, detrás de la pelota) y `front` (poste cercano
 * y travesaño, delante de todo lo que esté más arriba en la cancha).
 */
export function createGoal(scene: Phaser.Scene, side: Side): { back: Phaser.GameObjects.Graphics; front: Phaser.GameObjects.Graphics } {
  const lineX = side === 'home' ? 0 : PITCH.LENGTH;
  const outward = side === 'home' ? -1 : 1;
  const backX = lineX + outward * PITCH.GOAL_DEPTH;
  const H = PITCH.GOAL_HEIGHT;

  const back = scene.add.graphics();
  const front = scene.add.graphics();

  const P = (x: number, y: number, z: number): [number, number] => [projectX(x, y), projectY(y, z)];
  const line = (g: Phaser.GameObjects.Graphics, a: [number, number], b: [number, number]): void => {
    g.beginPath(); g.moveTo(a[0], a[1]); g.lineTo(b[0], b[1]); g.strokePath();
  };

  // Red: malla (líneas verticales y horizontales) en el techo, el fondo y los laterales.
  back.lineStyle(1, NET, 0.45);
  const cols = 8, rows = 4, depthSteps = 3;
  // Fondo (plano x = backX).
  for (let i = 0; i <= cols; i++) {
    const y = GOAL_TOP + ((GOAL_BOTTOM - GOAL_TOP) * i) / cols;
    line(back, P(backX, y, 0), P(backX, y, H));
  }
  for (let j = 0; j <= rows; j++) {
    const z = (H * j) / rows;
    line(back, P(backX, GOAL_TOP, z), P(backX, GOAL_BOTTOM, z));
  }
  // Techo (plano z = H) y piso.
  for (let i = 0; i <= cols; i++) {
    const y = GOAL_TOP + ((GOAL_BOTTOM - GOAL_TOP) * i) / cols;
    line(back, P(lineX, y, H), P(backX, y, H));
  }
  for (let d = 1; d <= depthSteps; d++) {
    const x = lineX + (outward * PITCH.GOAL_DEPTH * d) / depthSteps;
    line(back, P(x, GOAL_TOP, H), P(x, GOAL_BOTTOM, H));
  }
  // Laterales (planos y = GOAL_TOP y y = GOAL_BOTTOM).
  for (const y of [GOAL_TOP, GOAL_BOTTOM]) {
    for (let j = 0; j <= rows; j++) {
      const z = (H * j) / rows;
      line(back, P(lineX, y, z), P(backX, y, z));
    }
    for (let d = 1; d <= depthSteps; d++) {
      const x = lineX + (outward * PITCH.GOAL_DEPTH * d) / depthSteps;
      line(back, P(x, y, 0), P(x, y, H));
    }
  }
  // Postes traseros.
  back.lineStyle(3, POST, 1);
  line(back, P(backX, GOAL_TOP, 0), P(backX, GOAL_TOP, H));
  line(back, P(backX, GOAL_BOTTOM, 0), P(backX, GOAL_BOTTOM, H));
  line(back, P(backX, GOAL_TOP, H), P(backX, GOAL_BOTTOM, H));
  // Poste lejano (arriba en pantalla) va detrás.
  back.lineStyle(4, POST, 1);
  line(back, P(lineX, GOAL_TOP, 0), P(lineX, GOAL_TOP, H));
  line(back, P(lineX, GOAL_TOP, H), P(backX, GOAL_TOP, H));

  // Poste cercano + travesaño: delante.
  front.lineStyle(4, POST, 1);
  line(front, P(lineX, GOAL_BOTTOM, 0), P(lineX, GOAL_BOTTOM, H));
  line(front, P(lineX, GOAL_TOP, H), P(lineX, GOAL_BOTTOM, H));
  line(front, P(lineX, GOAL_BOTTOM, H), P(backX, GOAL_BOTTOM, H));

  back.setDepth(projectY(GOAL_TOP) - 1);
  front.setDepth(projectY(GOAL_BOTTOM) + 1);
  return { back, front };
}
