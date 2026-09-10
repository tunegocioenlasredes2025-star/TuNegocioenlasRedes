# Liga Arcade — PLAN de arquitectura

> Estado: **BORRADOR, pendiente de aprobación.** Escrito antes de la primera línea de
> código. Cada punto marcado con `[SUPUESTO n]` depende de una de las preguntas
> abiertas listadas al final; si cambiás la respuesta, cambio el plan.

---

## 1. Resumen en una línea

Juego de fútbol arcade 2.5D (11v11, liga argentina ficticia, 1v1 local y vs CPU)
hecho en TypeScript estricto + Phaser 3.90 + Vite, empaquetado con Capacitor 8 a un
APK Android, 100% offline, con la física de la pelota como núcleo del diseño.

---

## 2. Stack y versiones fijadas

| Pieza | Versión | Motivo |
|---|---|---|
| TypeScript | 5.x, `strict: true`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes` | Errores en compilación, no en el celu |
| Phaser | **3.90.0** (última 3.x estable; Phaser 4 queda fuera, pediste 3) | Render WebGL con fallback Canvas, input, escenas |
| Vite | 7.x | Dev server + bundle con tree-shaking; target `es2020` |
| Capacitor | 8.x (`@capacitor/core`, `@capacitor/android`, `@capacitor/preferences`, `@capacitor/haptics`, `@capacitor/screen-orientation`, `@capacitor/status-bar`) | Empaquetado nativo. Solo plugins oficiales, todos livianos |
| Vitest | 5.x | Tests de lógica pura (sin Phaser) |
| Node | 22 LTS | Build local y en CI |
| Android | minSdk 24 (Android 7), target 35 | Requisito de Capacitor 8; cubre gama media desde 2016 |

**No se usa**: Matter.js, Box2D, ECS externos, UI frameworks, librerías de
animación, ni assets con licencia. Física custom sobre Arcade solo para colisiones
2D triviales (jugador–jugador); la pelota tiene su propio integrador con eje Z.

---

## 3. Ubicación en el repo `[SUPUESTO 1]`

El repo actual es el sitio de la agencia (HTML estático desplegado en Vercel). El
juego vive en **`liga-arcade/`** como proyecto Node independiente, aislado del sitio:

- `.vercelignore` excluye `liga-arcade/` para que Vercel no lo publique ni lo builde.
- `.gitignore` raíz suma `liga-arcade/node_modules`, `liga-arcade/dist`, y los
  intermedios de Gradle dentro de `liga-arcade/android/`.
- La carpeta `liga-arcade/android/` (generada por Capacitor) **se commitea**: es lo
  que compila el APK en CI y donde se ajustan manifest, orientación y safe areas.

Si preferís un repo nuevo, el plan es idéntico moviendo la carpeta a la raíz.

---

## 4. Cómo llega el APK a tu celular `[SUPUESTO 2]`

Este entorno no tiene Android SDK, así que el APK **no se compila acá**. Propuesta:

1. **GitHub Actions** (`.github/workflows/android-apk.yml`): en cada push a la rama
   del juego corre `npm ci → vitest → tsc → vite build → cap sync → gradlew
   assembleDebug` y sube `liga-arcade-debug.apk` como artifact.
2. Vos abrís la pestaña *Actions* del repo desde el celular, bajás el artifact y lo
   instalás (hay que permitir "orígenes desconocidos" una sola vez).
3. En Fase 4 agrego build **release firmado** con keystore guardado en GitHub
   Secrets, para que el APK se pueda actualizar sin desinstalar.

Alternativa complementaria para iterar más rápido en Fase 1: publicar la build web
en `https://tunegocioenlasredes.com/liga-arcade/` (Chrome en el celu). El WebView
de Capacitor **es** Chrome, así que la sensación de control es representativa; lo
que no se puede probar así es el bloqueo de orientación, pantalla completa y haptics.

---

## 5. Estructura de carpetas

```
liga-arcade/
├── package.json  vite.config.ts  tsconfig.json  vitest.config.ts  capacitor.config.ts
├── index.html                      # único HTML; meta viewport-fit=cover
├── data/                           # TODO el contenido sale de acá, nada hardcodeado
│   ├── teams.json                  # 28 equipos: nombre, corto, ciudad, colores, kit, escudo, plantel
│   ├── formations.json             # 4-4-2, 4-3-3, 3-5-2, 4-2-3-1 con roles y posiciones base
│   ├── names.json                  # nombres y apellidos para el generador
│   └── tuning.json                 # constantes de física e IA (editables sin recompilar)
├── src/
│   ├── main.ts                     # crea el Phaser.Game y registra escenas
│   ├── core/                       # LÓGICA PURA. Cero imports de Phaser. 100% testeable.
│   │   ├── math/                   # Vec2, Vec3, clamp, lerp, ángulos, RNG seedable
│   │   ├── pitch/                  # dimensiones en metros, áreas, arcos, líneas
│   │   ├── physics/
│   │   │   ├── Ball.ts             # estado (x,y,z,vx,vy,vz,spin), integrador, rebotes, fricción, efecto
│   │   │   ├── Kick.ts             # potencia+tipo de toque → impulso (velocidad, elevación, spin)
│   │   │   ├── Collisions.ts       # pelota vs suelo/postes/travesaño/red/jugadores
│   │   │   └── PlayerBody.ts       # movimiento del jugador: aceleración, tope de velocidad, inercia
│   │   ├── match/
│   │   │   ├── MatchState.ts       # snapshot serializable: 22 jugadores + pelota + reloj + marcador
│   │   │   ├── MatchSim.ts         # tick fijo a 60 Hz: input → IA → física → reglas
│   │   │   ├── Possession.ts       # quién tiene la pelota, control, gambeta, intercepción
│   │   │   └── Clock.ts            # tiempo de partido, mitades, descuento
│   │   ├── rules/
│   │   │   ├── Referee.ts          # máquina de estados: EN_JUEGO, SAQUE_ARCO, CORNER, LATERAL, TIRO_LIBRE, PENAL, SAQUE_INICIAL
│   │   │   ├── Offside.ts          # línea de offside al momento del pase; activable
│   │   │   ├── Fouls.ts            # barridas: limpia / falta / amarilla / roja según ángulo, timing y zona
│   │   │   └── Penalties.ts        # tanda: alternancia, muerte súbita
│   │   ├── ai/
│   │   │   ├── TeamBrain.ts        # decisiones colectivas: línea defensiva, presión, fase (ataque/defensa/transición)
│   │   │   ├── PlayerBrain.ts      # FSM por jugador: MARCAR, CUBRIR, DESMARCAR, PRESIONAR, IR_AL_BALON, VOLVER_A_POSICION, ARQUERO_*
│   │   │   ├── roles/              # comportamiento por rol: GK, CB, FB, DM, CM, AM, W, ST
│   │   │   ├── Difficulty.ts       # 4 niveles: tiempo de reacción, error de pase/tiro, agresividad, frecuencia de decisión
│   │   │   └── Formation.ts        # posición ideal según fase y posición de la pelota (offset elástico)
│   │   ├── competition/
│   │   │   ├── League.ts           # fixture ida (28 equipos → 27 fechas), tabla, desempates
│   │   │   ├── Cup.ts              # llave de eliminación directa con penales
│   │   │   └── QuickSim.ts         # simulación rápida de partidos CPU vs CPU (para las fechas que no jugás)
│   │   ├── data/
│   │   │   ├── types.ts            # Team, Player, Kit, Crest, Formation… (tipos estrictos)
│   │   │   ├── validate.ts         # valida teams.json al arrancar; error claro si falta algo
│   │   │   └── generateNames.ts    # generador determinista de nombres argentinos
│   │   └── save/
│   │       └── SaveGame.ts         # esquema versionado de guardado (liga/copa en curso, settings)
│   ├── game/                       # CAPA PHASER. Solo presenta e inyecta input al core.
│   │   ├── scenes/                 # Boot, Preload, Menu, TeamSelect, Match, HUD, Pause, Result, League, Cup, Penalties, Settings
│   │   ├── render/
│   │   │   ├── Projection.ts       # (x,y,z) mundo → (sx,sy) pantalla; sombra; orden de profundidad
│   │   │   ├── PitchRenderer.ts    # cancha dibujada una vez a RenderTexture (césped a franjas, líneas, redes)
│   │   │   ├── PlayerSprites.ts    # spritesheets generados por código con colores del kit
│   │   │   ├── BallSprite.ts       # pelota + sombra proyectada + escala por altura
│   │   │   ├── CrestSVG.ts         # escudos SVG procedurales → textura
│   │   │   └── DebugOverlay.ts     # FPS, ms de update/render, draw calls, memoria, latencia input
│   │   ├── input/
│   │   │   ├── VirtualJoystick.ts  # flotante: aparece donde apoyás el dedo
│   │   │   ├── ActionButtons.ts    # botones contextuales + barra de potencia por duración
│   │   │   ├── TouchLayout.ts      # zonas para 1 jugador / 2 jugadores (mismo celu)
│   │   │   └── InputState.ts       # struct plano que lee el core cada tick
│   │   ├── camera/CameraRig.ts     # sigue la pelota con anticipación y zoom suave
│   │   ├── audio/                  # Fase 4
│   │   └── ui/                     # botones, paneles, tipografía, transiciones
│   └── platform/
│       ├── Storage.ts              # @capacitor/preferences con fallback a localStorage (web)
│       ├── Haptics.ts              # vibración corta en tiro/gol/falta (Fase 4)
│       ├── SafeArea.ts             # insets del notch → padding del HUD
│       └── Orientation.ts          # bloqueo landscape
├── tests/                          # Vitest: espeja src/core
├── android/                        # generado por `cap add android`, commiteado
└── public/                         # solo icono y splash
```

Regla de oro: **`src/core` no importa Phaser**. Toda la simulación es determinista
dado un input y una semilla, así que se testea, se puede simular a velocidad de CPU
para la liga, y en Fase 5 se puede sincronizar por red.

---

## 6. Loop de juego y latencia

- **Simulación a paso fijo de 60 Hz** (acumulador). Si el celu baja a 45 fps, la
  física no cambia; solo se renderizan menos frames.
- **Input**: los eventos `pointerdown/move/up` escriben directo en `InputState` en
  el mismo frame en que llegan (Phaser 3.90 no encola input). El tick siguiente ya lo
  ve. Latencia = 1 frame de render (~16 ms) + latencia del touchscreen. Objetivo < 50 ms
  medido en el overlay con un marcador de "toque → respuesta".
- **Render** interpola posiciones entre el último tick y el actual para movimiento
  suave aunque el frame no coincida con el tick.
- **Cero allocaciones por frame** en el core: vectores mutables preasignados,
  arrays de tamaño fijo, sin closures en el hot path.

---

## 7. Física de la pelota (lo más importante) `[SUPUESTO 5]`

Unidades en **metros y segundos** (cancha 105 × 68 m), escala a píxeles solo al
renderizar. Todas las constantes en `data/tuning.json`.

| Fenómeno | Modelo |
|---|---|
| Gravedad | `vz -= 9.81·dt` (escalado por un factor arcade ~1.3 para que caiga más rápido y se sienta ágil) |
| Aire | drag cuadrático suave: `v -= k·v·|v|·dt` |
| Rodando | fricción de rodadura (desacelera lineal) + umbral de parada |
| Pique | restitución 0.62 en Z; se pierde ~15% de velocidad horizontal por pique; después de N piques chicos, rueda |
| Efecto | spin lateral → fuerza Magnus perpendicular a la velocidad; decae con el tiempo |
| Postes / travesaño | cilindros: rebote reflejado con restitución 0.75 |
| Red | frena y "atrapa" la pelota (amortiguación fuerte), gol se cuenta al cruzar 100% la línea |
| Jugador | zona de control: si la pelota llega baja y lenta, se pega adelante del pie a distancia fija; si viene fuerte, rebota con error |

Toques (todos con potencia 0–1 por duración del toque, con barra visible):

| Botón | Velocidad | Elevación | Spin | Asistencia |
|---|---|---|---|---|
| Pase | media | rasante | nulo | apunta al compañero mejor ubicado en el cono del joystick |
| Tiro | alta | sube con potencia (potencia máxima = tiro alto) | según lateral del joystick | leve ajuste al arco |
| Centro | media-alta | alto | lateral | apunta al área |
| Pase alto (doble toque pase) | media | media | nulo | idem pase |

---

## 8. Render 2.5D `[SUPUESTO 3, 4]`

- Cámara cenital con perspectiva falsa: mundo plano en 2D, proyección
  `sx = x·S`, `sy = y·S·0.82 − z·S·0.7`. La sombra va en `(x, y)` a escala
  `1/(1+z)`. La altura se lee por la separación pelota–sombra.
- Cancha **horizontal** (arcos a izquierda y derecha) porque el celu está en landscape.
- Escala base: 1 m = 12 px de mundo; la cámara hace zoom 0.9–1.3 según la acción.
- Orden de dibujo por `y` (depth sort) cada frame para que el que está más abajo
  tape al de arriba.
- **Sprites generados por código** al cargar el partido: cuerpo, cabeza, camiseta,
  short y medias con los colores del kit (primario, secundario, número). 8
  direcciones × 6 frames de carrera + quieto + patada + barrida + arquero (vuelo,
  atajada). Se pintan una vez a un atlas por equipo. Cero PNG externos.
- Escudos: SVG procedural con 6 formas base (escudo clásico, círculo, rombo,
  cuadrado, pentágono, franja) + 4 patrones (bandas, mitades, cuartos, cruz) +
  monograma; parámetros en `teams.json`. Se rasteriza a textura con `Phaser.Textures`
  en la resolución que pide cada pantalla.
- Cancha: dibujada una vez a `RenderTexture` (franjas, líneas, redes). Un draw call.

---

## 9. Controles táctiles `[SUPUESTO 6]`

**Un jugador (vs CPU)**
- Joystick flotante en la mitad izquierda: nace donde apoyás el dedo, radio 60 px,
  zona muerta 12%, dirección analógica.
- Mitad derecha, 3 botones contextuales grandes (≥ 64 px) + sprint (mantener):
  - Con pelota: **PASE · TIRO · CENTRO** · SPRINT
  - Sin pelota: **BARRIDA · PRESIÓN · CAMBIAR** · SPRINT
- Potencia por duración del toque: barra circular alrededor del botón. Suelta = ejecuta.
- Cambio automático al jugador más cercano a la pelota cuando la posesión es rival,
  con histéresis para que no titile. Cambio manual con el botón CAMBIAR.

**Dos jugadores, mismo celu**
- El celu se apoya horizontal entre los dos, cada uno con **su mitad de la pantalla**:
  P1 mitad izquierda (joystick a la izquierda del todo, botones cerca del centro),
  P2 mitad derecha espejado. Los botones se achican a 2 + sprint (PASE/TIRO y
  BARRIDA/CAMBIAR) para que entren. HUD (marcador, reloj) arriba al centro.

---

## 10. IA

- **TeamBrain** decide fase (ataque, defensa, transición), altura de la línea,
  intensidad de presión y qué 2 jugadores van a presionar al portador.
- **PlayerBrain** FSM por rol. Estados: `VOLVER_A_POSICION`, `MARCAR(rival)`,
  `CUBRIR(zona)`, `PRESIONAR`, `IR_AL_BALON`, `DESMARCARSE`, `PEDIR_PASE`,
  `PORTADOR: AVANZAR | PASAR | TIRAR | DESPEJAR`, arquero: `POSICIONARSE`,
  `SALIR`, `ATAJAR`, `SACAR`.
- Portador: evalúa 3–5 opciones (avanzar, pase a cada compañero libre, tiro si en
  rango, despeje si está bajo presión en su área) con puntaje = xG aproximado +
  riesgo. Los stats del jugador pesan en la ejecución, no en la decisión.
- **Dificultad** (solo cambia percepción y ejecución, nunca stats):

| Nivel | Reacción | Error de pase/tiro | Frecuencia de decisión | Presión |
|---|---|---|---|---|
| Fácil | 450 ms | ±14° | 2 Hz | baja |
| Normal | 300 ms | ±9° | 4 Hz | media |
| Difícil | 180 ms | ±5° | 6 Hz | alta |
| Leyenda | 100 ms | ±2° | 10 Hz | asfixiante |

---

## 11. Reglas

Máquina de estados `Referee` con transiciones explícitas y testeadas:
gol → saque inicial; pelota fuera por línea de fondo → saque de arco o córner según
último toque; por lateral → lateral; falta → tiro libre directo (o penal si es en el
área); tarjeta amarilla/roja con expulsión (el equipo sigue con 10); offside
(activable en Settings, evaluado en el instante del pase hacia adelante); tanda de
penales en Copa si empatan. Tiempo configurable 2/4/6/8 min por partido (dos mitades
de la mitad), con descuento proporcional a las interrupciones.

---

## 12. Datos y contenido `[SUPUESTO 7, 8]`

- **28 equipos** inspirados en la Primera argentina: colores y ciudad reconocibles,
  nombres y escudos originales. Ejemplo de esquema:

```json
{
  "id": "ribera",
  "name": "Atlético La Ribera",
  "short": "RIB",
  "city": "Buenos Aires",
  "colors": { "primary": "#0A2A6E", "secondary": "#F5C400" },
  "kit": { "home": { "pattern": "band-h", "base": "#0A2A6E", "accent": "#F5C400" }, "away": { "pattern": "plain", "base": "#F5C400", "accent": "#0A2A6E" } },
  "crest": { "shape": "shield", "pattern": "band-h", "monogram": "AR" },
  "formation": "4-4-2",
  "rating": 84,
  "players": [ { "name": "Lautaro Giménez", "pos": "GK", "num": 1, "spd": 55, "sho": 30, "pas": 48, "dri": 35, "def": 40, "phy": 70, "gk": 82 } ]
}
```

- 18 jugadores por equipo (2 GK, 6 DEF, 6 MED, 4 DEL). Atributos 1–99 generados
  con distribución centrada en el `rating` del equipo, pero **guardados en el JSON**
  (no regenerados en runtime) para que sean editables.
- Todo el texto de UI en `data/strings.es.json` (español rioplatense).

---

## 13. Guardado local

`@capacitor/preferences` (fallback `localStorage` en web). Esquema versionado
`{ version, settings, league?, cup?, stats }`, con migraciones cuando cambie.
Se guarda al terminar cada partido y al salir de la app.

---

## 14. Performance: presupuesto y cómo se mide

| Métrica | Objetivo | Cómo se mide |
|---|---|---|
| FPS | 60 estables | overlay (`DebugOverlay`), promedio y p1 del último segundo |
| Tick de simulación | < 3 ms | `performance.now()` alrededor de `MatchSim.step` |
| Draw calls | < 60 por frame | contador del renderer WebGL de Phaser |
| Latencia input | < 50 ms | marcador toque→primer frame con respuesta, en overlay |
| Bundle | < 3 MB web, APK < 20 MB | `vite build` reporta; CI falla si se pasa |
| Arranque | < 3 s a menú | `performance.mark` en boot → menú, mostrado en overlay |
| Memoria | sin crecimiento en 30 min | overlay muestra `performance.memory` en Chrome |

Tácticas: un atlas por equipo, cancha en RenderTexture, pools para partículas y
textos, `Graphics` estáticos, sin `setText` cada frame, sin física Arcade en la
pelota, `roundPixels`, `antialias` off en sprites generados, `powerPreference:
high-performance`.

---

## 15. Tests (Vitest)

- `physics/Ball`: parábola con gravedad, rebote con restitución, se detiene en N s,
  spin curva hacia el lado correcto, choque con poste refleja.
- `rules/Referee`: cada transición; gol solo con la pelota 100% adentro; córner vs
  saque de arco según último toque; offside on/off; roja = 10 jugadores.
- `ai/Difficulty`: los 4 niveles producen errores decrecientes con misma semilla.
- `competition/League`: 28 equipos → 27 fechas, 14 partidos por fecha, ningún equipo
  juega dos veces por fecha; tabla ordena por puntos, diferencia, goles a favor.
- `competition/Cup`: llave de 32 con 4 byes, penales resuelven empates.
- `data/validate`: teams.json cumple esquema, 28 equipos, 18 jugadores c/u,
  atributos en 1–99, ids únicos.
- `save/SaveGame`: round-trip y migraciones.

CI: `npm run check` = `tsc --noEmit && vitest run && vite build`. Sin verde, no hay APK.

---

## 16. Fases, entregables y criterio de "listo"

### FASE 1 — Vertical slice (la que decide todo)
Entregable: APK con una cancha, un jugador controlado, una pelota, joystick +
botón de tiro con barra de potencia, cámara siguiendo la pelota, overlay de stats.
Listo cuando: vos decís que **se siente bien**. Iteramos la física y el control
hasta ahí; no se avanza por calendario.

### FASE 2 — Partido completo
11v11, cambio de jugador, todos los toques, reglas completas, IA por rol, 4
dificultades, arquero, HUD de partido, pausa, resultado. Listo cuando: un partido
de 4 min vs CPU en Difícil es divertido y sin bugs de reglas.

### FASE 3 — Modos y contenido
Menús, selección de equipo, 28 equipos con escudos y kits, amistoso 1v1 local,
liga con tabla y simulación de fechas, copa, tanda de penales suelta, settings,
guardado. Listo cuando: se puede jugar una liga entera y retomarla al día siguiente.

### FASE 4 — Pulido
Sonido (sintetizado por WebAudio + CC0 si hace falta), animaciones de celebración,
repetición de gol (rebobinado de snapshots del core), transiciones, haptics, splash,
icono, APK release firmado, sesión de 30 min sin crashes medida.

### FASE 5 — Online (solo si 1–4 impecables)
Lockstep determinista por WebSocket usando el core ya determinista.

Al final de cada fase: `npm run check` en verde, commit descriptivo, push, y 3
líneas de cómo probarlo en tu celu. No paso de fase sin tu OK.

---

## 17. Preguntas abiertas (con mi propuesta por defecto)

Marcá cuáles cambiás; lo que no menciones, lo tomo como aprobado.

1. **Ubicación**: `liga-arcade/` en este repo, excluido de Vercel. ¿O repo nuevo?
2. **APK**: por GitHub Actions (bajás el artifact al celu). ¿Tenés Android Studio en
   una PC como alternativa? ¿Querés además la build web publicada en el sitio para
   probar en Chrome?
3. **Ángulo de cámara**: cenital con perspectiva leve (cancha horizontal, arcos a los
   costados, jugadores se ven de arriba/atrás). ¿O más "TV" como DLS, con la cancha
   más aplastada?
4. **Estilo gráfico**: sprites vectoriales limpios generados por código (tipo Soccer
   Champs). ¿O pixel art?
5. **Sensación de pelota**: arcade ágil (cae rápido, pases secos, tiros con curva
   marcada). ¿O más "pesada" y realista?
6. **1v1 local**: cada jugador usa su mitad de pantalla (P1 izquierda, P2 derecha
   espejada), celu apoyado entre los dos. ¿Confirmás?
7. **Nombres de equipos**: originales pero reconocibles (ciudad + colores reales +
   nombre inventado, ej. "Atlético La Ribera"). ¿Querés que se parezcan más o menos?
8. **Idioma**: solo español rioplatense. ¿Sumamos inglés?
9. **Tu celular**: modelo y versión de Android, para calibrar el objetivo de
   performance con un dispositivo concreto.
10. **App ID**: `ar.tunegocioenlasredes.ligaarcade`. ¿Otro?
11. **Offside**: activado por defecto en Normal+ y desactivado en Fácil. ¿OK?
12. **Duración por defecto**: 4 min por partido. ¿OK?
