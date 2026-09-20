# Prompt: más carruseles, con los clientes reales

Para pegar en un Claude Code que corra **en la PC de Mateo**, con acceso al
navegador. Requiere el repo clonado en la rama
`claude/compassionate-einstein-ogwv8a`.

---

Necesito que armes más carruseles de Instagram para nuestra agencia, usando el
sistema de diseño que ya está construido en este repo. El sistema existe: no lo
rehagas. Tu trabajo es elegir los casos, escribir el copy y armar los archivos.

## Quiénes somos

**Tu Negocio En Las Redes (TNR)** — agencia digital en Ituzaingó, Morón y
Castelar (Zona Oeste, GBA). Somos Mateo De Rosa y Santi Stalla, los dos de 16.
Hacemos webs, tiendas, redes, publicidad, automatización de WhatsApp y CRM para
PyMEs de barrio.

- Web: https://www.tunegocioenlasredes.com.ar · IG: @tunegocioenlasredes_
- CRM: https://tunegocioenlasredes-crm.vercel.app/
- Rama de trabajo: `claude/compassionate-einstein-ogwv8a` (nunca `main`)

## Lo primero: quiénes son clientes de verdad

Los datos del CRM ya están cargados en
**`comercial/TNR-datos-para-el-analisis.xlsx`, hoja *Clientes***. Leela antes de
escribir una sola línea.

**Ojo con esto:** de los 15 trabajos publicados en `/trabajos` de la web, **la
mayoría son demos que nunca pagaron.** Mundo Cortinas, Pasión Matera,
Compugatti, Addware, Expocart, ATS Seguridad, Bite Club, LOFT, Consultorios VEC,
Electricista 24hs, Monitoreo Inteligente y After Gym figuran todos como
*"Demo / no pagó"*. Medisur es cliente pero todavía no cobramos nada.

Los que sí pagaron son otros, y son los únicos que pueden salir como caso:

| Cliente | Rubro | Dónde | Por qué da buen carrusel |
|---|---|---|---|
| **Setup Argentina** | Importación | — | El más grande. Web + blog + mantenimiento + **Google Ads para Estados Unidos**. Muy conforme |
| **Mantenimiento técnico Ciro** | Servicio técnico | Ituzaingó | Landing + SEO + Google Ads. Es la prueba de Ads local que nos falta. Muy conforme |
| **F5 Sport** | Alquiler de canchas | Morón | Cuarto mes de redes. Prueba que lo mensual funciona |
| **MC E Bikes** | Bicicletas eléctricas | Castelar | E-commerce + branding. Mari, la que decide, muy contenta |
| **Motos Roll** | Taller de motos | Ituzaingó | Web + mes de redes. Rubro bien de barrio |
| **Dani BOX** | Escuela de boxeo | Castelar | Web. Rubro visual, fácil de mostrar |
| **Ton Cars** | Concesionaria | — | Ya tiene dos carruseles hechos |

**Dos reglas que no se saltean:**

1. **La columna "¿Autoriza mostrarlo?" está vacía para todos.** Antes de dar por
   cerrado cualquier carrusel, preguntanos si ese cliente autoriza. Si no está
   confirmado, no se publica.
2. **Verificá los datos con el navegador.** Tenés acceso: abrí el sitio del
   cliente y confirmá lo que vayas a afirmar. Si vas a decir "diez accesos a
   WhatsApp", contalos. Si no da, cambiá la frase.

## Lo segundo: la devolución sobre lo que ya está hecho

Hay tres carruseles en `contenido/carruseles/`. Miralos antes de escribir:

| Carpeta | Slides | Veredicto |
|---|---|---|
| `00-muestra-estilo` | 4 | ✅ **Este es el molde. Funciona.** |
| `01-mundo-cortinas` | 8 | ⛔ No publicar: Mundo Cortinas nunca pagó. Además es largo |
| `02-diez-botones-whatsapp` | 8 | ❌ Cliente real (Ton Cars), pero largo y con relleno |

**El problema de los de 8 slides no es el diseño: es que estiran una idea que
entraba en cuatro.** En el de Mundo Cortinas los slides 2, 3 y 5 dicen tres
versiones de lo mismo, y el de "los cuatro pasos del proceso" es información de
manual que no aporta al argumento.

### La regla: 4 o 5 slides. Nunca más de 5.

El molde que funciona es `00-muestra-estilo`, donde cada slide hace un trabajo
distinto:

| Slide | Etiqueta | Su único trabajo |
|---|---|---|
| 1 | `Caso real · [Negocio] · [Barrio]` | El hook. Una tensión sin resolver |
| 2 | `El problema` | El problema del rubro, en una frase |
| 3 | `Qué construimos` | La decisión concreta, con la captura del celular |
| 4 | `Qué tiene hoy` | El resultado verificable, con CTA |

El quinto es opcional y sólo va si hay **un detalle concreto que valga por sí
solo** — nunca para "desarrollar más".

**El test antes de sumar un slide:** si lo borrás y el argumento se entiende
igual, era relleno. Borralo.

## Cómo se construye

Leé `contenido/sistema-visual-ig.md` y `contenido/editar-en-canva.md`.

Un carrusel es una carpeta con un `make.py` que define sólo el copy. El sistema
visual vive en `contenido/sistema.py` y el render en `contenido/build.py`:

```bash
python3 contenido/build.py contenido/carruseles/<carpeta>
```

Eso genera de una: los PNG 2160×2700 para publicar, el `editable-canva.pptx`,
el PDF de respaldo y una hoja de contacto para ver el ritmo de un vistazo.

Copiá `contenido/carruseles/00-muestra-estilo/make.py` como base. Los bloques
de `sistema.py` son `h()`, `sub()`, `split()`, `pasos()`, `vs()` y `cta()`. Los
fondos: `''` (blanco), `'mist'` (gris claro) y `'navy'`.

**Cuatro cosas que te van a morder:**

1. `build.py` avisa cuando un titular se parte en más renglones que los que pide
   el copy. Si sale el aviso, bajá un tamaño (`xl` → `lg` → `md` → `sm`) o
   escribí más corto. En `lg` entran ~19 caracteres por línea; en `md`, ~24.
2. Las capturas claras **no van sobre fondo navy**: se apagan. Mirá el fondo del
   sitio del cliente antes de elegir el color del slide.
3. El marcador celeste, **una vez por slide**. Dos anulan las dos.
4. No toques las fuentes ni el bloque `@media print`: están así por razones que
   costó encontrar, documentadas en `editar-en-canva.md`.

## Las capturas de los clientes

En `trabajos/` sólo hay capturas de celular de cinco negocios, y **tres de esos
son demos**. Para los clientes reales de la tabla de arriba vas a tener que
sacarlas vos: abrí el sitio en ancho de celular (~480 px), capturá desde arriba
y guardala en `trabajos/` siguiendo el criterio de nombre de las que ya están.

## Las reglas de contenido

1. **Nombre propio.** Cada carrusel nombra el negocio, el rubro y el barrio. Si
   sirve igual para una ferretería de Ituzaingó y una startup de Miami, está mal.
2. **Si un número no se puede verificar, no va.** Es la regla de toda la casa,
   escrita en `PENDIENTE-DATOS.md`. Tenés navegador: verificá.
3. **Prueba visible.** Captura real del cliente. **Cero fotos de banco.**
4. **Primera persona.** "Hicimos", "nos pasó". Nunca "las empresas deben".
5. **Nada de inventar resultados.** Si no sabés cuántas consultas le entran, no
   lo digas. Contá lo que se ve abriendo el sitio.

Español rioplatense, de vos, directo y sin adjetivos de más. El tono es el de la
web: concreto, sin vender humo.

## Qué entregás por carrusel

Una carpeta `contenido/carruseles/NN-nombre/` con `make.py`, los PNG en `png/`,
el `editable-canva.pptx` y un `caption.txt` con hashtags locales. Commiteá en la
rama `claude/compassionate-einstein-ogwv8a`.

## El orden de trabajo

1. Leé la hoja *Clientes* del Excel y proponeme **3 o 4 casos**, con el ángulo
   de cada uno en una línea. **Frená ahí y mostrámelo.**
2. Con el visto bueno, armá el primero y mostrame la hoja de contacto.
3. Si va, seguís con los demás.

No me armes los cuatro de una: prefiero corregir el primero que descartar cuatro.
