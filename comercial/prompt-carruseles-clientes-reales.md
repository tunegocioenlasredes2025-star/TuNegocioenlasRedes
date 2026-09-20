# Prompt: más carruseles, con clientes reales del CRM

Para pegar en un Claude Code que corra **en la PC de Mateo**, con acceso al
navegador. Requiere tener el repo clonado y la rama
`claude/compassionate-einstein-ogwv8a`.

---

Necesito que armes más carruseles de Instagram para nuestra agencia, usando un
sistema de diseño que ya está construido en este repo. Sos diseñador y director
creativo: el sistema ya existe, no lo rehagas — usalo y escribí el contenido.

## Quiénes somos

**Tu Negocio En Las Redes (TNR)** — agencia digital en Ituzaingó, Morón y
Castelar (Zona Oeste, GBA). Somos Mateo De Rosa y Santi Stalla, los dos de 16.
Hacemos webs, tiendas, redes, publicidad, automatización de WhatsApp, chatbots
y CRM para PyMEs de barrio.

- Web: https://www.tunegocioenlasredes.com.ar
- Instagram: @tunegocioenlasredes_
- CRM: https://tunegocioenlasredes-crm.vercel.app/
- Rama de trabajo: `claude/compassionate-einstein-ogwv8a` (nunca `main`)

## Paso 1 — Entrá al CRM antes de diseñar nada

**Usá el navegador de esta PC.** Este trabajo lo empezó otra sesión que corría
en la nube y **no tenía acceso al CRM**, así que armó los carruseles con lo que
decía la web pública. Ese es justamente el problema a corregir.

**Varios de los trabajos que figuran en `/trabajos` de la web son demos, no
clientes que pagaron.** Nadie sabe cuáles hasta mirar el CRM. Así que:

1. Abrí el CRM y sacá la lista real de clientes.
2. Marcá, para cada uno: si pagó de verdad, si sigue activo, si quedó conforme,
   y si autoriza que mostremos su caso.
3. **Sólo se hacen carruseles de clientes reales, conformes y que autoricen.**
   Si no podés confirmar alguna de las tres cosas, ese cliente no va. Preguntanos
   antes de asumir.

Cuando tengas la lista, **frená y mostrámela** con tu propuesta de qué 3 o 4
casos convertir en carrusel y por qué. Recién ahí seguís.

## Paso 2 — La devolución sobre lo que ya está hecho

Hay tres carruseles en `contenido/carruseles/`. Miralos antes de escribir nada:

| Carpeta | Slides | Veredicto |
|---|---|---|
| `00-muestra-estilo` | 4 | ✅ **Este es el molde. Funciona.** |
| `01-mundo-cortinas` | 8 | ❌ Demasiado largo, con relleno |
| `02-diez-botones-whatsapp` | 8 | ❌ Demasiado largo, con relleno |

**El problema de los de 8 no es el diseño, es que estiran una idea que entraba
en cuatro slides.** En el de Mundo Cortinas, los slides 2, 3 y 5 dicen tres
versiones de lo mismo ("explicar lo mismo cuesta tiempo"), y el de los cuatro
pasos del proceso es información de manual que no aporta al argumento.

**La regla: 4 o 5 slides. Nunca más de 5.**

El molde que funciona es el de `00-muestra-estilo`, y cada slide tiene un
trabajo distinto:

| Slide | Etiqueta | Su único trabajo |
|---|---|---|
| 1 | `Caso real · [Negocio] · [Barrio]` | El hook. Una tensión sin resolver |
| 2 | `El problema` | El problema del rubro, en una frase |
| 3 | `Qué construimos` | La decisión concreta + captura del celular |
| 4 | `Qué tiene hoy` | El resultado, verificable. Con CTA |

El quinto slide es opcional y sólo va si hay **un detalle concreto que valga
por sí solo** — no para "desarrollar más".

**El test antes de sumar un slide:** si lo borrás y el argumento se entiende
igual, era relleno. Borralo.

## Paso 3 — Cómo se construye (el sistema ya existe)

Leé primero `contenido/sistema-visual-ig.md` y `contenido/editar-en-canva.md`.

Un carrusel es una carpeta con un `make.py` que sólo define el copy. El sistema
visual está en `contenido/sistema.py` y el render en `contenido/build.py`.

```bash
python3 contenido/build.py contenido/carruseles/<carpeta>
```

Eso genera de una: los PNG 2160×2700 para publicar, el `editable-canva.pptx`,
el PDF de respaldo y una hoja de contacto para revisar el ritmo de un vistazo.

Copiá `contenido/carruseles/00-muestra-estilo/make.py` como base. Los bloques
disponibles en `sistema.py` son `h()`, `sub()`, `split()`, `pasos()`, `vs()` y
`cta()`. Los fondos son `''` (blanco), `'mist'` (gris claro) y `'navy'`.

**Cuatro cosas que te van a morder si no las sabés:**

1. `build.py` avisa cuando un titular se parte en más renglones que los que
   pide el copy. Si aparece el aviso, bajá un escalón de tamaño
   (`xl` → `lg` → `md` → `sm`) o escribí más corto. De referencia: en `lg`
   entran ~19 caracteres por línea, en `md` ~24.
2. Las capturas claras **no van sobre fondo navy**: se apagan. Fijate el fondo
   de la web de ese cliente antes de elegir el color del slide.
3. El marcador celeste se usa **una vez por slide**. Dos anulan las dos.
4. No toques las fuentes ni el bloque `@media print`: están así por razones que
   costó encontrar y están documentadas en `editar-en-canva.md`.

## Paso 4 — Las capturas de los clientes

En `trabajos/` sólo hay capturas de celular de cinco: GICI, Medisur, Mundo
Cortinas, Pasión Matera y TonCars.

Si el caso que vas a hacer no está ahí, **sacá la captura vos con el navegador**:
abrí el sitio del cliente en ancho de celular (~480 px), capturá desde arriba y
guardala en `trabajos/` con el mismo criterio de nombre que las otras.

## Las reglas de contenido (no negociables)

1. **Nombre propio.** Cada carrusel nombra el negocio, el rubro y el barrio. Si
   sirve igual para una ferretería de Ituzaingó y una startup de Miami, está mal.
2. **Si un número no se puede verificar, no va.** Es la regla de toda la casa y
   está escrita en `PENDIENTE-DATOS.md`. Tenés navegador: si vas a decir "diez
   accesos a WhatsApp", abrí el sitio y contalos. Si no da, cambiá la frase.
3. **Prueba visible.** Captura real del cliente. **Cero fotos de banco.**
4. **Primera persona.** "Hicimos", "nos pasó". Nunca "las empresas deben".
5. **Nada de inventar resultados.** Si no sabés cuántas consultas le entran,
   no lo digas. Describí lo que se puede ver abriendo el sitio.

Escribí en español rioplatense, de vos, directo y sin adjetivos de más. El tono
es el de la web: concreto, sin vender humo.

## Qué entregás por cada carrusel

Una carpeta `contenido/carruseles/NN-nombre/` con:

- `make.py` — el copy y el orden de los slides
- `png/slide-01..04.png` — listos para publicar
- `editable-canva.pptx` — para retocar en Canva
- `caption.txt` — el texto del posteo, con hashtags locales

Commiteá en la rama `claude/compassionate-einstein-ogwv8a`.

## El orden de trabajo

1. CRM → lista de clientes reales, activos, conformes y que autoricen.
2. **Frená y mostrame** los 3 o 4 casos que proponés, con el ángulo de cada uno.
3. Con el visto bueno, armá el primero, mostrame la hoja de contacto y esperá.
4. Si va, seguís con los demás.

No me armes los cuatro de una: prefiero corregir el primero que descartar cuatro.
