# Informe SEO — Tu Negocio En Las Redes

**Fecha:** 28 de julio de 2026
**Sitio:** https://www.tunegocioenlasredes.com.ar
**Estado:** desplegado en producción y verificado en vivo

---

## 1. El hallazgo principal

Antes de cualquier análisis fino apareció la causa de fondo:

> **Todo el trabajo SEO previo (25/07) nunca se había commiteado.**
> Producción seguía sirviendo el build del **16 de julio**: sin `robots.txt`, sin `sitemap.xml`, sin URLs limpias y sin datos estructurados.

Es decir: el sitio no aparecía en Google en parte porque **Google no tenía forma de descubrirlo ni de entenderlo**. No era un problema de estrategia, era un problema de que el trabajo estaba en el disco y no en internet.

### El segundo hallazgo: la marca

El `<title>` del home era:

```
Agencia de Marketing Digital y Páginas Web | Zona Oeste
```

**No contenía el nombre de la marca.** Las subpáginas decían solo `| TNR`. Ningún H1 del sitio contenía la frase "Tu Negocio En Las Redes".

Cuando alguien busca "Tu Negocio En Las Redes", Google necesita una página que se declare como esa entidad. Ninguna lo hacía. Esa es la explicación más probable de por qué no aparecían ni por su propio nombre.

---

## 2. Auditoría: qué estaba mal

### SEO técnico

| Ítem | Estado previo |
|---|---|
| `robots.txt` | No existía en producción |
| `sitemap.xml` | No existía en producción |
| URLs limpias | No activas (`/servicios` daba 404) |
| Canonicals | Apuntaban al apex, que **308-redirige** al www → todos apuntaban a URLs que redirigen |
| Marca en `<title>` | Ausente en el home, abreviada a "TNR" en el resto |
| `lang` | `es` genérico en vez de `es-AR` |
| `meta keywords` | Presente (Google la ignora hace más de una década) |
| Datos estructurados | Solo en las 6 páginas, sin Service ni LocalBusiness con geo/horarios |
| Página 404 | No existía |
| `manifest` | No existía |

### Performance

| Ítem | Estado previo | Impacto |
|---|---|---|
| Favicon | `Logo.png` de **1,4 MB** | Se descargaba en cada página |
| `og:image` | `Logo.png` de **1,4 MB** | WhatsApp y Facebook debían bajar 1,4 MB para previsualizar un link |
| Logo en nav y footer | `Logo.png` de **1,4 MB**, mostrado a 52 px | ~2,8 MB por página solo en logos |
| Tipografía | Google Fonts | 2 orígenes externos en el critical path (DNS + TLS + CSS + fuente) |
| Imágenes de trabajos | Sin `width`/`height` | CLS (el layout salta al cargar) |
| Fallback de capturas | `onerror` → thum.io | Dependencia de un tercero que rate-limita y devuelve un GIF de spinner |
| Cache de `styles.css` | `immutable`, 1 año, **sin versionado** | Al cambiar el CSS, los visitantes recurrentes seguirían viendo el viejo durante meses |

### On-page

Ningún H1 del sitio contenía una sola palabra clave. Eran buenos ganchos comerciales, pero SEO-nulos:

- Home: *"Hacemos crecer tu negocio digitalmente."*
- Servicios: *"Todo lo que tu negocio necesita en un solo lugar."*
- IA: *"Mientras algunos responden manual, otros automatizan todo."*
- Trabajos: *"No solo hacemos webs..."*
- Nosotros: *"Jóvenes, sí. Pero los resultados no mienten."*
- Contacto: *"Tu presencia digital puede hacerte perder o multiplicar clientes."*

Además: solo 6 páginas para cubrir ~30 keywords objetivo. Sin páginas por servicio, sin páginas locales, sin blog.

---

## 3. Qué se corrigió

### Técnico

- **Migración completa al dominio canónico `www`** en canonicals, Open Graph, Twitter Cards, `sitemap.xml`, `robots.txt` y todos los `@id` de JSON-LD. Ya no hay canonicals apuntando a URLs que redirigen.
- **`robots.txt` y `sitemap.xml` publicados** — el sitemap se genera desde los archivos reales, así que no se desincroniza.
- **URLs limpias activas** (`cleanUrls`) y `.html` → 308 a la URL limpia.
- **La marca completa entra en los 6 `<title>`.**
- `lang="es-AR"`, `og:locale`, `meta keywords` eliminada.
- **Página 404** con enlazado interno y `noindex`.
- `site.webmanifest` + set completo de favicons.
- `vercel.json`: content-types explícitos, redirects de rutas cortas (`/crm`, `/web`, `/redes`…), política de cache corregida.

### Performance

| Cambio | Antes | Ahora |
|---|---|---|
| Favicon | 1,4 MB | **3 KB** |
| Imagen para compartir | 1,4 MB (logo cuadrado) | **76 KB** (`og-image.jpg` 1200×630 diseñada) |
| Logo en nav/footer | 1,4 MB | **19 KB** |
| Tipografía | 2 orígenes externos | **Self-hosteada**, 49 KB, con `preload` |
| Imágenes de trabajos | Sin dimensiones | `width`/`height` + `decoding="async"` (sin CLS) |
| Cache de assets | Insegura | Versionado por hash (`?v=`) + `immutable` 1 año |

El HTML del home viaja en **35 KB** y responde en **~0,12 s**.

### On-page

Los seis H1 se reescribieron **manteniendo el gancho comercial pero incorporando la keyword**. Ejemplo del home:

```
Antes:  Hacemos crecer tu negocio digitalmente.
Ahora:  Agencia de marketing digital y páginas web.
```

> Nota: el H1 nuevo empujaba el botón "Quiero una demo gratis" por debajo del pliegue en pantallas de 720 p. Se ajustó el corte de línea hasta devolver el hero a su altura original, sin perder la keyword.

### Contenido nuevo — de 6 a 22 páginas

**6 landings de servicio** (~900-1.100 palabras cada una, con FAQ propia y schema `Service`):

- `/paginas-web` · `/tiendas-online` · `/gestion-de-redes`
- `/publicidad-digital` · `/automatizacion-whatsapp` · `/crm-para-pymes`

**4 landings locales** con schema `LocalBusiness` (geo + horarios):

- `/marketing-digital-zona-oeste` (hub) · `/marketing-digital-ituzaingo` · `/marketing-digital-moron` · `/marketing-digital-castelar`

> **Importante:** no son la misma página con el nombre del barrio cambiado. Google penaliza eso como *doorway pages*. Cada una describe el tejido comercial real de su localidad, con ángulo, ejemplos y FAQ propios: Ituzaingó gira alrededor del comercio de barrio y el perfil distinto de Parque Leloir; Morón alrededor de competir donde hay más competencia y el costo por clic es más alto; Castelar alrededor de los emprendedores que venden solo por Instagram y ya sienten el techo.

**Blog con 4 artículos long-form** (schema `BlogPosting`), atacando búsquedas informacionales con intención comercial:

- ¿Cuánto cuesta una página web en Argentina?
- Cómo conseguir clientes por Instagram
- Chatbot de WhatsApp: qué automatizar y qué no
- Cómo aparecer en Google Maps

### Datos estructurados

| Tipo | Cantidad |
|---|---|
| BreadcrumbList | 20 |
| FAQPage | 15 |
| WebPage / CollectionPage / AboutPage / ContactPage | 17 |
| Service | 13 |
| BlogPosting | 4 |
| ProfessionalService (LocalBusiness, con geo y horarios) | 5 |
| Blog, WebSite, Organization | 3 |

### Enlazado interno

- Footer ampliado y sincronizado en las 22 páginas (servicios + zonas + blog).
- Tarjetas de servicio del home y de `/servicios` enlazadas a sus landings.
- Bloque "Somos de Zona Oeste" en el home hacia las 4 páginas locales.
- Cada landing cierra con 4 enlaces contextuales a páginas relacionadas.
- Enlaces dentro del texto de cada artículo hacia las páginas comerciales.

### Robustez (encontrado de paso)

- **`.reveal` solo se oculta si hay JS.** Antes, si `main.js` fallaba, *todo* el contenido del sitio quedaba invisible para siempre. Ahora se ve igual.
- Se respeta `prefers-reduced-motion`.
- El `IntersectionObserver` pasó de `threshold: 0.1` a `0`, para que un bloque de texto muy alto no pueda quedar sin revelarse.

---

## 4. Estimación de impacto

Ordenado por impacto real esperado. Las estimaciones son de dirección y magnitud, no promesas de posición.

| # | Mejora | Impacto | Plazo |
|---|---|---|---|
| 1 | **Deployar el SEO que estaba sin publicar** | **Decisivo.** Sin sitemap ni robots, el resto no existía | Días |
| 2 | **Marca en los `<title>`** | **Alto** para la búsqueda "Tu Negocio En Las Redes" | 2-6 semanas |
| 3 | **16 páginas nuevas** | **Alto.** Pasás de 6 a 22 puertas de entrada; cada landing puede rankear por su cuenta | 2-4 meses |
| 4 | **Landings locales** | **Alto** para "marketing digital Morón", "páginas web Ituzaingó" — baja competencia, alta intención | 1-3 meses |
| 5 | **Canonicals coherentes** | **Medio-alto.** Antes se diluía la señal entre apex y www | 3-8 semanas |
| 6 | **H1 con keywords** | **Medio-alto.** Es de las señales on-page más fuertes | 3-8 semanas |
| 7 | **Datos estructurados** | **Medio.** No sube posiciones directamente, pero habilita rich results (FAQ, breadcrumbs) que suben el CTR | 3-8 semanas |
| 8 | **Blog** | **Medio, creciente.** Captura búsquedas informacionales y construye autoridad temática | 3-6 meses |
| 9 | **Performance (−2,8 MB por página)** | **Medio.** Core Web Vitals es factor de ranking, y sobre todo baja el rebote en mobile | Inmediato |
| 10 | **og-image de 76 KB** | **Bajo en SEO, alto en conversión.** Los links compartidos por WhatsApp ahora previsualizan al instante | Inmediato |
| 11 | **Enlazado interno** | **Medio.** Distribuye autoridad y acelera el descubrimiento de las páginas nuevas | 2-6 semanas |

**Expectativa honesta:** los primeros movimientos en Search Console se ven entre la **segunda y la sexta semana**. El posicionamiento por keywords comerciales competidas ("agencia de marketing digital") es un trabajo de **6 a 12 meses** y depende mucho de conseguir enlaces externos. Las keywords locales de cola larga ("agencia de marketing en Ituzaingó") son las que pueden dar resultados en **1 a 3 meses**.

---

## 5. Próximos pasos, por prioridad

### 🔴 Bloqueantes — requieren tu cuenta (yo no puedo hacerlos)

**1. Google Search Console** — *esto es lo más urgente de todo.*
   - Entrar a https://search.google.com/search-console
   - Agregar la propiedad **`https://www.tunegocioenlasredes.com.ar`** (con www)
   - Verificar (lo más simple: registro TXT de DNS en Cloudflare)
   - Enviar el sitemap: `sitemap.xml`
   - Usar "Inspección de URLs" → "Solicitar indexación" en el home y en las 4 landings locales

   Sin esto, Google va a descubrir el sitio igual, pero mucho más lento y a ciegas: no vas a poder ver por qué búsquedas aparecés ni qué errores hay.

**2. Google Business Profile** — *lo de mayor retorno por hora invertida.*
   - Crear o reclamar la ficha en https://business.google.com
   - Categoría principal: **"Agencia de marketing"**
   - Zona de servicio: Ituzaingó, Morón, Castelar, Haedo, Ramos Mejía
   - Cargar horarios, fotos reales y descripción
   - Poner `https://www.tunegocioenlasredes.com.ar` como sitio web
   - Empezar a pedir reseñas sistemáticamente y **responderlas todas**

   La guía completa quedó escrita en `/blog/aparecer-en-google-maps` — la escribiste para tus clientes, aplicátela.

**3. Analítica** — hoy el sitio **no tiene nada instalado**. No hay forma de saber si algo funciona.
   - Crear una propiedad **GA4** y pasarme el `G-XXXXXXX`: yo lo instalo en las 22 páginas en un minuto.

### 🟡 Alto impacto — lo puedo hacer yo cuando digas

4. **Decidir apex vs www.** Hoy el primario en Vercel es `www` y todo apunta ahí, que es consistente. Si preferís el dominio sin `www` (queda más limpio en tarjetas y en el logo), cambialo en Vercel → Domains y yo migro los canonicals.
5. **Convertir las capturas de `/trabajos` a WebP** (~30-40 % menos peso).
6. **Más landings locales**: Haedo, Ramos Mejía, Hurlingham, Merlo. Solo si les damos contenido propio real, como a las cuatro actuales.
7. **Landings de servicio × localidad** para los combos con más demanda (ej. `/paginas-web-ituzaingo`). Con cuidado: acá es donde es fácil caer en doorway pages.
8. **Testimonios con schema `Review`** en las landings. Necesito los textos reales de clientes.
9. **Video real del CRM** en `/trabajos` (sigue pendiente desde antes; hoy hay un mockup en HTML).

### 🟢 Sostenido — el trabajo de todos los meses

10. **Un artículo nuevo cada 2 semanas.** Es lo que más mueve la aguja a mediano plazo.
11. **Backlinks.** Es la pieza que falta y la más difícil: directorios locales, cámaras de comercio de Morón e Ituzaingó, notas en medios zonales, y sobre todo **un enlace desde cada web que le hacés a un cliente** ("Desarrollado por Tu Negocio En Las Redes"). Esto último es gratis, escalable y probablemente tu mayor activo SEO sin explotar.
12. **Reseñas en Google**, de forma sistemática después de cada proyecto.

---

## 6. Estrategia a 6 meses

### Mes 1 — Que Google entienda que existís
Search Console verificado y sitemap enviado. Google Business Profile publicado. GA4 instalado. Solicitar indexación manual de las 22 URLs. Primeras 5 reseñas.

**Objetivo:** aparecer en el puesto 1 al buscar "Tu Negocio En Las Redes".

### Mes 2 — Ganar lo local
Reforzar las 4 páginas locales con casos reales de cada zona. Ficha de Google con publicaciones semanales y fotos. Sumar Haedo y Ramos Mejía. 2 artículos nuevos. Arrancar el enlace en el pie de las webs de clientes.

**Objetivo:** entrar al bloque de 3 resultados del mapa para "agencia de marketing en Ituzaingó" y similares.

### Mes 3-4 — Autoridad temática
Un artículo cada 2 semanas alrededor de los servicios que más margen dejan. Landings de servicio × localidad para los 3-4 combos con más demanda real (medida en Search Console, no adivinada). Primeros backlinks de directorios y prensa local.

**Objetivo:** primera página para keywords locales de servicio; primeras impresiones para "agencia de marketing digital" a nivel nacional.

### Mes 5-6 — Escalar lo que ya funciona
Con datos reales de Search Console: duplicar el contenido de lo que ya trae impresiones, reescribir lo que trae impresiones pero no clics (es un problema de `title`, no de contenido), y podar lo que no trae nada. Casos de éxito con métricas concretas. Campañas de Google Ads sobre las keywords que el orgánico confirmó que convierten.

**Objetivo:** flujo estable de consultas orgánicas; marca posicionada en Zona Oeste.

### Sobre las keywords más competidas

"marketing digital", "agencia de marketing digital" y "desarrollo web" a nivel nacional compiten contra agencias con años de antigüedad y cientos de backlinks. **No son realistas a 6 meses y perseguirlas de entrada es la forma más rápida de quemar esfuerzo.**

La estrategia correcta es la contraria: dominar primero lo local y lo específico, donde la competencia es baja y la intención de compra es alta. La autoridad que se construye ahí es la que después permite pelear por los términos grandes.

---

## 7. Detalles operativos

### Cómo regenerar el sitio

```bash
python _build/build.py
```

Genera las 16 páginas, regenera `sitemap.xml` y `robots.txt` desde los archivos reales, y estampa el hash de versión en los assets. Correlo **siempre** después de tocar contenido en `_build/`.

### Estructura

- **6 páginas a mano:** `index`, `servicios`, `ia`, `trabajos`, `nosotros`, `contacto`.
- **16 generadas** desde `_build/`.
- El nav y el footer de las generadas están en `_build/chrome.py`. **Si cambiás el nav, cambialo ahí *y* en las 6 a mano.**

### Cosas que no hay que romper

- **El versionado `?v=` de los assets.** La cache es de 1 año e `immutable`. Sin el hash, un cambio de CSS tarda meses en llegarle a los visitantes recurrentes.
- **La tipografía self-hosteada.** Volver a Google Fonts reintroduce 2 orígenes externos en el critical path.
- **`.reveal` bajo `.js`.** Es lo que evita que el sitio quede en blanco si el JS falla.

### Nota sobre `WebSite SearchAction`

Estaba en tu lista de schemas a implementar. **No se implementó a propósito:** ese schema le declara a Google que el sitio tiene un buscador interno, y Google verifica que la URL de búsqueda funcione. Como el sitio no tiene buscador, declararlo sería una señal falsa. Se puede agregar el día que haya búsqueda real.
