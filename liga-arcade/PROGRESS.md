# Liga Arcade — PROGRESS

## Estado general
- [x] Relevamiento del repo y del entorno
- [x] PLAN.md aprobado con ajustes (iPhone → PWA, modo carrera DLS, Primera + Primera Nacional)

## FASE 1 — Vertical slice · **lista para que la pruebes**
- [x] Scaffold: Vite 7 + TS 5 estricto + Phaser 3.90 + Vitest 3 + Capacitor 8
- [x] Core sin Phaser: pelota con eje Z (gravedad, drag, pique, fricción, efecto), postes y travesaño con colisión continua, red, gol, jugador con inercia, conducción y toque largo al sprintar, tiro/pase/centro por potencia
- [x] 22 tests en verde (física, reglas de gol, posesión, determinismo)
- [x] Render 2.5D con perspectiva estilo DLS: cancha en textura única, arcos con red, sprite de jugador generado por código (8 direcciones × correr/patear/barrer), pelota con sombra y altura
- [x] Joystick flotante + botones TIRO / PASE / CENTRO / SPRINT con anillo de potencia, multi-touch real
- [x] Cámara que sigue la pelota con anticipación y zoom
- [x] Overlay de stats (FPS, 1% low, ms de simulación, latencia de input, boot, heap) → botón "FPS" o `?stats`
- [x] PWA: manifest, service worker con precache, íconos, overlay "girá el teléfono", safe areas
- [x] Proyecto Android (Capacitor) + workflow de GitHub Actions que deja el APK como artifact
- [x] Test de humo en Chromium headless con viewport de iPhone (arranque < 1 s, 0 errores, gol de punta a punta)
- [ ] **Probado en tu iPhone** → ajustar sensación (velocidad, potencia, cámara, tamaño de botones) hasta que se sienta bien
- [ ] OK explícito para pasar a Fase 2

## FASE 2 — Partido completo
- [ ] 11v11, cambio de jugador automático/manual, arquero, IA por rol, 4 dificultades, reglas completas, HUD de partido

## FASE 3 — Modos y contenido
- [ ] Menús, 30 + 36 equipos con escudos y kits, amistoso 1v1 local, liga, copa, penales, settings, guardado
- [ ] Modo Carrera estilo DLS (monedas, mercado de pases, estadio, ascensos)

## FASE 4 — Pulido
- [ ] Sonido, celebraciones, repetición de gol, transiciones, APK release firmado, sesión de 30 min sin crashes

## FASE 5 — Online
- [ ] Pendiente
