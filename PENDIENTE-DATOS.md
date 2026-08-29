# Pendiente de datos

Lo que la web necesita y no se puede escribir sin preguntar. Nada de esto se
inventó ni se dejó como placeholder: las secciones que dependen de estos datos
directamente no se construyeron.

Ordenado por impacto en conversión, de mayor a menor.

> Regla que se siguió en toda la implementación: si un número no se puede
> verificar, no va. Un dato falso descubierto vale menos que no tener dato.

---

| # | Qué falta | Qué dato exacto hace falta | A quién pedírselo | Qué sección espera | Por qué mueve la aguja |
|---|---|---|---|---|---|
| 1 | **Testimonios** | 3 para el home y 5 para /trabajos. De cada uno: nombre y apellido, nombre del negocio, 2-3 líneas escritas por esa persona, y foto o logo. Autorización para publicarlo. | Mundo Cortinas, TonCars, Medisur, GICI, Pasión Matera — los que mejor relación tengan | Home, entre los casos y los servicios (el hueco ya está marcado en `index.html`). Y /trabajos | Hoy hay **cero** pruebas sociales en las 22 páginas: ni un testimonio, ni una reseña, ni una frase de cliente. Es lo único que contesta "¿y por qué te creo?" sin que lo diga la agencia sobre sí misma |
| 2 | **Un resultado numérico por caso** | Un número por proyecto, del tipo: consultas por semana antes y después, unidades publicadas, turnos pedidos por la web, tiempo que tarda ahora en publicar un producto. No hace falta que sea espectacular: hace falta que sea real y chequeable | Los dueños. Si no lo tienen medido, sirve un número propio de la agencia: unidades cargadas, días de entrega, mensajes automatizados por mes | Cuarta línea de cada caso del home. La plantilla ya tiene lugar: **el problema → qué construimos → qué tiene hoy → [falta]** | Los casos hoy cuentan qué se construyó. Sin un número, siguen siendo una descripción de trabajo y no una prueba de resultado |
| 3 | **El "antes" real de cada cliente** | Cómo vendía ese negocio antes de la web: dónde publicaba, cómo contestaba, qué le costaba. Dos o tres frases | Los dueños, en la misma charla del punto 2 | Primera línea de cada caso. Hoy dice el problema **del rubro**, no la historia de ese negocio, porque eso no se puede verificar abriendo el sitio | Un "antes" concreto y ajeno convence mucho más que un problema genérico bien redactado |
| 4 | **Endpoint real para guardar leads** | Una URL que reciba un POST con JSON. Sirve Formspree, un Google Apps Script, una función de Vercel o una tabla de Supabase | Decisión de ustedes. Es media hora de trabajo una vez elegido | `main.js`, constante `LEAD_ENDPOINT` (hoy `''`). El `fetch` ya está escrito detrás del `if`: se pega la URL y se enciende | Hoy, si la persona completa el formulario y cierra la pestaña de WhatsApp antes de tocar enviar, **la consulta desaparece**. No queda registro de que existió |
| 5 | **Rangos de precio** | Un rango por tipo de proyecto: landing, web institucional, tienda online, sistema a medida. "Desde $X" ya sirve | Ustedes | Respuesta de la FAQ "¿cuánto cuesta una página web?", y una página `/precios` | Es la primera pregunta de todos y la web contesta "depende". El que necesita un número y no lo encuentra, se va a buscarlo a otro lado |
| 6 | **Frase textual de un dueño** | Dos líneas escritas por él, con nombre y negocio. Distinto del testimonio del punto 1: esta va adentro del caso | Los mismos dueños | Cierre de cada caso del home | Rompe la objeción de la edad sin nombrarla. Tres clientes hablando bien valen más que cualquier párrafo defensivo en /nosotros |
| 7 | **Captura de una demo real** | Una imagen de una demo entregada de verdad, con permiso de ese cliente para mostrarla | El cliente al que se le hizo | Sección "Demo gratis" del home | La sección explica bien qué llega, pero no lo muestra. Ver una demo real es la diferencia entre entender la oferta y creerla |
| 8 | **Logos de clientes** | Archivo del logo de cada cliente, en PNG con fondo transparente, y permiso escrito para usarlo | Los clientes | Franja de prueba del home, al lado de las capturas | Un logo se reconoce en medio segundo; una captura hay que mirarla. Suma sin ocupar scroll |
| 9 | **Reseñas de Google** | Que el perfil de Google Business esté verificado y tenga reseñas | Requiere terminar la verificación del perfil (dirección postal / video) y después pedirle reseñas a los clientes | Franja de prueba y footer | Aparecen en los resultados de búsqueda, no solo en la web: es la única prueba social que se ve **antes** de entrar al sitio |

---

## Cómo pedirlo

Los puntos 1, 2, 3 y 6 salen todos de la misma conversación. Una llamada de
diez minutos por cliente alcanza para los cuatro:

1. ¿Cómo vendías antes de tener la web? *(punto 3)*
2. ¿Notaste algún cambio desde que está online? ¿Cuántas consultas te entran
   por semana? *(punto 2)*
3. ¿Le recomendarías el trabajo a alguien? ¿Me lo podés escribir en dos
   líneas? *(puntos 1 y 6)*
4. ¿Puedo publicar tu nombre, el del negocio y el logo? *(puntos 1 y 8)*

Con tres clientes que contesten, se completan cinco de las nueve filas.

## Qué se hizo mientras tanto

- El hueco de testimonios está marcado con un comentario en `index.html`, sin
  bloque vacío ni texto de relleno.
- Los casos se escribieron con lo verificable abriendo el sitio del cliente.
- La FAQ de precios sigue contestando "depende" — sin rango inventado.
- `LEAD_ENDPOINT` está vacío, con el `fetch` listo detrás de un `if`.
