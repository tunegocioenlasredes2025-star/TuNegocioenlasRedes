# Secure Growing — Sistema visual y de contenido para Instagram

Documento de trabajo. Todo lo que se produce para @securegrowing sale de acá y de `tokens.css`.
Fecha: septiembre 2026.

---

## 0. Fuentes de este documento

| Fuente | Qué aportó | Estado |
|---|---|---|
| Código de la landing `secure-growing.vercel.app` (repo `tunegocioenlasredes2025-star/SecureGrowing`, rama main, `index.html` + `assets/styles.css`) | Copy completo, paleta con HEX exactos, tipografías, patrones de layout | Leído entero. La URL pública está bloqueada desde este entorno, se leyó el código fuente que la genera. |
| Nota de proyecto `proyecto-b2b-secure-growing.md` (Drive, 30/08/2026) | Decisiones de branding, gustos verificados de Mateo, economía del cliente, planes | Leída. |
| Instagram @securegrowing | Bloqueado desde este entorno. No se scrapeó nada. | El único dato de cuenta disponible es "477 seguidores" medido en la nota del 30/08/2026. No se inventó nada más. |
| `./referencias/*.png` (piezas ya producidas) | Debían ser la base del análisis del sistema visual | **No están en el repo ni en Drive.** Este documento se armó con la landing como pieza de referencia real. Cuando estén las capturas, se ajusta la sección 3. |

---

## 1. La marca (descubrimiento)

**Qué es.** Agencia / consultora de canal comercial digital para empresas B2B. Se presenta como
"Marketing B2B industrial". Tres verticales: seguridad electrónica, canal ferretero, industria.
Este trabajo es solo para la vertical de seguridad electrónica.

**Propuesta de valor (literal de la web).**
"Tus vendedores no necesitan más esfuerzo. Necesitan más gente a quién venderle."
"Le llevamos demanda calificada al área comercial de tu empresa. Con números, todos los meses."

**A quién le habla.** Al dueño o gerente comercial de una empresa de seguridad electrónica que
le vende a empresas o a instaladores: centrales de monitoreo mayoristas, integradores,
distribuidores, fabricantes e importadores. No al vecino que quiere una alarma. Tiene
vendedores, tiene producto, no tiene tiempo y desconfía de las agencias.

**El problema que nombra la web (tres puntos).**
1. El que te busca no te encuentra. "Te googlea antes de llamarte. Si no lo convencés ahí, se va sin que te enteres."
2. Tus vendedores esperan sentados. "Cierran bien. El problema es lo poco que les llega para cerrar."
3. Nadie sabe qué funcionó. "Se invierte en redes, catálogos y expos. A fin de año nadie tiene el número."

**Lo que resuelve (tres pastillas).** Más demanda calificada · Posicionamiento técnico · Contenido que convierte.

**Los cinco frentes (sección #frentes).**
01 Procesos de venta — "Del primer mensaje al cierre, ordenado y automatizado."
02 Marketing B2B — "Vender a empresas es otro juego. Lo jugamos así."
03 Análisis de mercado — "Quién te compra, cuántos son y dónde están."
04 Páginas web — "Que terminan en una reunión, no en un formulario."
05 Contenido — "Foto, video y piezas para redes y prensa del sector."

**El método (tres etapas, siempre en ese orden).**
01 Diagnóstico — "Dos semanas. Sale un informe con números, no con opiniones."
02 Estrategia — "A quién, con qué mensaje y por qué canal. Por escrito."
03 Producción — "Se ejecuta y se mide. Lo que no mueve el número, se cambia."

**Prueba.** Clientes nombrados: Monitoreo Inteligente (central de monitoreo mayorista) y ATS Seguridad.
Trabajan con la prensa especializada del sector (InfoSeguridad). "Empresas del rubro, no casos de otro país."

**CTA único.** Reunión de 20 minutos. "Miramos tu canal comercial antes de la reunión y llegamos con el diagnóstico hecho."

**Vocabulario propio (usar).** demanda calificada · canal comercial · el número · frentes · diagnóstico ·
te dejamos el número · el que firma la compra · posicionamiento técnico · reunión de 20 minutos ·
"lo que no mueve el número, se cambia" · el rubro · instalador · abonado · central de monitoreo.

**Vocabulario prohibido.** leads (decir "contactos" o "demanda"), marca personal, comunidad, engagement,
"tu marca", transformar, potenciar, "en el mundo actual", "la clave está en", "¿sabías que?",
"no se trata de X sino de Y", emojis, signos de exclamación.

**Objeciones que la web responde (y que las piezas tienen que atacar).**
| Objeción del dueño | Respuesta de Secure Growing |
|---|---|
| "En este rubro se vende por relación y referidos, no por internet" | Te googlean antes de llamarte, aunque vengan referidos. |
| "Ya tengo vendedores" | Cierran bien; el problema es lo poco que les llega. |
| "Ya probé con una agencia y no sirvió" | Nadie te dejó el número. Nosotros medimos hasta el cierre. |
| "Marketing es caro para lo que vendo" | La cuenta se hace con el valor de un abonado en el tiempo, no con el precio del mes. |
| "Mi web ya está / con el catálogo alcanza" | Cuando te comparan contra tres proveedores, el más serio tiene que ser vos. |
| "No tengo tiempo" | Veinte minutos y llegamos con el diagnóstico hecho. |
| "No hay nada para publicar en este rubro" | La prensa del sector publica casi a diario. Contenido hay, falta sistema. |

**Voz.** Español rioplatense, vos. Frases cortas, punto y aparte. Seco, sin adorno, sin exclamación.
Nombra la realidad concreta del dueño (el vendedor sentado, el catálogo, la expo, el instalador que
cobra una vez). Números antes que adjetivos. Cierra siempre con una acción que se puede hacer hoy.

---

## 2. Paleta (HEX exactos, tomados de `assets/styles.css`)

| Token | HEX | Uso en la landing |
|---|---|---|
| verde | `#053727` | fondo principal (hero, resolvemos, por qué, cta), theme-color |
| verde-alto | `#0A4A34` | verde un tono arriba, reservado para bloques sobre verde |
| verde-med | `#406459` | eyebrow sobre hueso |
| negro | `#0A0B0C` | fondo alterno (método, footer) |
| cobre | `#C8863C` | botón principal, numeración 01-05, contorno de números gigantes, punto del ticker, cobre del logo |
| cobre-cl | `#E7B173` | palabra acentuada del titular, eyebrow sobre oscuro, títulos de "por qué" |
| cobre-osc | `#7A5526` | marca de agua del logo (logo-bronce.svg) |
| hueso | `#F4F3EF` | fondo claro y texto sobre oscuro |
| hueso-2 | `#E4E1D9` | divisoras sobre hueso |
| texto | `#11201B` | texto sobre hueso |
| texto-sub | `#4E5E59` | texto secundario sobre hueso |
| sobre-cobre | `#20140A` | texto del botón cobre |

Alphas de hueso sobre oscuro: .78 (bajada), .70 (cuerpo), .60 (ticker), .40 (legal), .16 (líneas).

**Contraste (WCAG, calculado).**
- hueso `#F4F3EF` sobre verde `#053727`: 11.9:1 (AAA).
- cobre-cl `#E7B173` sobre verde `#053727`: 6.9:1 (AAA). Es el acento para texto sobre oscuro. Sobre negro: 10.3:1.
- cobre `#C8863C` sobre verde `#053727`: 4.4:1. **Pasa AA solo como texto grande** (más de 24 px, o 19 px en negrita). Se usa en números gigantes, numeración de filas y elementos de dato. Para texto chico sobre verde va cobre-cl, nunca cobre.
- cobre `#C8863C` sobre negro `#0A0B0C`: 6.5:1 (AA en cualquier tamaño).
- verde `#053727` sobre hueso `#F4F3EF`: 11.9:1. verde-med `#406459` sobre hueso: 5.9:1. texto-sub `#4E5E59` sobre hueso: 6.2:1.
- cobre `#C8863C` sobre hueso `#F4F3EF`: 2.7:1. **No pasa AA para texto.** Sobre hueso, el cobre solo va en elementos gráficos grandes (barras, puntos, numeración de 100 px o más). Texto en cobre sobre hueso, nunca.
- **No hay lima en el sistema.** El negro+lima es de Monitoreo Inteligente y el negro+oro es de ATS, ambos clientes; la decisión del 30/08 los descarta para Secure Growing. El acento es cobre.

**Reglas de color.**
- Dos fondos oscuros (verde y negro) y uno claro (hueso). Un carrusel alterna como la landing: abre en verde, cambia a hueso o negro por bloque de sentido, cierra en verde.
- Un solo acento por slide: cobre / cobre-cl. Nunca dos acentos.
- Nada de degradados visibles, texturas ni grillas de fondo (gusto verificado de Mateo).

---

## 3. Tipografía

| Rol | Familia | Pesos | Google Fonts |
|---|---|---|---|
| Display (titulares, números, pastillas, eyebrow, botones) | Bricolage Grotesque | 700, 800 | sí |
| Texto (bajadas, cuerpo, notas) | Instrument Sans | 400, 500, 600 | sí |

Ambas están en Canva. Los archivos viven en `./fonts/` y se cargan por `@font-face` con ruta local.
Los woff2 de Google Fonts son fuentes variables; para el PDF se usan instancias estáticas TTF generadas de esos mismos archivos (`fonts/BricolageGrotesque-Bold.ttf`, `-ExtraBold.ttf`, `InstrumentSans-Regular.ttf`, `-Medium.ttf`, `-SemiBold.ttf`), ver sección 7.

**Jerarquía por slide (de arriba hacia abajo).**
1. **Eyebrow**: 22 px, Bricolage 700, mayúsculas, tracking .2em, cobre-cl sobre oscuro / verde-med sobre hueso. Dice de qué trata la pieza o numera el slide ("02 / 08").
2. **Titular**: 88 a 112 px, Bricolage 800, tracking −.035em, line-height 1.0. Una palabra o frase acentuada en cobre-cl. Máximo tres líneas.
3. **Bajada**: 30 px, Instrument Sans 400, hueso al 78 % sobre oscuro / texto-sub sobre hueso. Máximo 3 líneas, máximo 40 caracteres por línea.
4. **Elemento de dato**: el número gigante, la barra, la grilla, la tabla o el timeline. Ocupa el centro visual del slide. Cada dato lleva su etiqueta a 22 px y su fuente a 22 px, hueso al 60 %.
5. **Firma**: isotipo 64 px + "@securegrowing" 22 px Bricolage 700, abajo a la izquierda. Slide número o "deslizá" abajo a la derecha, 22 px, hueso al 40 %.

**Números gigantes.** Bricolage 800, 260 a 420 px, tracking −.05em, line-height .85. En la landing van en contorno cobre (`-webkit-text-stroke`). En el PDF editable el contorno convierte el texto en curvas, así que en PDF el número va en cobre sólido, y el contorno queda para el PNG (ver sección 7).

---

## 4. Grilla y márgenes (lienzo 1080 × 1350)

- Margen exterior: 80 px a los cuatro lados. Zona segura: nada esencial a menos de 64 px del borde.
- Ancho útil: 920 px. Una sola columna; cuando hay dos columnas contrapuestas, 2 × 444 px con 32 px de calle.
- Eyebrow arranca a 96 px del borde superior.
- Firma termina a 80 px del borde inferior.
- Separación entre bloques: 32 px; entre grupos: 56 px.
- Todo alineado a la izquierda, salvo el slide de cierre que puede centrar como la sección CTA de la landing.

---

## 5. Tratamiento de fondo y formas

- Fondos planos. Sin grilla, sin textura, sin ruido, sin glow. Sin foto de fondo.
- Divisoras de 2 px (`hueso-2` sobre claro, hueso al 16 % sobre oscuro) para separar filas, como en la landing.
- Pastilla (`border-radius: 999px`) hueso sobre verde, texto verde Bricolage 800: es la forma firma de la marca ("Más demanda calificada"). Siempre redonda, nunca rectangular.
- Bloques de dato con esquinas de 28 px como máximo y sin borde visible. Nada de tarjetas rectangulares con borde (a Mateo le parecen genéricas).
- Botón cobre redondo, texto `#20140A`, solo en el último slide.
- Isotipo: `logo-blanco.svg` sobre oscuro, `logo.svg` sobre hueso. Marca de agua opcional con `logo-bronce.svg` a opacidad baja, apagada por defecto como en la landing.

---

## 6. Patrón conceptual: un dato, una prueba visual

Cada slide interior tiene **un** dato y **un** elemento visual que lo demuestra. Nunca dos datos en un slide,
nunca un slide con solo texto después del hero. Los elementos disponibles, y la regla es que **no se
repite el mismo elemento en dos piezas distintas**:

| Elemento | Qué demuestra | Cómo se construye (CSS puro) |
|---|---|---|
| Número gigante | Una cifra que pesa sola | texto 260-420 px, cobre |
| Cascada de barras | Cómo se achica algo etapa por etapa (embudo) | 4-5 divs de alto fijo y ancho decreciente |
| Barra comparativa | A contra B | 2 divs horizontales, uno cobre, uno hueso al 16 % |
| Grilla de puntos | Cuántos de cuántos | flex-wrap de círculos, prendidos en cobre, apagados en hueso al 16 % |
| Timeline horizontal | Qué pasa antes de qué | línea de 2 px con puntos cobre y etiquetas debajo |
| Escalera | Cómo se acumula | 3 escalones de alto creciente con la cifra arriba de cada uno |
| Tabla ranking | Quién queda mejor parado en una comparación | filas divididas por líneas, columnas con etiqueta |
| Dos columnas contrapuestas | Lo que te dicen / lo que tiene que pasar | dos columnas con encabezado, divisora vertical de 2 px |
| Segmentos de tiempo | Cuánto dura algo | fila de 14 celdas, las cumplidas en cobre |
| Pastillas apiladas | Tres cosas, nada más | tres pills hueso una debajo de otra |
| Red de nodos | Un mercado chico donde todos se conocen | puntos unidos por líneas de 2 px (SVG con `<circle>` y `<line>`, sin texto adentro) |
| Filas numeradas | Lista corta con jerarquía | numeración 01-05 en cobre + título display + bajada, divisoras entre filas |

---

## 7. Reglas de producción (HTML → PDF editable → PNG)

- Un HTML por pieza, sin dependencias externas. Fuentes por `@font-face` apuntando a `../fonts/`.
- Cada slide es `<section class="slide">` de 1080 × 1350 px con `page-break-after: always`.
- `@page { size: 11.25in 14.0625in; margin: 0 }` (= 1080 × 1350 px a 96 dpi).
- Export: Playwright `page.pdf({ printBackground: true, preferCSSPageSize: true })`.
- **Fuentes estáticas.** Chromium embebe las fuentes variables como Type3 (curvas). Por eso el PDF usa
  instancias estáticas TTF generadas de los woff2 de Google Fonts (`fonts/*.ttf`). Así el texto queda
  como texto y Canva lo mapea por nombre a Bricolage Grotesque e Instrument Sans.
- **Sin `-webkit-text-stroke` en el PDF.** También produce Type3. El número en contorno se resuelve con
  `@media print { .num { color: cobre } }` y en pantalla/PNG conserva el contorno.
- Fondos y formas solo con CSS (div, border-radius, border). Sin imágenes de fondo. El isotipo es el único SVG y no lleva `<text>`.
- Cada bloque editable (eyebrow, titular, bajada, número, cada barra, firma) es un elemento hermano directo dentro de `.slide`, sin wrappers innecesarios, para que al aplanar grupos Canva deje una capa por bloque.
- Verificación obligatoria: `pdftotext` / pypdf sobre cada PDF tiene que devolver todo el copy, y las fuentes del PDF tienen que listarse como TrueType/Type0, nunca Type3.
- Respaldo PNG @2x (2160 × 2700) por slide.

---

## 8. Checklist de QA por pieza

- El titular se lee a 200 px de ancho (miniatura de feed).
- Nada cortado ni tocando los 64 px de zona segura.
- Cada slide interior aporta un dato nuevo. Si un slide no tiene dato, se saca.
- Dos piezas no comparten elemento visual ni titular parecido.
- Contraste: cobre-cl sobre verde 6.9:1, cobre sobre verde 4.4:1 (solo texto grande), hueso sobre verde 11.9:1. Cobre sobre hueso solo en gráficos.
- Copy: sin exclamación, sin emoji, sin frases de LinkedIn, cierre con acción concreta y distinta.
