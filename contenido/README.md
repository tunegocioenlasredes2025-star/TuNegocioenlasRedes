# Contenido de Instagram — sistema v1

Carpeta de trabajo para @tunegocioenlasredes_. No se publica en la web.

---

## 1. Diagnóstico del feed actual

Mirando la grilla de los últimos ~30 posteos, el problema no es el diseño.
El diseño está bien resuelto. El problema es que **el contenido no puede
distinguirse del de cualquier otra agencia.**

Cinco cosas concretas:

**a) Una sola fórmula, repetida veinte veces.**
"Tu web no vende. Es un folleto caro." · "Tu negocio no trabaja mal. Trabaja
como en 2015." · "Tenés seguidores. No tenés clientes." · "Te comparan por
precio cuando no ven tu valor." · "Tu competencia ya está online."
Es siempre la misma estructura: *negación + acusación + palabra en celeste*.
Funciona la primera vez. A la quinta, el que scrollea ya sabe cómo sigue.

**b) Cero nombres propios.** En toda la grilla no aparece un solo cliente, un
solo barrio, un solo rubro con nombre. Todo es "tu negocio", "las PyMEs",
"tus clientes". Un mensaje que le habla a todos no le habla a nadie.

**c) No se ve nunca el trabajo.** Hay una sola captura real (GICI en Google).
El resto son fotos de banco: piezas de ajedrez, el logo de Apple, laptops
lindas, gráficos de la bolsa, una foto del Mundial. Esas imágenes están
disponibles para cualquiera. Literalmente cualquiera.

**d) El Mundial forzado.** "Lo que la remontada le enseña a tu negocio",
"El gol llegó a los 93, la venta llega con el seguimiento". Es el movimiento
más hecho del marketing argentino. Todos lo hacen la misma semana.

**e) El feed es oscuro y la web nueva es clara.** Quien viene del sitio a
Instagram siente que son dos marcas. Y el azul marino sobre negro es
exactamente el color que usa el 90% de las agencias del rubro.

> Lo más raro de todo: **la web dice cosas mucho mejores que el Instagram.**
> "Diez accesos a WhatsApp en la misma página, y cada consulta entra con el
> vehículo ya elegido en vez de un 'hola, qué precio tiene'." Eso es específico,
> verificable y no lo puede escribir nadie más. El Instagram, en cambio, dice
> "tu web no vende". El contenido bueno ya está escrito: está en `index.html`.

---

## 2. Las cinco reglas anti-genérico

Un posteo no se publica si no pasa las cinco.

| # | Regla | Cómo se chequea |
|---|---|---|
| 1 | **Nombre propio** | ¿Nombra un negocio, un rubro o un barrio? Si sirve igual para una ferretería de Ituzaingó y para una startup de Miami, no va |
| 2 | **Número verificable** | Si hay un número, ¿lo podemos chequear? Si no, se saca. *(Misma regla que se usó en la web — `PENDIENTE-DATOS.md`)* |
| 3 | **Prueba visible** | ¿Podemos mostrar algo real? Captura, chat, pantalla, cara. Si la única imagen posible es una foto de banco, la idea es débil |
| 4 | **Primera persona** | "Hicimos", "nos pasó", "un cliente nos dijo". Nunca "las empresas deben" |
| 5 | **No lo vi antes** | Si el hook ya lo viste en otra cuenta de agencia esta semana, se tira |

---

## 3. Los dos formatos

### Reels → **El Camino del Negocio**
Entrevistas a dueños de PyMEs de barrio. Ver `camino-del-negocio/`.
Primera: Infoseguridad + Mundo Ferretero.

### Estáticas y carruseles → tres pilares

| Pilar | Qué es | Frecuencia | Formato |
|---|---|---|---|
| **Caso real** | Un cliente nuestro, con la estructura de la web: el problema → qué construimos → qué tiene hoy | 1 cada 2 semanas | Carrusel 6-8 slides |
| **El detalle** | Una decisión chiquita de un trabajo real, explicada. Lo que hacemos todos los días y nadie ve | 1 por semana | Estática o carrusel de 3 |
| **Traducción** | Un concepto técnico llevado a lo simple — pero SIEMPRE aterrizado en un negocio concreto | 1 por semana | Carrusel 6-8 slides |

El pilar del medio es el más importante y el que nadie hace. Nadie cuenta por
qué el botón de WhatsApp va diez veces en la misma página. Nosotros sí podemos:
lo decidimos nosotros.

---

## 4. Banco de ideas — listas para producir

Todas salen de trabajo real que ya existe. Ninguna necesita inventar nada.

### Caso real
1. **TonCars** — "El problema no era la web. Era el primer mensaje." Cómo una ficha por unidad cambia la consulta que entra. *(hecho: `carruseles/00-muestra-estilo/`)*
2. **Mundo Cortinas** — "Una black out y una sunscreen no son lo mismo. Si eso no está escrito, lo explicás cincuenta veces por semana."
3. **Medisur** — "Nadie busca 'un centro médico'. Busca el estudio que le pidieron." Por qué una página por estudio, a 2.600 km de acá.
4. **GICI** — "Un contador no compite con otro contador. Compite con el que aparece primero cuando buscás 'contador para monotributo'."
5. **Pasión Matera** — Qué cambia cuando un producto artesanal tiene carrito y no solo un DM.

### El detalle
6. "Por qué en la web de TonCars hay **diez** botones de WhatsApp y no uno."
7. "Por qué escribimos el precio de la cortina antes de que pregunten."
8. "El campo del formulario que sacamos y subió las consultas." *(solo si hay dato real)*
9. "Lo que hace tu web en los 3 segundos que la persona tarda en decidir si se queda." — con captura real, no con una foto de reloj.
10. "Cómo se ve tu negocio en Google Maps a las 11 de la noche."

### Traducción
11. "CRM" sin decir CRM: un día de trabajo de una ferretería con cuaderno vs. con sistema.
12. "Automatización" sin decir automatización: los seis mensajes que mandás todos los días y son siempre el mismo.
13. "SEO local" sin decir SEO: por qué te encuentra el de tu cuadra y no el de Palermo.
14. "IA" sin la foto del robot: las tres cosas puntuales que usamos nosotros esta semana, con captura.

### Derivados de la entrevista
15. Carrusel "5 frases de [nombre]" — 6 slides, tipografía sola, sin foto.
16. Estática con su cara y una frase textual entre comillas.

---

## 5. Cómo se produce

```
python3 contenido/build.py contenido/carruseles/<carpeta>
```

Genera, en la carpeta del carrusel:
- `png/slide-XX.png` — 2160×2700 (retina 2x), listo para subir
- `editable-canva.pdf` — texto vectorial, para importar a Canva
- `png/contacto.png` — hoja de contacto para revisar de un vistazo

Sistema visual y reglas de diseño: `sistema-visual-ig.md`.
