# Liga Arcade

Juego de fútbol arcade 2.5D para celular. TypeScript + Phaser 3.90 + Vite; Capacitor para Android; PWA para iPhone.

## Comandos

```bash
npm install          # una vez
npm run dev          # servidor local en http://localhost:5173/juego/
npm run check        # tsc + vitest + build (lo que corre CI)
npm run build        # build web → ../juego/ (lo que sirve Vercel en /juego)
npm run smoke        # abre la build en Chromium headless con viewport de iPhone, juega y saca capturas en smoke-out/
BASE_PATH=/ OUT_DIR=www npm run build && npx cap sync android   # build para el APK
```

## Cómo se publica

- **iPhone (PWA)**: la carpeta `juego/` en la raíz del repo se despliega con el sitio en Vercel.
  Abrir `https://tunegocioenlasredes.com/juego` en Safari → Compartir → "Agregar a inicio". Funciona offline.
- **Android (APK)**: el workflow `.github/workflows/liga-arcade-android.yml` compila `app-debug.apk` en cada push
  y lo deja como artifact en la pestaña Actions.

## Estructura

- `src/core/` lógica pura (física, reglas, IA). No importa Phaser. Se testea con Vitest.
- `src/game/` presentación Phaser: escenas, render 2.5D, input táctil, cámara.
- `src/platform/` puente con el dispositivo (safe areas, orientación, guardado).
- `data/` todo el contenido y las constantes de ajuste (`tuning.json`).
- `tests/` espejo de `src/core`.

`?stats` en la URL (o tocar "FPS" arriba a la izquierda) muestra el overlay de rendimiento.
