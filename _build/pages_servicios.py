# -*- coding: utf-8 -*-
"""Landings por servicio."""

import chrome as C
import schemas as S
import icons as I
import components as CO


def _prose(inner, cls="section-dark"):
    return f'''
    <section class="{cls}">
        <div class="container">
            <div class="prose reveal">
{inner}
            </div>
        </div>
    </section>
'''


def _page(*, path, title, description, og_title, tag, h1, lead, bread_mid,
          prose, cards, cards_head, faq_items, related_title, related, cta,
          service_kw, extra_sections="", tldr=None, cta_top=None):
    prose = CO.lead_block(prose, tldr, cta_top)
    schema = S.dump([
        S.breadcrumb([("Inicio", "/"), bread_mid[0], (bread_mid[1][0], path)]),
        S.webpage(path, og_title, description),
        S.service(service_kw["name"], service_kw["type"], service_kw["desc"], path,
                  offers=service_kw.get("offers")),
        S.faq(faq_items),
    ])
    return path, (
        C.head(title=title, description=description, path=path, schema=schema, og_title=og_title)
        + C.nav("/servicios")
        + C.breadcrumb([("Inicio", "/"), (bread_mid[0][0], bread_mid[0][1]), (bread_mid[1][0], None)])
        + C.page_hero(tag, h1, lead)
        + _prose(prose)
        + I.grid(cards, tag=cards_head[0], h2=cards_head[1], sub=cards_head[2])
        + extra_sections
        + C.faq_section(faq_items, heading=f'Preguntas sobre<br><span class="gradient-text">{tag.lower()}.</span>')
        + C.related_section(related_title, related)
        + C.cta_section(*cta)
        + C.FOOTER
    )


# ---------------------------------------------------------------- PÁGINAS WEB
def paginas_web():
    faq_items = [
        ("¿Cuánto cuesta una página web en Argentina?",
         "No hay un precio único porque no todos los sitios resuelven lo mismo. Una <strong>landing page</strong> de una sola sección cuesta bastante menos que una web institucional de cinco páginas, y mucho menos que una tienda online con carrito y pagos. Por eso trabajamos al revés: primero te hacemos una <strong>demo gratis</strong> de tu página, la ves funcionando, y recién ahí te pasamos un precio cerrado. Sin adelantos para ver una maqueta y sin costos que aparecen a mitad del proyecto."),
        ("¿En cuánto tiempo tengo mi página web lista?",
         "La <strong>demo la tenés funcionando en menos de 72 horas</strong>. Una vez que la aprobás, una landing page suele quedar publicada en pocos días y una web institucional completa en una o dos semanas. El plazo real depende casi siempre de una sola cosa: la velocidad con la que nos pasás textos, fotos y logo."),
        ("¿La página web va a andar bien en el celular?",
         "Sí, y no es un extra: es el punto de partida. Diseñamos <strong>mobile-first</strong> porque en Argentina la enorme mayoría de las visitas a webs de negocios locales llegan desde el teléfono. Cada sitio se prueba en pantallas chicas antes que en escritorio."),
        ("¿Usan WordPress o plantillas?",
         "No. Desarrollamos con <strong>código propio</strong> (HTML, CSS y JavaScript, o React cuando el proyecto lo pide). Eso significa una web mucho más liviana, más rápida, sin plugins que se rompen, sin actualizaciones que te tumban el sitio y sin cuotas mensuales de licencias. También significa que el diseño es tuyo y no una plantilla que usan otros mil negocios."),
        ("¿La página web viene optimizada para Google?",
         "Sí. Cada sitio sale con <strong>SEO técnico de base</strong>: títulos y descripciones únicos por página, estructura de encabezados correcta, datos estructurados (Schema), sitemap, robots.txt, URLs limpias, imágenes optimizadas y velocidad de carga cuidada. Eso es lo que hace que Google pueda entender e indexar tu sitio."),
        ("¿Me quedo con la página si dejo de trabajar con ustedes?",
         "Sí. La web es tuya. Te entregamos el proyecto y podés llevártelo cuando quieras. No secuestramos dominios ni código."),
        ("¿Incluye dominio y hosting?",
         "Te dejamos todo configurado y funcionando: dominio (.com.ar o .com), certificado SSL y publicación. El hosting de nuestros sitios es muy económico porque al ser webs estáticas y livianas no necesitan servidores caros."),
    ]

    prose = '''                <h2>Una página web que trabaja, no una que solo existe</h2>
                <p>La mayoría de los negocios de Zona Oeste que nos escriben ya tuvieron una página web antes. El problema casi nunca fue que "no tenían web": el problema es que la que tenían no hacía nada. Nadie la encontraba en Google, tardaba ocho segundos en cargar, se veía rota en el celular y no tenía un solo lugar claro donde el visitante pudiera escribir.</p>
                <p>Una página web profesional tiene un trabajo concreto: <strong>convertir a alguien que te está mirando en alguien que te escribe</strong>. Todo lo demás —la estética, las animaciones, la cantidad de secciones— está al servicio de eso.</p>

                <h2>Qué tipo de página web necesita tu negocio</h2>
                <p>No todos los negocios necesitan lo mismo, y venderte de más sería la forma más rápida de que el proyecto no te cierre. Estas son las cuatro opciones reales:</p>
                <h3>Landing page</h3>
                <p>Una sola página, un solo objetivo. Ideal si querés que te escriban por WhatsApp, que reserven un turno o que dejen sus datos. Es la opción más rápida de publicar y la que mejor funciona si vas a hacer <a href="/publicidad-digital">publicidad digital</a>, porque toda la página empuja hacia una única acción.</p>
                <h3>Web institucional</h3>
                <p>Varias secciones: inicio, servicios, trabajos, nosotros, contacto. Es lo que necesitás si querés que tu negocio transmita solidez, si vendés servicios que requieren confianza (estudios contables, consultorios, constructoras) o si querés posicionarte en Google para varias búsquedas distintas. Cada sección puede atacar una palabra clave diferente.</p>
                <h3>Web con catálogo</h3>
                <p>Mostrás productos con fotos, precios y detalles, pero la venta se cierra por WhatsApp. Es el formato que mejor funciona para la mayoría de los comercios de barrio: toda la vidriera online, sin la complejidad de administrar pagos y envíos.</p>
                <h3>Tienda online</h3>
                <p>Carrito, medios de pago y envíos. Si querés vender 24/7 sin intervenir en cada operación, mirá <a href="/tiendas-online">cómo trabajamos las tiendas online</a>.</p>

                <table>
                    <thead>
                        <tr><th>Tipo de web</th><th>Qué resuelve</th><th>Cuándo conviene</th><th>Plazo</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Landing page</strong></td><td>Un solo objetivo: que te escriban, reserven o compren</td><td>Si vas a hacer publicidad o recién arrancás</td><td>Días</td></tr>
                        <tr><td><strong>Web institucional</strong></td><td>Varias secciones que dan solidez a la marca</td><td>Servicios que se eligen por confianza</td><td>1 a 2 semanas</td></tr>
                        <tr><td><strong>Web con catálogo</strong></td><td>Muestra productos; la venta cierra por WhatsApp</td><td>Comercios con muchos productos</td><td>1 a 2 semanas</td></tr>
                        <tr><td><strong>Tienda online</strong></td><td>Carrito, cobro y envíos sin que intervengas</td><td>Volumen alto y productos que no requieren asesoramiento</td><td>3 semanas o más</td></tr>
                    </tbody>
                </table>

                <h2>Cómo trabajamos</h2>
                <ol>
                    <li><strong>Charla inicial.</strong> Entendemos qué hace tu negocio, a quién le vendés y qué querés que pase cuando alguien entra a tu web.</li>
                    <li><strong>Demo gratis en 72 horas.</strong> Te armamos una versión real de tu página, con tu logo y tus colores. No una maqueta en Figma: una web que abrís en el celular y navegás.</li>
                    <li><strong>Ajustes.</strong> Nos decís qué cambiarías. Iteramos hasta que te cierre.</li>
                    <li><strong>Publicación.</strong> Dominio, SSL, sitemap, Google Search Console y analítica. Todo configurado.</li>
                    <li><strong>Seguimiento.</strong> Te mostramos cómo leer los datos y qué ajustar según lo que la gente realmente hace en tu sitio.</li>
                </ol>

                <h2>Por qué no usamos plantillas</h2>
                <p>Una web armada con plantillas y plugins arrastra código que tu negocio no usa. Eso se traduce en algo muy concreto: <strong>carga lenta</strong>. Y la velocidad no es un detalle estético, es un factor de posicionamiento que Google mide directamente a través de las Core Web Vitals, además de ser la principal razón por la que alguien abandona un sitio antes de que termine de abrir.</p>
                <p>Escribimos el código a mano. Nuestros sitios pesan una fracción de lo que pesa una web promedio armada con constructores visuales, cargan casi instantáneamente y no dependen de veinte plugins que hay que mantener actualizados.</p>

                <div class="callout">
                    <p><strong>Antes de decidir nada:</strong> te hacemos la demo de tu página web sin costo. La ves andando, la abrís en tu celular, se la mostrás a quien quieras. Recién después hablamos de plata.</p>
                </div>'''

    cards = [
        ("monitor", "Diseño a medida", "Sin plantillas. El diseño se piensa desde cero para tu rubro, tu marca y tus clientes.", "Código propio"),
        ("smartphone", "Mobile-first", "Se diseña primero para el celular, que es de donde llega la mayoría de tus visitas.", "100% responsive"),
        ("gauge", "Carga en menos de 2 segundos", "Webs estáticas, livianas y sin plugins. Velocidad real, no promesas.", "Core Web Vitals"),
        ("search", "SEO técnico incluido", "Metadatos, Schema, sitemap, URLs limpias e imágenes optimizadas desde el día uno.", "Listo para Google"),
        ("message", "Conversión por WhatsApp", "Botón flotante, mensajes prearmados y CTAs en cada sección para que te escriban.", "Más consultas"),
        ("shield", "Dominio y SSL", "Te dejamos el dominio configurado, el certificado activo y el sitio publicado.", "Todo listo"),
    ]

    return _page(
        path="/paginas-web",
        tldr=[
            "Hay <strong>cuatro tipos de web</strong> y elegir mal es el error más caro: landing, institucional, catálogo o tienda online.",
            "Desarrollamos con <strong>código propio</strong>, no plantillas: sitios más livianos, más rápidos y sin plugins que se rompen.",
            "Cada sitio sale con <strong>SEO técnico de base</strong>: metadatos, Schema, sitemap, URLs limpias e imágenes optimizadas.",
            "Ves una <strong>demo real funcionando en 72 horas</strong> antes de que hablemos de precio.",
        ],
        cta_top=("<strong>Antes de leer todo esto:</strong> te armamos la demo de tu página con tu logo y tus colores, sin costo.",
                 "Quiero mi demo gratis", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"),
        title="Diseño y Desarrollo de Páginas Web | Tu Negocio En Las Redes",
        description="Diseño y desarrollo de páginas web profesionales en Zona Oeste: landing pages, webs institucionales y catálogos. Demo gratis en 72 horas.",
        og_title="Páginas Web Profesionales | Demo Gratis en 72 hs",
        tag="Páginas Web",
        h1='Diseño y desarrollo de<br><span class="gradient-text">páginas web profesionales.</span>',
        lead="Creamos páginas web que generan consultas, no solo visitas. Código propio, carga rápida, mobile-first y optimizadas para Google desde el primer día. Te mostramos una demo gratis de tu sitio antes de que decidas nada.",
        bread_mid=(("Servicios", "/servicios"), ("Páginas Web",)),
        prose=prose,
        cards=cards,
        cards_head=("Qué incluye", 'Todo lo que trae<br><span class="gradient-text">tu página web.</span>',
                    "No son extras que se cobran aparte. Es el estándar con el que entregamos cada sitio."),
        faq_items=faq_items,
        related_title='Servicios que se<br><span class="gradient-text">complementan.</span>',
        related=[
            ("/tiendas-online", "Tiendas online", "Si además de mostrar querés cobrar online, con carrito y medios de pago."),
            ("/publicidad-digital", "Publicidad digital", "Tu web lista más campañas en Meta y Google para traerle tráfico desde el día uno."),
            ("/marketing-digital-ituzaingo", "Páginas web en Ituzaingó", "Cómo trabajamos con los comercios y profesionales de la zona."),
            ("/trabajos", "Ver trabajos reales", "Doce sitios que desarrollamos y están online funcionando hoy."),
        ],
        cta=('¿Cómo se vería tu negocio con una web<br>que <span class="gradient-text">vende de verdad?</span>',
             "Te hacemos una demo real de tu página web, con tu logo y tus colores, sin costo y sin compromiso.<br>La ves funcionando antes de decidir cualquier cosa.",
             "Quiero mi demo gratis →", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"),
        service_kw={
            "name": "Diseño y Desarrollo de Páginas Web",
            "type": "Desarrollo Web",
            "desc": "Diseño y desarrollo de páginas web profesionales a medida: landing pages, sitios institucionales y catálogos online, con SEO técnico y optimización de velocidad.",
            "offers": ["Landing page", "Web institucional", "Web con catálogo de productos",
                       "Rediseño de sitio existente", "Optimización de velocidad y SEO técnico"],
        },
    )


# --------------------------------------------------------------- TIENDAS ONLINE
def tiendas_online():
    faq_items = [
        ("¿Cuánto cuesta hacer una tienda online?",
         "Una tienda online cuesta más que una web común porque hay que integrar catálogo, carrito, medios de pago y envíos, y porque después hay que poder administrarla. Como siempre, te armamos la <strong>demo gratis</strong> con algunos de tus productos cargados y recién ahí te pasamos el precio cerrado."),
        ("¿Puedo cargar y modificar los productos yo mismo?",
         "Sí. Te dejamos un <strong>panel de administración</strong> desde el que cargás productos, cambiás precios, marcás sin stock y subís fotos sin tocar una línea de código ni depender de nosotros para cada cambio."),
        ("¿Con qué medios de pago funciona?",
         "Integramos <strong>Mercado Pago</strong>, que es lo que usa prácticamente todo el mundo en Argentina y permite tarjeta, débito, dinero en cuenta y cuotas. También podemos habilitar transferencia bancaria y pago contra entrega según cómo trabajes."),
        ("¿Y los envíos?",
         "Configuramos costos de envío por zona, retiro en local y, si te sirve, integración con correo. Muchos comercios de la zona arrancan con envío propio en el radio cercano y retiro en el local: es lo más simple y lo que menos margen te come."),
        ("¿Me conviene una tienda online o un catálogo con WhatsApp?",
         "Depende del volumen. Si vendés pocas unidades de ticket alto y te gusta asesorar en la conversación, un <strong>catálogo con WhatsApp</strong> te alcanza y es más barato. Si vendés muchas unidades, productos que no requieren explicación, o te cansaste de responder \"¿cuánto sale?\" cien veces por día, la tienda online se paga sola. Te ayudamos a decidir sin empujarte a la opción más cara."),
        ("¿La tienda aparece en Google?",
         "Sí. Cada producto y cada categoría se publica con su propia URL, su título y sus datos estructurados de tipo Product, que es lo que permite que Google muestre precio y disponibilidad directamente en los resultados de búsqueda."),
    ]

    prose = '''                <h2>Vender online sin depender de responder mensajes</h2>
                <p>El techo de vender por WhatsApp aparece siempre en el mismo punto: llega un momento en el que el negocio no crece porque vos no das abasto. Cada venta requiere que alguien conteste "¿tenés talle M?", "¿cuánto sale?", "¿hacés envío a Castelar?". Multiplicá eso por cincuenta consultas diarias y el problema deja de ser conseguir clientes: el problema es atenderlos.</p>
                <p>Una <strong>tienda online</strong> resuelve exactamente eso. El cliente entra, ve stock y precio actualizado, elige, paga y recibe su comprobante. Vos aparecés recién cuando hay que preparar el pedido.</p>

                <h2>Qué te dejamos funcionando</h2>
                <p>Una tienda online no es un catálogo con un botón de pagar. Para que funcione de verdad tiene que resolver el circuito completo:</p>
                <ul>
                    <li><strong>Catálogo administrable</strong> con categorías, variantes (talle, color, medida) y control de stock.</li>
                    <li><strong>Carrito y checkout</strong> pensados para que no se caiga la venta en el último paso, que es donde se pierde la mayoría de las compras.</li>
                    <li><strong>Mercado Pago integrado</strong>, con tarjeta, débito y cuotas.</li>
                    <li><strong>Cálculo de envío</strong> por zona, con opción de retiro en el local.</li>
                    <li><strong>Panel de administración</strong> para que cargues productos y veas tus pedidos sin depender de nadie.</li>
                    <li><strong>Avisos automáticos</strong> al cliente y a vos cuando entra una compra.</li>
                </ul>

                <h2>Tienda propia o Mercado Libre: no es lo mismo</h2>
                <p>Mercado Libre te da tráfico, y eso es real. Pero también te cobra una comisión sobre cada venta, te pone a competir por precio contra otros vendedores dentro de la misma pantalla y, sobre todo, <strong>no te deja construir marca</strong>: el cliente le compró a Mercado Libre, no a vos, y la próxima vez va a buscar el producto, no tu nombre.</p>
                <p>Una tienda propia no reemplaza a Mercado Libre: la mayoría de nuestros clientes usan las dos. La diferencia es que en la tuya el margen es tuyo, los datos de tus clientes son tuyos y la experiencia de compra la definís vos.</p>

                <table>
                    <thead>
                        <tr><th></th><th>Tienda propia</th><th>Mercado Libre</th><th>Catálogo + WhatsApp</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Comisión por venta</strong></td><td>Ninguna</td><td>Sí, sobre cada venta</td><td>Ninguna</td></tr>
                        <tr><td><strong>Tráfico</strong></td><td>Lo traés vos</td><td>Ya lo tiene la plataforma</td><td>Lo traés vos</td></tr>
                        <tr><td><strong>Marca</strong></td><td>Es tuya</td><td>Competís dentro de la plataforma</td><td>Es tuya</td></tr>
                        <tr><td><strong>Datos del cliente</strong></td><td>Tuyos</td><td>De la plataforma</td><td>Tuyos</td></tr>
                        <tr><td><strong>Atención por venta</strong></td><td>Automática</td><td>Automática</td><td>Manual</td></tr>
                    </tbody>
                </table>

                <h2>Una tienda sin visitas no vende</h2>
                <p>Esto es lo que casi nadie te dice antes de venderte un ecommerce: publicar la tienda es la mitad del trabajo. Si nadie la visita, no hay conversión posible. Por eso cada tienda sale con <strong>SEO de producto</strong> (URLs propias, datos estructurados de precio y stock) y, si tiene sentido para tu negocio, la combinamos con <a href="/publicidad-digital">campañas de publicidad digital</a> y <a href="/gestion-de-redes">gestión de redes</a> para llevarle tráfico desde el primer mes.</p>

                <div class="callout">
                    <p><strong>Te lo mostramos con tus productos:</strong> armamos la demo con algunos de tus artículos reales cargados, para que veas cómo se ve tu tienda antes de invertir un peso.</p>
                </div>'''

    cards = [
        ("cart", "Carrito y checkout", "Proceso de compra corto y claro, diseñado para que no se caiga la venta al final.", "Menos abandono"),
        ("credit", "Mercado Pago", "Tarjeta, débito, dinero en cuenta y cuotas. Lo que tus clientes ya usan.", "Cobro integrado"),
        ("package", "Stock y variantes", "Talles, colores y medidas con control de stock real por variante.", "Sin sobreventa"),
        ("map", "Envíos por zona", "Costos por zona, retiro en local y avisos automáticos al cliente.", "Logística clara"),
        ("layers", "Panel propio", "Cargá productos, cambiá precios y mirá tus pedidos sin depender de nadie.", "Autogestionable"),
        ("search", "SEO de producto", "Cada producto con su URL, su título y datos estructurados de precio y stock.", "Indexable"),
    ]

    return _page(
        path="/tiendas-online",
        tldr=[
            "El techo de vender por WhatsApp no es conseguir clientes: es <strong>no dar abasto para atenderlos</strong>.",
            "Te dejamos el circuito completo: catálogo con stock, carrito, <strong>Mercado Pago</strong>, envíos por zona y panel propio.",
            "Una tienda propia no reemplaza a Mercado Libre: la diferencia es que <strong>el margen y los datos son tuyos</strong>.",
            "Publicar la tienda es la mitad del trabajo: sin visitas no hay conversión posible.",
        ],
        cta_top=("<strong>Te lo mostramos con tus productos:</strong> armamos la demo con algunos de tus artículos reales cargados.",
                 "Quiero ver mi tienda", "Quiero%20una%20demo%20de%20tienda%20online"),
        title="Tiendas Online y E-commerce a Medida | Tu Negocio En Las Redes",
        description="Desarrollo de tiendas online y ecommerce en Zona Oeste: carrito, Mercado Pago, control de stock, envíos y panel propio. Demo gratis con tus productos cargados.",
        og_title="Tiendas Online y E-commerce | Demo Gratis",
        tag="Tiendas Online",
        h1='Tiendas online que<br><span class="gradient-text">venden solas.</span>',
        lead="Desarrollamos tu ecommerce completo: catálogo con stock, carrito, Mercado Pago, envíos por zona y panel de administración propio. Para que dejes de vender contestando mensajes uno por uno.",
        bread_mid=(("Servicios", "/servicios"), ("Tiendas Online",)),
        prose=prose,
        cards=cards,
        cards_head=("Qué incluye", 'Todo el circuito<br><span class="gradient-text">de venta resuelto.</span>',
                    "Del catálogo al cobro y del cobro al envío. Sin partes sueltas."),
        faq_items=faq_items,
        related_title='Para que tu tienda<br><span class="gradient-text">reciba visitas.</span>',
        related=[
            ("/publicidad-digital", "Publicidad digital", "Campañas de Meta y Google que le traen compradores a tu tienda."),
            ("/gestion-de-redes", "Gestión de redes", "Contenido que sostiene la marca y alimenta el tráfico orgánico."),
            ("/paginas-web", "Páginas web", "Si todavía no necesitás cobrar online, quizás te alcance con un catálogo."),
            ("/crm-para-pymes", "CRM para PyMEs", "Para ordenar clientes, pedidos y seguimiento cuando el volumen crece."),
        ],
        cta=('¿Y si tus clientes pudieran comprarte<br><span class="gradient-text">sin escribirte?</span>',
             "Te armamos la demo de tu tienda online con algunos de tus productos reales cargados.<br>Sin costo y sin compromiso.",
             "Quiero mi tienda online →", "Quiero%20una%20demo%20de%20tienda%20online"),
        service_kw={
            "name": "Desarrollo de Tiendas Online y E-commerce",
            "type": "E-commerce",
            "desc": "Desarrollo de tiendas online a medida con carrito, integración de Mercado Pago, control de stock, cálculo de envíos y panel de administración.",
            "offers": ["Tienda online completa", "Catálogo con carrito", "Integración de Mercado Pago",
                       "Panel de administración de productos", "Migración desde otra plataforma"],
        },
    )


# -------------------------------------------------------------- GESTIÓN DE REDES
def gestion_de_redes():
    faq_items = [
        ("¿Cuánto cuesta la gestión de redes sociales?",
         "Depende de cuántas publicaciones y qué formatos incluya el plan, y de si necesitás producción de fotos y video o trabajamos con material que ya tenés. Armamos el plan según lo que tu negocio realmente necesita: no vendemos paquetes cerrados de \"20 posts\" que después nadie sabe para qué sirven."),
        ("¿Qué diferencia hay entre un community manager y una agencia?",
         "Un <strong>community manager</strong> publica y responde. Una agencia además define la estrategia: qué se dice, a quién, con qué objetivo y cómo se mide si funcionó. La diferencia se nota en el resultado: publicar todos los días sin estrategia genera movimiento, no clientes."),
        ("¿Ustedes producen el contenido o lo tengo que mandar yo?",
         "Producimos. Diseñamos las piezas, escribimos los copys, armamos los guiones de reels y editamos. Cuando hace falta material propio del negocio (fotos de productos, del local, del equipo), coordinamos una jornada de producción o te damos indicaciones concretas para que lo grabes vos con el celular."),
        ("¿En cuánto tiempo se ven resultados en Instagram?",
         "Los primeros movimientos de alcance y guardados se ven en <strong>tres a cuatro semanas</strong>. El crecimiento sostenido de seguidores y, sobre todo, de consultas reales, se consolida entre el <strong>segundo y el tercer mes</strong>. Cualquiera que te prometa resultados en dos semanas te está vendiendo humo."),
        ("¿Responden los mensajes y comentarios?",
         "Podemos hacerlo, y en muchos casos conviene combinarlo con <a href=\"/automatizacion-whatsapp\">automatización</a>: el bot responde al instante las preguntas repetidas (precios, horarios, ubicación) y las consultas que valen la pena llegan a una persona. Así nadie espera y vos no vivís pegado al teléfono."),
        ("¿Sirve para mi rubro?",
         "Trabajamos con gastronomía, indumentaria, gimnasios, estética, salud, servicios profesionales, comercios de barrio y eventos. Lo que cambia entre rubros no es si sirve, sino qué formato funciona: un gimnasio necesita reels de rutinas y transformaciones, un estudio contable necesita contenido que explique y genere autoridad."),
    ]

    prose = '''                <h2>Publicar no es lo mismo que crecer</h2>
                <p>La mayoría de los negocios que nos escriben no tienen un problema de constancia: publican. El problema es que publican sin que exista una razón detrás de cada pieza. Suben una foto del producto, una frase motivacional, un feliz día del amigo. El feed se llena, la cuenta no crece y, lo más importante, <strong>no entra ni una consulta</strong>.</p>
                <p>La gestión de redes que sirve arranca antes del diseño: arranca definiendo qué querés que pase. Si el objetivo es que reserven turnos, el contenido tiene que empujar reservas. Si el objetivo es que te conozcan en el barrio, tiene que optimizar alcance local. Son dos estrategias distintas y se ven distinto.</p>

                <h2>Cómo armamos la estrategia</h2>
                <h3>1. Diagnóstico</h3>
                <p>Miramos tu cuenta, tu competencia directa en la zona y qué está funcionando en tu rubro hoy. No en abstracto: qué formatos, qué duraciones, qué ganchos.</p>
                <h3>2. Sistema visual</h3>
                <p>Definimos paleta, tipografías y plantillas para que tu cuenta se reconozca de un vistazo. Esto no es capricho estético: una identidad consistente es lo que hace que alguien que te vio tres veces en el feed se acuerde de tu nombre.</p>
                <h3>3. Pilares de contenido</h3>
                <p>Definimos tres o cuatro tipos de publicación que se repiten con lógica: contenido que educa, contenido que muestra el producto o servicio, prueba social (clientes, resultados, reseñas) y contenido que vende directo. La proporción entre ellos cambia según el rubro.</p>
                <h3>4. Producción y publicación</h3>
                <p>Diseñamos, escribimos y programamos. Vos aprobás antes de que salga.</p>
                <h3>5. Medición</h3>
                <p>Alcance, guardados, compartidos, visitas al perfil y clics al WhatsApp. Los guardados y los compartidos importan más que los likes, porque son las señales que Instagram usa para decidir a cuánta gente nueva mostrarte.</p>

                <h2>Reels: el formato que todavía regala alcance</h2>
                <p>Instagram sigue premiando el video corto con alcance orgánico que ningún otro formato te da. Para un negocio local eso es enorme: es la forma más barata que existe hoy de que te vea gente de tu zona que no te sigue.</p>
                <p>Un reel que funciona necesita tres cosas: un <strong>gancho en los primeros dos segundos</strong>, una razón para quedarse hasta el final y algo que empuje a guardar o compartir. Producimos los guiones con esa estructura, no grabando lo que salga.</p>

                <h2>Redes e Instagram no reemplazan a tu web</h2>
                <p>Instagram te da alcance, pero es un terreno alquilado: no controlás el algoritmo, no te llevás a tus seguidores si mañana te cierran la cuenta y no aparecés en Google cuando alguien busca tu servicio. Por eso la combinación que mejor funciona para un negocio local es <strong>redes que generan atención + <a href="/paginas-web">página web propia</a> que convierte y posiciona</strong>.</p>

                <div class="callout">
                    <p><strong>Antes de contratar nada:</strong> escribinos y te hacemos un diagnóstico gratis de tu cuenta, con tres cosas concretas que podés cambiar esta semana aunque no trabajes con nosotros.</p>
                </div>'''

    cards = [
        ("pen", "Estrategia y copywriting", "Pilares de contenido y textos escritos para generar consultas, no likes.", "Con objetivo"),
        ("sparkles", "Diseño de piezas", "Sistema visual propio: paleta, tipografías y plantillas reconocibles.", "Identidad consistente"),
        ("camera", "Reels y video corto", "Guiones con gancho en los primeros 2 segundos y edición completa.", "Alcance orgánico"),
        ("calendar", "Calendario y publicación", "Planificamos el mes, vos aprobás y nosotros publicamos.", "Constancia real"),
        ("users", "Comunidad", "Respuesta a comentarios y mensajes, combinable con automatización.", "Sin dejar a nadie esperando"),
        ("chart", "Reporte mensual", "Alcance, guardados, visitas al perfil y clics al WhatsApp. Con lectura, no solo números.", "Medible"),
    ]

    return _page(
        path="/gestion-de-redes",
        tldr=[
            "Si publicás seguido y no entra ninguna consulta, el problema no es la frecuencia: es que <strong>el contenido no pide una acción</strong>.",
            "Los <strong>guardados y compartidos</strong> pesan más que los likes: son la señal que usa Instagram para mostrarte a gente nueva.",
            "Los reels siguen regalando alcance orgánico, pero necesitan <strong>gancho en los primeros dos segundos</strong>.",
            "Primeros movimientos de alcance en 3 o 4 semanas; consultas sostenidas entre el segundo y el tercer mes.",
        ],
        cta_top=("<strong>Diagnóstico gratis:</strong> miramos tu cuenta y te damos tres cambios concretos para aplicar esta semana.",
                 "Quiero mi diagnóstico", "Quiero%20un%20diagn%C3%B3stico%20de%20mis%20redes"),
        title="Gestión de Redes Sociales e Instagram | Tu Negocio En Las Redes",
        description="Gestión de redes sociales en Zona Oeste: estrategia, diseño, reels y reportes. Manejo de Instagram que genera consultas, no solo likes.",
        og_title="Gestión de Redes e Instagram para Negocios",
        tag="Gestión de Redes",
        h1='Gestión de redes que<br><span class="gradient-text">trae clientes.</span>',
        lead="Estrategia, diseño, reels y copywriting para que tu Instagram deje de ser una vidriera vacía y empiece a generar consultas reales. Con reportes que muestran qué funcionó y por qué.",
        bread_mid=(("Servicios", "/servicios"), ("Gestión de Redes",)),
        prose=prose,
        cards=cards,
        cards_head=("Qué incluye", 'Lo que hacemos<br><span class="gradient-text">todos los meses.</span>',
                    "El plan se arma según tu rubro y tu objetivo. Estos son los bloques con los que trabajamos."),
        faq_items=faq_items,
        related_title='Lo que potencia<br><span class="gradient-text">tus redes.</span>',
        related=[
            ("/publicidad-digital", "Publicidad digital", "Poner presupuesto detrás del contenido que ya demostró funcionar."),
            ("/automatizacion-whatsapp", "Automatización de WhatsApp", "Para que las consultas que generan tus redes no queden sin respuesta."),
            ("/paginas-web", "Páginas web", "El lugar propio al que llevás el tráfico que generan tus redes."),
            ("/blog/como-conseguir-clientes-por-instagram", "Cómo conseguir clientes por Instagram", "Guía práctica con lo que aplicamos en las cuentas que gestionamos."),
        ],
        cta=('¿Y si tu Instagram<br><span class="gradient-text">te trajera clientes?</span>',
             "Escribinos y te hacemos un diagnóstico gratis de tu cuenta,<br>con tres cambios concretos que podés aplicar esta misma semana.",
             "Quiero mi diagnóstico gratis →", "Quiero%20un%20diagn%C3%B3stico%20de%20mis%20redes"),
        service_kw={
            "name": "Gestión de Redes Sociales",
            "type": "Community Management",
            "desc": "Gestión integral de redes sociales: estrategia de contenido, diseño de piezas, producción de reels, copywriting, publicación y reportes mensuales.",
            "offers": ["Gestión de Instagram", "Producción de reels", "Diseño de piezas y carruseles",
                       "Copywriting y calendario de contenido", "Reportes de métricas"],
        },
    )


# ------------------------------------------------------------ PUBLICIDAD DIGITAL
def publicidad_digital():
    faq_items = [
        ("¿Cuánto tengo que invertir en publicidad?",
         "Son dos costos distintos: el <strong>presupuesto de pauta</strong> (lo que le pagás a Meta o Google, y que va directo a mostrar tus anuncios) y el <strong>honorario de gestión</strong>. Para un negocio local, una inversión diaria chica y sostenida suele rendir bastante mejor que un pico de una semana y después nada. Definimos el número con vos según el margen de lo que vendés y cuántas consultas necesitás por mes."),
        ("¿Meta Ads o Google Ads?",
         "Resuelven cosas distintas. <strong>Google Ads</strong> captura demanda que ya existe: alguien busca \"cerrajería en Morón\" ahora mismo y necesita resolverlo hoy. <strong>Meta Ads</strong> (Instagram y Facebook) genera demanda: le muestra tu negocio a gente que no te estaba buscando pero que encaja con tu cliente ideal. Si vendés algo urgente, Google. Si vendés algo que se decide mirando, Meta. Muchas veces conviene combinar."),
        ("¿En cuánto tiempo veo resultados?",
         "Las primeras consultas suelen aparecer en los <strong>primeros días</strong>. Pero los primeros siete a catorce días son de aprendizaje: la plataforma está probando a quién mostrarle tus anuncios. Los datos confiables para optimizar aparecen recién después de esa fase. Cortar una campaña a los cinco días es la forma más común de tirar el presupuesto."),
        ("¿Necesito una página web para hacer publicidad?",
         "No es obligatorio —se puede mandar el tráfico directo a WhatsApp— pero cambia mucho el resultado. Una <a href=\"/paginas-web\">landing page</a> te deja explicar mejor, filtrar consultas que no van a comprar y medir con precisión qué anuncio generó qué. Sin eso, estás optimizando a ciegas."),
        ("¿Puedo saber cuánto me costó cada cliente?",
         "Sí, y es exactamente lo que medimos. Configuramos el seguimiento de conversiones para saber <strong>cuánto costó cada consulta</strong> y, cuando el circuito lo permite, cuántas de esas consultas terminaron en venta. Sin eso, la publicidad es una apuesta."),
        ("¿Se puede segmentar solo a mi zona?",
         "Sí, y para un negocio local es clave. Podemos mostrar los anuncios únicamente en un radio determinado alrededor de tu local, o solo en Ituzaingó, Morón y Castelar. No tiene sentido pagar por mostrarle tu peluquería de Castelar a alguien de Quilmes."),
    ]

    prose = '''                <h2>Publicidad que se mide, no que se gasta</h2>
                <p>La mayoría de los negocios que probaron publicidad digital y les fue mal cometieron el mismo error: pusieron plata en "promocionar publicación". Ese botón es la forma más cara y menos precisa de anunciar. No te deja segmentar bien, no optimiza para conversiones y no te dice cuánto te costó cada consulta.</p>
                <p>Una campaña bien armada arranca por otro lado: <strong>a quién le hablás, qué le ofrecés y qué querés que haga</strong>. Recién después viene el presupuesto.</p>

                <h2>Google Ads: capturar demanda que ya existe</h2>
                <p>Cuando alguien busca "electricista urgente Ituzaingó" o "gimnasio en Castelar", ya decidió que necesita el servicio. Solo está eligiendo a quién. Google Ads te pone adelante de esa persona en el momento exacto.</p>
                <p>Es el canal con la intención de compra más alta que existe, y por eso suele ser el que mejor convierte para servicios. Trabajamos las campañas de búsqueda con palabras clave locales, anuncios que responden a lo que la persona buscó y <strong>palabras clave negativas</strong> para no pagar por clics que nunca iban a comprar.</p>

                <h2>Meta Ads: generar demanda donde no la había</h2>
                <p>En Instagram y Facebook nadie está buscando tu negocio. Están mirando el celular. Tu anuncio tiene que ganarse la atención en el primer segundo y dar una razón concreta para frenar el scroll.</p>
                <p>Es el canal ideal para productos que se venden mostrándolos: gastronomía, indumentaria, estética, gimnasios, eventos. También es donde mejor funciona el <strong>remarketing</strong>: volver a impactar a quien ya visitó tu web o vio tu video y no terminó de escribirte. Esa audiencia es la más barata y la que más convierte, y es la que casi nadie trabaja.</p>

                <table>
                    <thead>
                        <tr><th></th><th>Google Ads</th><th>Meta Ads</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Qué resuelve</strong></td><td>Captura demanda que ya existe</td><td>Genera demanda donde no la había</td></tr>
                        <tr><td><strong>Intención de compra</strong></td><td>Alta: ya te está buscando</td><td>Baja: está mirando el celular</td></tr>
                        <tr><td><strong>Mejor para</strong></td><td>Servicios urgentes y búsquedas concretas</td><td>Productos que se venden mostrándolos</td></tr>
                        <tr><td><strong>Costo por clic</strong></td><td>Más alto</td><td>Más bajo</td></tr>
                        <tr><td><strong>Velocidad</strong></td><td>Rápida</td><td>Media: necesita fase de aprendizaje</td></tr>
                    </tbody>
                </table>

                <h2>Qué hacemos concretamente</h2>
                <ol>
                    <li><strong>Configuración técnica.</strong> Pixel de Meta, etiqueta de Google, eventos de conversión y verificación de dominio. Si esto está mal, todo lo demás mide mal.</li>
                    <li><strong>Investigación.</strong> Palabras clave reales de tu rubro y tu zona, y análisis de lo que están anunciando tus competidores.</li>
                    <li><strong>Creatividades.</strong> Imágenes, videos y textos de anuncio. Siempre varias versiones para poder comparar.</li>
                    <li><strong>Segmentación.</strong> Zona geográfica, intereses, audiencias similares y públicos de remarketing.</li>
                    <li><strong>Optimización semanal.</strong> Pausar lo que no rinde, escalar lo que rinde, rotar creatividades antes de que se desgasten.</li>
                    <li><strong>Reporte claro.</strong> Cuánto se invirtió, cuántas consultas entraron y cuánto costó cada una. En castellano, sin capturas de paneles que no significan nada.</li>
                </ol>

                <div class="callout">
                    <p><strong>Importante:</strong> si tu negocio todavía no tiene dónde recibir bien las consultas, la publicidad amplifica el problema. Antes de recomendarte pauta te vamos a decir con franqueza si primero conviene resolver la <a href="/paginas-web">web</a> o la <a href="/automatizacion-whatsapp">respuesta automática</a>.</p>
                </div>'''

    cards = [
        ("search", "Google Ads", "Aparecés cuando alguien de tu zona busca exactamente lo que vendés.", "Alta intención"),
        ("megaphone", "Meta Ads", "Instagram y Facebook para llegar a quien todavía no te conoce.", "Genera demanda"),
        ("refresh", "Remarketing", "Volvés a impactar a quien ya te visitó y no terminó de escribirte.", "El público más barato"),
        ("map", "Segmentación local", "Radio alrededor de tu local o localidades puntuales de Zona Oeste.", "Sin desperdicio"),
        ("target", "Seguimiento de conversiones", "Pixel y eventos configurados para saber qué anuncio trajo qué consulta.", "Todo medido"),
        ("chart", "Reporte de costo por consulta", "Cuánto invertiste, cuántas consultas entraron y cuánto salió cada una.", "Sin humo"),
    ]

    return _page(
        path="/publicidad-digital",
        tldr=[
            "El botón de promocionar publicación es la forma <strong>más cara y menos precisa</strong> de anunciar.",
            "<strong>Google Ads captura demanda</strong> que ya existe; <strong>Meta Ads genera demanda</strong> nueva. Resuelven cosas distintas.",
            "El <strong>remarketing</strong> es la audiencia más barata y la que más convierte, y es la que casi nadie trabaja.",
            "Los primeros 7 a 14 días son de aprendizaje: cortar antes es tirar el presupuesto.",
        ],
        cta_top=("<strong>¿Sabés cuánto te cuesta cada cliente hoy?</strong> Si no lo sabés, ese es exactamente el problema.",
                 "Analizar mis campañas", "Quiero%20hacer%20publicidad%20para%20mi%20negocio"),
        title="Meta Ads y Google Ads | Tu Negocio En Las Redes",
        description="Campañas de Meta Ads y Google Ads para negocios de Zona Oeste: segmentación local, remarketing y reporte de costo por consulta.",
        og_title="Publicidad Digital: Meta Ads y Google Ads",
        tag="Publicidad Digital",
        h1='Campañas que traen<br><span class="gradient-text">clientes, no clics.</span>',
        lead="Publicidad en Google, Instagram y Facebook con segmentación local, seguimiento de conversiones y reporte claro de cuánto te costó cada consulta. Nada de promocionar publicaciones y cruzar los dedos.",
        bread_mid=(("Servicios", "/servicios"), ("Publicidad Digital",)),
        prose=prose,
        cards=cards,
        cards_head=("Qué incluye", 'Cómo trabajamos<br><span class="gradient-text">tus campañas.</span>',
                    "Configuración técnica, creatividades, optimización semanal y reportes que se entienden."),
        faq_items=faq_items,
        related_title='Para que la pauta<br><span class="gradient-text">rinda de verdad.</span>',
        related=[
            ("/paginas-web", "Landing pages", "El destino que hace que el tráfico pago se convierta en consultas."),
            ("/automatizacion-whatsapp", "Automatización de WhatsApp", "Para responder al instante las consultas que trae la pauta."),
            ("/gestion-de-redes", "Gestión de redes", "Contenido orgánico que sostiene la marca entre campaña y campaña."),
            ("/crm-para-pymes", "CRM para PyMEs", "Para no perder el seguimiento de los leads que generan tus campañas."),
        ],
        cta=('¿Cuánto te está costando<br><span class="gradient-text">cada cliente hoy?</span>',
             "Si no lo sabés, ese es exactamente el problema. Escribinos y lo revisamos juntos,<br>sin costo y sin compromiso.",
             "Quiero analizar mis campañas →", "Quiero%20hacer%20publicidad%20para%20mi%20negocio"),
        service_kw={
            "name": "Publicidad Digital (Meta Ads y Google Ads)",
            "type": "Publicidad Digital",
            "desc": "Gestión de campañas de publicidad digital en Google Ads y Meta Ads con segmentación local, remarketing, seguimiento de conversiones y reportes de costo por consulta.",
            "offers": ["Campañas de Google Ads", "Campañas de Meta Ads", "Remarketing",
                       "Configuración de pixel y conversiones", "Optimización y reportes mensuales"],
        },
    )


# --------------------------------------------------------- AUTOMATIZACIÓN WHATSAPP
def automatizacion_whatsapp():
    faq_items = [
        ("¿Qué es exactamente un chatbot de WhatsApp?",
         "Es un sistema conectado a tu número de WhatsApp que responde automáticamente a quien te escribe. Puede dar precios, horarios y ubicación, mostrar el catálogo, tomar un pedido o agendar un turno, las 24 horas. Cuando la consulta se complica o el cliente lo pide, <strong>le pasa la conversación a una persona</strong> sin que se pierda el hilo."),
        ("¿El cliente se da cuenta de que le habla un bot?",
         "Se lo aclaramos, y eso es a propósito: la gente tolera perfectamente un bot que resuelve rápido, pero se enoja mucho si siente que la engañaron. Lo que sí hacemos es cuidar el tono para que hable como tu negocio y no como un formulario."),
        ("¿Se puede conectar con IA de verdad?",
         "Sí. Hay dos niveles. Un <strong>bot por menú</strong> (el cliente elige opciones) es más barato, predecible y suficiente para muchos negocios. Un <strong>bot con inteligencia artificial</strong> entiende preguntas escritas libremente y responde con la información real de tu negocio. Recomendamos IA cuando recibís muchas consultas distintas y poco previsibles."),
        ("¿Me van a bloquear el número?",
         "No, si se hace bien. Trabajamos sobre la <strong>API oficial de WhatsApp Business</strong>, que es la vía habilitada por Meta para esto. Los bloqueos les pasan a quienes usan herramientas no oficiales para mandar mensajes masivos no solicitados."),
        ("¿Qué pasa si el bot no sabe responder algo?",
         "Deriva a una persona. Se configura un umbral: si el cliente pregunta algo fuera del alcance, pide hablar con alguien, o el bot detecta que se está trabando, la conversación pasa a vos con todo el historial. El objetivo no es que el bot conteste todo: es que conteste lo repetitivo."),
        ("¿Cuánto tiempo lleva implementarlo?",
         "Un bot por menú suele estar funcionando en <strong>una a dos semanas</strong>. Uno con IA y conexión a catálogo o sistema de turnos lleva algo más, porque hay que cargar y ordenar la información con la que va a responder."),
    ]

    prose = '''                <h2>El 80% de los mensajes que respondés son los mismos cinco</h2>
                <p>Hacé la prueba: abrí WhatsApp y mirá las últimas veinte conversaciones de tu negocio. Casi con seguridad, la enorme mayoría son alguna versión de "¿cuánto sale?", "¿a qué hora abren?", "¿dónde están?", "¿hacen envíos?" y "¿tenés turno para esta semana?".</p>
                <p>Esas respuestas no requieren tu criterio. Requieren tu tiempo, que es distinto. Y tienen un costo oculto todavía peor: <strong>la consulta que llega a las once de la noche y contestás a las nueve de la mañana ya compró en otro lado</strong>. En servicios locales, el que responde primero se lleva una parte enorme de las ventas.</p>

                <h2>Qué puede resolver solo</h2>
                <ul>
                    <li><strong>Precios y planes:</strong> responder al instante, con la lista siempre actualizada.</li>
                    <li><strong>Horarios y ubicación:</strong> incluso el mapa y cómo llegar.</li>
                    <li><strong>Catálogo:</strong> mostrar productos con foto y precio dentro de la conversación.</li>
                    <li><strong>Turnos y reservas:</strong> mostrar disponibilidad y agendar directamente.</li>
                    <li><strong>Estado de pedido:</strong> el cliente consulta solo, sin ocuparte a vos.</li>
                    <li><strong>Preguntas frecuentes:</strong> formas de pago, envíos, garantías, requisitos.</li>
                    <li><strong>Derivación inteligente:</strong> ventas a una persona, soporte a otra.</li>
                </ul>

                <h2>Menú o inteligencia artificial</h2>
                <p>Un <strong>bot por menú</strong> ofrece opciones numeradas. Es predecible, barato y no se equivoca nunca. Funciona muy bien cuando tus consultas entran en cinco o seis categorías claras.</p>
                <p>Un <strong>bot con IA</strong> entiende lenguaje natural: el cliente escribe "hola, tenés turno el jueves a la tarde para color?" y lo resuelve sin obligarlo a navegar un menú. Responde solo con la información real de tu negocio que le cargamos, así que no inventa. Conviene cuando el volumen es alto y las preguntas son variadas.</p>
                <p>No siempre la IA es la respuesta correcta. Te vamos a recomendar la opción más simple que resuelva tu caso, porque un bot más complejo de lo necesario es más caro de mantener y falla más.</p>

                <table>
                    <thead>
                        <tr><th></th><th>Bot por menú</th><th>Bot con IA</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Cómo interactúa</strong></td><td>Opciones numeradas</td><td>El cliente escribe como quiere</td></tr>
                        <tr><td><strong>Costo</strong></td><td>Más bajo</td><td>Más alto</td></tr>
                        <tr><td><strong>Margen de error</strong></td><td>Ninguno</td><td>Bajo: responde solo con lo que le cargamos</td></tr>
                        <tr><td><strong>Implementación</strong></td><td>1 a 2 semanas</td><td>Algo más: hay que ordenar la información</td></tr>
                        <tr><td><strong>Conviene cuando</strong></td><td>Tus consultas entran en 5 o 6 categorías</td><td>Alto volumen y preguntas impredecibles</td></tr>
                    </tbody>
                </table>

                <h2>Automatizar no es solo responder</h2>
                <p>La parte que más plata deja no es la respuesta automática: es <strong>el seguimiento</strong>. La mayoría de los negocios pierden ventas no porque no contestan, sino porque nadie vuelve a escribirle al que preguntó el precio y no respondió más.</p>
                <p>Podemos automatizar recordatorios de turno (que bajan muchísimo el ausentismo), seguimiento a las 48 horas de una consulta sin cerrar, avisos de carrito abandonado y pedidos de reseña después de una compra. Todo eso se conecta naturalmente con un <a href="/crm-para-pymes">CRM</a> para que quede registrado quién es quién y en qué estado está cada conversación.</p>

                <div class="callout">
                    <p><strong>Probalo antes de contratarlo:</strong> escribinos y te armamos un bot de demostración con las preguntas reales de tu negocio, para que veas cómo respondería.</p>
                </div>'''

    cards = [
        ("bot", "Respuesta 24/7", "Precios, horarios, ubicación y preguntas frecuentes resueltas al instante.", "Sin esperas"),
        ("sparkles", "Chatbot con IA", "Entiende preguntas escritas libremente y responde con datos reales de tu negocio.", "Lenguaje natural"),
        ("calendar", "Turnos y reservas", "Muestra disponibilidad, agenda y manda recordatorios automáticos.", "Menos ausentismo"),
        ("users", "Derivación a humano", "Cuando la consulta lo amerita, pasa a una persona con todo el historial.", "Sin perder el hilo"),
        ("refresh", "Seguimiento automático", "Recontacta al que preguntó y no volvió. Ahí está la venta que se pierde.", "Recupera ventas"),
        ("shield", "API oficial de Meta", "Trabajamos sobre WhatsApp Business API. Sin riesgo de bloqueo de número.", "Vía habilitada"),
    ]

    return _page(
        path="/automatizacion-whatsapp",
        tldr=[
            "El 80% de los mensajes que respondés son <strong>las mismas cinco preguntas</strong>: precio, horario, ubicación, turno y forma de pago.",
            "El costo real no es tu tiempo: es <strong>la consulta que llega a la medianoche</strong> y contestás a la mañana siguiente.",
            "Empezá por un <strong>bot de menú</strong>: es más barato, no se equivoca y te muestra con datos qué preguntas se repiten.",
            "Lo que más plata deja no es responder, es el <strong>seguimiento automático</strong> al que preguntó y no volvió.",
        ],
        cta_top=("<strong>Probalo antes de contratarlo:</strong> te armamos un bot de demostración con las preguntas reales de tu negocio.",
                 "Quiero probarlo", "Quiero%20automatizar%20mi%20WhatsApp"),
        title="Chatbots de WhatsApp con IA | Tu Negocio En Las Redes",
        description="Automatización de WhatsApp para empresas: chatbots con IA que responden 24/7, agendan turnos y hacen seguimiento. Sobre API oficial de Meta.",
        og_title="Automatización de WhatsApp y Chatbots con IA",
        tag="Automatización de WhatsApp",
        h1='<span class="gradient-text">Chatbots</span> que atienden<br>tu WhatsApp 24/7.',
        lead="Automatizamos las consultas repetidas de tu negocio para que nadie espere una respuesta hasta mañana. Precios, turnos, catálogo y seguimiento, resueltos solos. Sobre la API oficial de WhatsApp Business.",
        bread_mid=(("IA & Automatización", "/ia"), ("Automatización de WhatsApp",)),
        prose=prose,
        cards=cards,
        cards_head=("Qué incluye", 'Lo que tu WhatsApp<br><span class="gradient-text">puede resolver solo.</span>',
                    "Se configura según tu rubro. Estas son las funciones que más usan nuestros clientes."),
        faq_items=faq_items,
        related_title='Con qué se<br><span class="gradient-text">combina mejor.</span>',
        related=[
            ("/crm-para-pymes", "CRM para PyMEs", "Para que cada conversación quede registrada y con un estado claro."),
            ("/ia", "IA & Automatización", "El panorama completo de lo que la inteligencia artificial puede hacer en tu negocio."),
            ("/publicidad-digital", "Publicidad digital", "Si vas a generar más consultas, primero asegurate de poder responderlas."),
            ("/blog/chatbot-whatsapp-para-negocios", "Guía: chatbot de WhatsApp", "Qué automatizar primero y qué conviene dejar en manos de una persona."),
        ],
        cta=('¿Cuántas ventas perdiste<br>por <span class="gradient-text">responder tarde?</span>',
             "Te armamos un bot de demostración con las preguntas reales de tu negocio,<br>para que veas cómo respondería. Sin costo.",
             "Quiero automatizar mi WhatsApp →", "Quiero%20automatizar%20mi%20WhatsApp"),
        service_kw={
            "name": "Automatización de WhatsApp y Chatbots",
            "type": "Automatización",
            "desc": "Desarrollo e implementación de chatbots de WhatsApp con inteligencia artificial sobre la API oficial de Meta: respuesta automática, agenda de turnos, catálogo y seguimiento de leads.",
            "offers": ["Chatbot de WhatsApp por menú", "Chatbot de WhatsApp con IA",
                       "Agenda de turnos automatizada", "Seguimiento automático de leads",
                       "Integración con CRM"],
        },
    )


# ----------------------------------------------------------------- CRM PARA PYMES
def crm_para_pymes():
    faq_items = [
        ("¿Qué es un CRM y para qué sirve?",
         "Es el sistema donde queda registrado <strong>quién es cada cliente y en qué estado está</strong>: quién consultó, quién ya recibió presupuesto, quién compró y a quién hay que volver a escribirle. Sin eso, esa información vive en la cabeza de una persona y en conversaciones de WhatsApp que nadie más puede ver."),
        ("¿No me alcanza con un Excel?",
         "Al principio sí, y está perfecto empezar así. El Excel deja de alcanzar cuando lo tienen que usar dos o tres personas a la vez, cuando necesitás que algo te avise que hay un seguimiento vencido, o cuando querés saber de dónde vinieron tus clientes del último trimestre sin pasar una hora armando la tabla."),
        ("¿Por qué un CRM a medida y no uno de los que ya existen?",
         "Los CRM comerciales son excelentes, pero están pensados para procesos de venta genéricos y se pagan por usuario todos los meses en dólares. Para muchas PyMEs eso significa pagar por decenas de funciones que no usan y pelearse con las tres que sí necesitan. Un <strong>sistema a medida</strong> hace exactamente lo que tu negocio hace, sin cuota por usuario. Dicho esto: si tu caso encaja en una herramienta que ya existe, te lo vamos a decir en vez de venderte un desarrollo."),
        ("¿Se conecta con WhatsApp?",
         "Sí, y es la integración que más se nota. Cada consulta que entra por <a href=\"/automatizacion-whatsapp\">WhatsApp</a> puede crear automáticamente el contacto en el CRM con su origen y su estado, para que ninguna consulta quede sin seguimiento."),
        ("¿Puedo entrar desde el celular?",
         "Sí. Los sistemas que desarrollamos funcionan en el navegador y se adaptan al celular, así que se usan desde cualquier dispositivo sin instalar nada."),
        ("¿Y si mañana necesito una función nueva?",
         "Se agrega. Esa es la ventaja de un sistema propio: crece con el negocio en lugar de obligarte a adaptar el negocio al software."),
        ("¿Cuánto tarda un desarrollo así?",
         "Una primera versión funcional con lo esencial suele estar en <strong>tres a seis semanas</strong>. Preferimos entregar algo que ya te sirve y crecer desde ahí, en vez de desaparecer seis meses y volver con un sistema enorme que no se parece a lo que necesitabas."),
    ]

    prose = '''                <h2>El problema no es conseguir clientes. Es no perderlos.</h2>
                <p>Cuando un negocio empieza a andar bien, aparece un cuello de botella que sorprende a casi todos: entran más consultas de las que se pueden seguir. El presupuesto que quedó en visto, el cliente que dijo "la semana que viene te confirmo" hace un mes, el que compró una vez y nunca volvió porque nadie le escribió.</p>
                <p>Nada de eso se pierde por falta de esfuerzo. Se pierde porque <strong>la información está desparramada</strong>: un poco en WhatsApp, un poco en un cuaderno, un poco en la memoria del que atendió. Un CRM junta todo eso en un solo lugar donde se puede ver el estado real del negocio.</p>

                <h2>Qué resuelve un CRM en una PyME</h2>
                <h3>Ver el embudo completo</h3>
                <p>Cuántas consultas entraron este mes, cuántas se convirtieron en presupuesto y cuántas terminaron en venta. Con eso sabés dónde se te caen los clientes: si entran pocas consultas tenés un problema de marketing; si entran muchas y no cierran, tenés un problema de proceso de venta. Son soluciones opuestas y sin datos es imposible saber cuál te toca.</p>
                <h3>Que nadie quede sin seguimiento</h3>
                <p>Cada contacto tiene un estado y una próxima acción con fecha. El sistema avisa cuando algo está vencido. Esto solo, en la mayoría de los negocios, recupera más ventas de las que cuesta el desarrollo.</p>
                <h3>Saber de dónde viene cada cliente</h3>
                <p>Si registrás el origen de cada consulta (Instagram, Google, recomendación, <a href="/publicidad-digital">publicidad</a>), a los tres meses sabés exactamente en qué canal conviene invertir y cuál estás sosteniendo por costumbre.</p>
                <table>
                    <thead>
                        <tr><th></th><th>Excel</th><th>CRM comercial</th><th>CRM a medida</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Costo inicial</strong></td><td>Cero</td><td>Bajo</td><td>Más alto</td></tr>
                        <tr><td><strong>Costo mensual</strong></td><td>Cero</td><td>Por usuario, en dólares</td><td>Ninguno</td></tr>
                        <tr><td><strong>Se adapta a tu proceso</strong></td><td>A mano y con esfuerzo</td><td>Parcialmente</td><td>Totalmente</td></tr>
                        <tr><td><strong>Varias personas a la vez</strong></td><td>Se complica</td><td>Sí</td><td>Sí</td></tr>
                        <tr><td><strong>Alertas automáticas</strong></td><td>No</td><td>Sí</td><td>Sí</td></tr>
                    </tbody>
                </table>

                <h3>Dejar de depender de una persona</h3>
                <p>Si el que atiende se enferma o se va, el historial de cada cliente sigue estando. Esto es especialmente crítico en negocios familiares, donde toda la información suele vivir en la cabeza del dueño.</p>

                <h2>Más allá del CRM: software para tu negocio</h2>
                <p>Muchos de nuestros clientes arrancan pidiendo un CRM y terminan con un sistema que cubre más cosas, porque el problema real era otro. Desarrollamos también:</p>
                <ul>
                    <li><strong>Gestión de turnos y reservas</strong> con recordatorios automáticos.</li>
                    <li><strong>Control de stock</strong> con alertas de mínimos y movimientos.</li>
                    <li><strong>Paneles de métricas</strong> para ver el estado del negocio de un vistazo.</li>
                    <li><strong>Presupuestos y remitos</strong> generados desde el sistema.</li>
                    <li><strong>Herramientas internas</strong> para procesos propios que hoy resolvés a mano.</li>
                </ul>
                <p>Podés ver algunos de estos sistemas funcionando en la sección de <a href="/trabajos">trabajos</a>.</p>

                <h2>Cómo lo desarrollamos</h2>
                <p>Empezamos entendiendo tu proceso real, no el que debería ser. Después definimos la <strong>primera versión útil</strong>: lo mínimo que ya te ahorra tiempo. La entregamos, la usás algunas semanas y sobre ese uso real definimos qué sigue. Es mucho más efectivo que intentar especificar todo el sistema por adelantado, porque hasta que no lo usás no sabés qué necesitás de verdad.</p>

                <div class="callout">
                    <p><strong>Primera charla sin costo:</strong> nos contás cómo manejás hoy tus clientes y te decimos con franqueza si necesitás un desarrollo a medida, una herramienta que ya existe, o simplemente ordenar el Excel que ya tenés.</p>
                </div>'''

    cards = [
        ("users", "Ficha de cliente", "Historial completo: qué consultó, qué se le ofreció y en qué quedó.", "Todo en un lugar"),
        ("layers", "Embudo de ventas", "Estados claros, de la consulta al cierre. Sabés dónde se traba cada venta.", "Proceso visible"),
        ("clock", "Alertas de seguimiento", "El sistema te avisa a quién hay que volver a escribirle y cuándo.", "Nada se pierde"),
        ("message", "Integración con WhatsApp", "Las consultas entran solas al sistema con su origen y su estado.", "Sin carga manual"),
        ("chart", "Panel de métricas", "Consultas, conversión y origen de tus clientes, en tiempo real.", "Decisiones con datos"),
        ("code", "A medida y sin cuota por usuario", "Hace lo que tu negocio hace. Y crece cuando el negocio crece.", "Software propio"),
    ]

    return _page(
        path="/crm-para-pymes",
        tldr=[
            "El problema no es conseguir clientes: es <strong>no perderlos</strong> en presupuestos que quedaron en visto.",
            "Un CRM te muestra <strong>dónde se cae la venta</strong>: si entran pocas consultas es marketing, si entran muchas y no cierran es proceso.",
            "Las <strong>alertas de seguimiento</strong> suelen recuperar más ventas de lo que cuesta el desarrollo.",
            "Si tu caso entra en una herramienta que ya existe, te lo decimos en vez de venderte un desarrollo.",
        ],
        cta_top=("<strong>Primera charla sin costo:</strong> contanos cómo manejás hoy tus clientes y te decimos con franqueza qué necesitás.",
                 "Quiero ordenar mis clientes", "Quiero%20un%20CRM%20para%20mi%20negocio"),
        title="CRM para PyMEs y Software a Medida | Tu Negocio En Las Redes",
        description="CRM para PyMEs y software a medida: seguimiento de clientes, embudo de ventas, alertas e integración con WhatsApp. Sin cuota por usuario.",
        og_title="CRM para PyMEs y Software a Medida",
        tag="CRM y Software",
        h1='<span class="gradient-text">CRM</span> y software<br>hecho para tu negocio.',
        lead="Sistemas de gestión a medida para que dejes de perder clientes en el camino: seguimiento, embudo de ventas, alertas, turnos, stock y métricas reales. Sin cuotas mensuales por usuario.",
        bread_mid=(("IA & Automatización", "/ia"), ("CRM para PyMEs",)),
        prose=prose,
        cards=cards,
        cards_head=("Qué incluye", 'Lo que hace<br><span class="gradient-text">tu sistema.</span>',
                    "Cada desarrollo se arma sobre tu proceso real. Estos son los módulos que más pedidos tienen."),
        faq_items=faq_items,
        related_title='Lo que suele<br><span class="gradient-text">ir junto.</span>',
        related=[
            ("/automatizacion-whatsapp", "Automatización de WhatsApp", "Que las consultas entren solas al CRM, con su origen y su estado."),
            ("/ia", "IA & Automatización", "Todo lo que la inteligencia artificial puede automatizar en tu negocio."),
            ("/trabajos", "Sistemas que desarrollamos", "CRM y apps de gestión funcionando hoy en negocios reales."),
            ("/publicidad-digital", "Publicidad digital", "Para medir de punta a punta qué campaña generó qué venta."),
        ],
        cta=('¿Sabés cuántas ventas<br><span class="gradient-text">se te escaparon este mes?</span>',
             "Contanos cómo manejás hoy a tus clientes y te decimos con franqueza qué necesitás.<br>Aunque la respuesta sea que no necesitás contratarnos.",
             "Quiero ordenar mis clientes →", "Quiero%20un%20CRM%20para%20mi%20negocio"),
        service_kw={
            "name": "CRM y Software a Medida para PyMEs",
            "type": "Desarrollo de Software",
            "desc": "Desarrollo de CRM y software de gestión a medida para PyMEs: seguimiento de clientes, embudo de ventas, turnos, control de stock, paneles de métricas e integración con WhatsApp.",
            "offers": ["CRM a medida", "Gestión de turnos y reservas", "Control de stock",
                       "Paneles de métricas", "Herramientas internas a medida"],
        },
    )


ALL = [paginas_web, tiendas_online, gestion_de_redes,
       publicidad_digital, automatizacion_whatsapp, crm_para_pymes]
