# -*- coding: utf-8 -*-
"""Blog: índice + artículos."""

import chrome as C
import schemas as S
import components as CO

PUB = "2026-07-28"


def _post(*, slug, title, description, h1, lead, read, prose, faq_items=None,
          keywords=None, related=None, tldr=None, cta_top=None):
    path = f"/blog/{slug}"
    prose = CO.lead_block(prose, tldr, cta_top)
    graph = [
        S.breadcrumb([("Inicio", "/"), ("Blog", "/blog"), (h1, path)]),
        S.article(path, h1, description, PUB, keywords=keywords),
    ]
    if faq_items:
        graph.append(S.faq(faq_items))

    body = f'''
    <header class="page-hero">
        <div class="hero-bg">
            <div class="hero-orb hero-orb-1"></div>
            <div class="hero-orb hero-orb-2"></div>
            <div class="hero-grid"></div>
        </div>
        <div class="container">
            <div class="post-header">
                <div class="post-meta">
                    <span>Blog</span><span>·</span>
                    <time datetime="{PUB}">28 de julio de 2026</time><span>·</span>
                    <span>{read} min de lectura</span>
                </div>
                <h1>{h1}</h1>
                <p>{lead}</p>
            </div>
        </div>
    </header>

    <article class="section-dark">
        <div class="container">
            <div class="prose reveal">
{prose}
            </div>
        </div>
    </article>
'''

    out = (
        C.head(title=title, description=description, path=path, schema=S.dump(graph),
               og_title=h1, page_type="article")
        + C.nav()
        + C.breadcrumb([("Inicio", "/"), ("Blog", "/blog"), (h1, None)])
        + body
    )
    out += CO.share_bar(path, h1)
    if faq_items:
        out += C.faq_section(faq_items, heading='Preguntas<br><span class="gradient-text">frecuentes.</span>')
    if related:
        out += C.related_section('Seguí leyendo<br><span class="gradient-text">o pasá a la acción.</span>', related)
    out += C.cta_section(
        '¿Querés que lo hagamos<br><span class="gradient-text">nosotros por vos?</span>',
        "Te armamos una demo real de tu página web, con tu logo y tus colores,<br>sin costo y sin compromiso.",
        "Quiero mi demo gratis →", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web")
    out += C.FOOTER
    return path, out


# ------------------------------------------------------------------ ARTÍCULO 1
def precio_pagina_web():
    faq_items = [
        ("¿Cuánto cuesta una página web en Argentina en 2026?",
         "El rango es enorme porque \"página web\" abarca cosas muy distintas: una landing page de una sección, una web institucional de cinco páginas y una tienda online con carrito y pagos son tres productos diferentes con costos diferentes. Lo que sí es constante es la estructura: diseño, desarrollo, contenido, dominio y hosting. Pedí siempre el presupuesto desglosado en esas partes."),
        ("¿Por qué hay presupuestos tan distintos para lo mismo?",
         "Porque casi nunca es lo mismo. Un sitio armado con una plantilla comprada y contenido genérico se hace en horas. Uno diseñado a medida, con textos escritos para tu negocio y SEO técnico configurado, lleva días de trabajo. Ambos son \"una página web\" y ambos precios pueden ser honestos: lo que cambia es qué recibís."),
        ("¿Conviene una web barata para empezar?",
         "Conviene una web <strong>simple</strong>, que no es lo mismo que barata. Una landing page bien hecha es una excelente forma de empezar. Lo que no conviene es una web mal hecha, porque después rehacerla cuesta más que haberla hecho bien de entrada, y mientras tanto estuvo dándole a Google señales que te perjudican."),
        ("¿Qué costos mensuales tiene una página web?",
         "Dos fijos y chicos: la <strong>renovación anual del dominio</strong> y el <strong>hosting</strong>. Un sitio estático y liviano se hospeda por muy poco o incluso sin costo en plataformas modernas. Después, opcionales: mantenimiento, cambios de contenido y campañas. Desconfiá de cuotas mensuales altas y obligatorias solo por \"tener\" el sitio online."),
    ]

    prose = '''                <p>Es la primera pregunta que nos hacen y la más difícil de responder de una, porque "página web" nombra cosas que no se parecen entre sí. Es como preguntar cuánto sale un vehículo: depende de si hablamos de una bicicleta o de una camioneta.</p>
                <p>Lo que sí se puede hacer —y es lo que vamos a hacer acá— es explicarte <strong>de qué depende el precio</strong>, para que cuando pidas presupuestos sepas qué estás comparando y por qué dos números tan distintos pueden ser los dos honestos.</p>

                <h2>De qué depende realmente el precio</h2>
                <h3>1. La cantidad de páginas y funciones</h3>
                <p>Una landing page es una sola página con un objetivo. Una web institucional tiene cinco o seis secciones. Una tienda online suma catálogo, carrito, pagos y envíos. Cada escalón agrega trabajo de diseño, desarrollo y prueba. La tienda online es la que más se dispara, porque hay que integrar sistemas de terceros y contemplar todos los casos en los que una compra puede fallar.</p>

                <h3>2. Plantilla o diseño a medida</h3>
                <p>Este es el factor que más explica las diferencias. Comprar una plantilla y cambiarle los textos y el logo lleva pocas horas. Diseñar desde cero lleva días. El resultado también es distinto: la plantilla la están usando otros miles de negocios y te obliga a adaptar tu contenido a su estructura, en vez de que la estructura sirva a lo que vos querés comunicar.</p>

                <h3>3. Quién escribe el contenido</h3>
                <p>Un costo que casi nunca está en el presupuesto y siempre aparece en el camino. Si los textos los ponés vos, el proyecto sale más barato y se demora lo que tardes en escribirlos —que en la práctica suele ser la razón número uno por la que una web queda meses sin publicarse—. Si los escribe la agencia, sale más y avanza solo.</p>

                <h3>4. Si incluye SEO técnico</h3>
                <p>Una web puede estar hermosa y ser invisible para Google. Que sea indexable requiere trabajo concreto: títulos y descripciones únicos, estructura de encabezados correcta, datos estructurados, sitemap, robots.txt, URLs limpias, imágenes optimizadas y velocidad de carga. <strong>Preguntá explícitamente si está incluido</strong>, porque muchas veces no lo está y es lo que después define si la web te sirve o no.</p>

                <h3>5. La tecnología</h3>
                <p>Un sitio hecho con código propio es más liviano y rápido que uno armado con constructores visuales, que arrastran código que tu negocio no usa. La velocidad no es capricho: Google la mide directamente como factor de posicionamiento a través de las Core Web Vitals, y es la principal razón por la que la gente abandona un sitio antes de que abra.</p>

                <h2>Las cinco preguntas que tenés que hacer antes de contratar</h2>
                <ol>
                    <li><strong>¿La web va a ser mía?</strong> Tiene que quedar a tu nombre el dominio y tenés que poder llevarte el sitio. Que no te lo secuestren si te vas.</li>
                    <li><strong>¿Incluye SEO técnico?</strong> Que te digan específicamente qué. "Sí, está optimizada" no es una respuesta.</li>
                    <li><strong>¿Puedo modificar el contenido?</strong> O dependés de ellos —y de que te cobren— cada vez que cambia un precio.</li>
                    <li><strong>¿Qué costos mensuales tiene?</strong> Dominio y hosting sí. Cuotas altas y obligatorias solo por estar online, no.</li>
                    <li><strong>¿Puedo verla antes de pagar?</strong> Esta es la más importante.</li>
                </ol>

                <div class="callout">
                    <p><strong>Nuestra postura sobre el último punto:</strong> te hacemos la <a href="/paginas-web">demo de tu página web gratis</a>, con tu logo y tus colores, antes de que pongas un peso. La ves funcionando en tu celular y recién ahí hablamos de precio. Nos parece la única forma justa de vender esto.</p>
                </div>

                <h2>El error más caro: mirar solo el precio</h2>
                <p>Una web de bajo costo que no aparece en Google, tarda cinco segundos en cargar y no tiene un lugar claro para escribirte no es barata: es cara, porque no genera nada. El costo real de una web no es lo que pagaste, es <strong>lo que te devuelve por mes</strong>.</p>
                <p>Si tu sitio te trae dos consultas por mes que se convierten en clientes, ya se pagó. Si no te trae ninguna, cualquier precio fue caro.</p>

                <h2>Entonces, ¿cuánto deberías gastar?</h2>
                <p>La forma sana de pensarlo es al revés de como se piensa habitualmente. No arranques por "cuánto quiero gastar", arrancá por <strong>cuánto vale un cliente para tu negocio</strong>. Si tu ticket promedio es alto y un cliente te deja un margen importante, una web que te traiga tres clientes al año ya justificó la inversión con muchísimo margen. Si vendés productos de ticket bajo, necesitás volumen y probablemente te convenga empezar simple e ir escalando.</p>
                <p>Esa cuenta la podés hacer vos en cinco minutos y vale más que cualquier lista de precios.</p>'''

    return _post(
        slug="cuanto-cuesta-una-pagina-web-argentina",
        tldr=[
            "No hay un precio único: <strong>landing, institucional y tienda online</strong> son tres productos distintos.",
            "Lo que más explica las diferencias de presupuesto es <strong>plantilla contra diseño a medida</strong>.",
            "Preguntá siempre si <strong>incluye SEO técnico</strong>: sin eso la web puede quedar invisible para Google.",
            "Costos mensuales reales: solo <strong>dominio y hosting</strong>. Desconfiá de cuotas altas obligatorias.",
            "La cuenta que importa no es cuánto sale, es <strong>cuánto te devuelve por mes</strong>.",
        ],
        cta_top=("<strong>Nuestra postura:</strong> te hacemos la demo de tu web antes de que pongas un peso. Recién ahí hablamos de precio.",
                 "Quiero mi demo gratis", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"),
        title="¿Cuánto cuesta una página web en Argentina? Guía 2026",
        description="De qué depende el precio de una página web en Argentina: plantilla vs diseño a medida, SEO técnico y costos. Qué preguntar antes de contratar.",
        h1="¿Cuánto cuesta una página web en Argentina?",
        lead="La pregunta que todos hacen primero. Te explicamos de qué depende el precio, por qué dos presupuestos por “lo mismo” pueden ser los dos honestos, y qué preguntar antes de contratar.",
        read=8,
        prose=prose,
        faq_items=faq_items,
        keywords=["cuánto cuesta una página web", "precio página web argentina",
                  "cuánto sale una web", "diseño web precio", "desarrollo web argentina"],
        related=[
            ("/paginas-web", "Páginas web", "Cómo trabajamos y qué incluye cada sitio que entregamos."),
            ("/tiendas-online", "Tiendas online", "Si además de mostrar necesitás cobrar online."),
            ("/blog/aparecer-en-google-maps", "Aparecer en Google Maps", "La acción gratuita con mejor retorno para un negocio local."),
            ("/trabajos", "Ver trabajos", "Doce sitios que desarrollamos, online funcionando hoy."),
        ],
    )


# ------------------------------------------------------------------ ARTÍCULO 2
def clientes_instagram():
    faq_items = [
        ("¿Cuántos seguidores necesito para vender por Instagram?",
         "Muchos menos de los que pensás. Una cuenta de 800 seguidores del barrio, que realmente pueden comprarte, vende más que una de 15.000 conseguidos con sorteos y gente de otro país. Lo que importa no es el número, es <strong>qué porcentaje de tus seguidores puede efectivamente ser tu cliente</strong>."),
        ("¿Cuántas veces por semana hay que publicar?",
         "Es mejor tres veces por semana sostenidas durante seis meses que todos los días durante tres semanas y después nada. La constancia le importa al algoritmo, pero sobre todo le importa a la gente: te empieza a reconocer recién después de verte varias veces."),
        ("¿Los sorteos sirven?",
         "Para conseguir seguidores sí, para conseguir clientes casi nunca. Un sorteo mal planteado te trae cazadores de premios que después no interactúan, y eso <strong>baja tu alcance promedio</strong> y te perjudica. Si hacés uno, que el premio sea tu propio producto y que participar exija algo que solo haría alguien realmente interesado."),
        ("¿Conviene pagar publicidad en Instagram?",
         "Sí, pero después de tener contenido que ya funcione orgánicamente. Poner plata detrás de una pieza que ya demostró que la gente guarda y comparte multiplica algo que anda; ponerla detrás de contenido que a nadie le interesó solo hace que más gente lo ignore, y más caro."),
    ]

    prose = '''                <p>La mayoría de los negocios que nos escriben tienen el mismo diagnóstico: publican seguido, tienen un feed prolijo, y no les entra una sola consulta. Instagram les consume tiempo todas las semanas y no les devuelve clientes.</p>
                <p>Casi siempre el problema no es la frecuencia ni el diseño. Es que <strong>el contenido no está construido para generar una acción</strong>. Acá va lo que aplicamos en las cuentas que gestionamos.</p>

                <h2>1. Tu perfil es una landing page, no una presentación</h2>
                <p>Alguien ve un reel tuyo, le interesa y entra a tu perfil. Tenés unos pocos segundos para que entienda tres cosas: <strong>qué vendés, a quién y cómo te compra</strong>. Si tu biografía dice "✨ Emprendedora ✨ Amante del café ✨ Mamá de dos", no dice ninguna de las tres.</p>
                <p>Lo que sí funciona:</p>
                <ul>
                    <li><strong>Nombre con palabra clave.</strong> El campo "nombre" (no el @usuario) es buscable dentro de Instagram. "Tortas Ana" no aparece cuando alguien busca tortas; "Ana | Tortas personalizadas Castelar" sí.</li>
                    <li><strong>Una línea que diga qué resolvés</strong>, en criollo.</li>
                    <li><strong>Zona explícita</strong> si sos un negocio local. Mucha gente descarta perfiles solo porque no sabe si les queda cerca.</li>
                    <li><strong>Un solo link</strong>, al lugar donde querés que vaya. Si tenés <a href="/paginas-web">web propia</a>, ahí; si no, a WhatsApp con mensaje prearmado.</li>
                    <li><strong>Historias destacadas</strong> ordenadas como un menú: precios, cómo comprar, envíos, opiniones de clientes.</li>
                </ul>

                <h2>2. Guardados y compartidos valen más que los likes</h2>
                <p>El like es la interacción más barata que existe: se da sin pensar, mientras se scrollea. El <strong>guardado</strong> significa "esto me sirve, lo quiero para después". El <strong>compartido</strong> significa "esto es tan útil que se lo mando a alguien". Son las señales que mejor predicen que un contenido va a seguir mostrándose a gente nueva.</p>
                <p>Entonces la pregunta al planificar deja de ser "¿esto va a gustar?" y pasa a ser <strong>"¿alguien guardaría esto?"</strong>. Los formatos que se guardan son concretos: listas de precios, guías de talles, pasos, comparativas, checklists, respuestas a preguntas frecuentes.</p>

                <h2>3. Los primeros dos segundos deciden todo</h2>
                <p>En un reel, la gente decide si sigue mirando antes de que termines de saludar. Por eso los reels que arrancan con "Hola, ¿cómo están? Hoy les quiero contar..." pierden a la mayoría de la audiencia antes del segundo tres.</p>
                <p>Arrancá por el conflicto o el resultado:</p>
                <ul>
                    <li>"Este error te está costando clientes todos los días."</li>
                    <li>"Así quedó una cocina que estaba para tirar."</li>
                    <li>"Tres cosas que nadie te dice antes de comprar una bici usada."</li>
                </ul>
                <p>Y sumá texto en pantalla desde el primer frame: gran parte de la gente mira sin sonido.</p>

                <h2>4. Contenido local: tu mayor ventaja</h2>
                <p>Si sos un negocio de barrio, no compitas por temas generales contra cuentas nacionales con equipos de producción. Competí por lo que ellos no pueden: <strong>tu zona</strong>. Mostrá el local, la calle, los clientes reales, el barrio. Usá la ubicación en cada publicación e historia. Ese contenido tiene menos alcance total pero muchísima más conversión, porque le llega a gente que efectivamente puede ir a comprarte.</p>

                <h2>5. Prueba social: lo que más vende y menos se publica</h2>
                <p>Los testimonios, las capturas de mensajes de clientes contentos (con permiso), los antes y después y los productos en manos de gente real convierten más que cualquier pieza de diseño. Y son gratis: los estás recibiendo por privado todo el tiempo. Lo único que hay que hacer es pedirlos sistemáticamente y publicarlos.</p>

                <h2>6. Pedí la acción. Siempre.</h2>
                <p>Suena obvio y es lo que más falta. Un porcentaje enorme de las publicaciones de negocios no dice qué hacer. Cerrá siempre con una instrucción concreta y única: "Escribinos por WhatsApp y te pasamos disponibilidad", "Comentá QUIERO y te mando el precio", "Guardalo para cuando lo necesites". Una sola, no tres.</p>

                <h2>7. El límite de Instagram (y qué hacer con eso)</h2>
                <p>Instagram es terreno alquilado. No controlás el algoritmo, no te llevás a tus seguidores si mañana perdés la cuenta, y —esto es lo más ignorado— <strong>no aparecés en Google</strong>. Quien busca "tortas personalizadas Castelar" en el buscador no te encuentra nunca.</p>
                <p>Por eso la combinación que funciona no es Instagram <em>o</em> web: es Instagram para que te descubran y <a href="/paginas-web">web propia</a> para que te encuentren y convertir. Y cuando el volumen de mensajes crece, <a href="/automatizacion-whatsapp">automatizar las respuestas repetidas</a> para no perder las consultas que llegan a la madrugada.</p>

                <div class="callout">
                    <p><strong>Si querés una mano:</strong> escribinos y te hacemos un <a href="/gestion-de-redes">diagnóstico gratis de tu cuenta</a>, con tres cambios concretos que podés aplicar esta semana aunque no trabajes con nosotros.</p>
                </div>'''

    return _post(
        slug="como-conseguir-clientes-por-instagram",
        tldr=[
            "Tu perfil es una landing page: en segundos tiene que decir <strong>qué vendés, a quién y cómo te compran</strong>.",
            "Los <strong>guardados y compartidos</strong> predicen el alcance mucho mejor que los likes.",
            "En reels, los <strong>primeros dos segundos</strong> deciden todo. Arrancá por el conflicto o el resultado.",
            "Tu mayor ventaja como negocio local es el <strong>contenido de tu zona</strong>: menos alcance, mucha más conversión.",
            "Cerrá siempre con <strong>una sola</strong> instrucción concreta.",
        ],
        cta_top=("<strong>¿Querés una mano?</strong> Te hacemos un diagnóstico gratis de tu cuenta con tres cambios para esta semana.",
                 "Quiero mi diagnóstico", "Quiero%20un%20diagn%C3%B3stico%20de%20mis%20redes"),
        title="Cómo conseguir clientes por Instagram: guía práctica 2026",
        description="Cómo conseguir clientes reales por Instagram: optimizar el perfil, contenido que se guarda, ganchos en reels y prueba social. Guía práctica.",
        h1="Cómo conseguir clientes por Instagram",
        lead="Publicás seguido, el feed se ve bien y no entra ni una consulta. Casi siempre el problema no es la frecuencia: es que el contenido no está construido para generar una acción.",
        read=9,
        prose=prose,
        faq_items=faq_items,
        keywords=["como conseguir clientes por instagram", "vender por instagram",
                  "instagram para negocios", "community manager", "contenido para empresas"],
        related=[
            ("/gestion-de-redes", "Gestión de redes", "Lo hacemos nosotros: estrategia, diseño, reels y reportes."),
            ("/publicidad-digital", "Publicidad digital", "Cuándo conviene poner presupuesto detrás del contenido."),
            ("/blog/chatbot-whatsapp-para-negocios", "Chatbot de WhatsApp", "Para responder las consultas que generan tus redes."),
            ("/paginas-web", "Páginas web", "El terreno propio que Instagram no te puede dar."),
        ],
    )


# ------------------------------------------------------------------ ARTÍCULO 3
def chatbot_whatsapp():
    faq_items = [
        ("¿Un chatbot de WhatsApp sirve para un negocio chico?",
         "Sí, y a veces más que para uno grande, porque en un negocio chico el que contesta los mensajes suele ser el dueño. Automatizar las cinco preguntas repetidas le devuelve varias horas por semana a la persona que menos tiempo tiene."),
        ("¿Puedo perder clientes por usar un bot?",
         "Podés, si está mal implementado: un bot que no entiende, que no deja salir del menú o que oculta que es un bot genera más bronca que ausencia de respuesta. Bien implementado pasa lo contrario, porque el cliente obtiene la respuesta al instante en vez de esperar hasta mañana. La clave es <strong>siempre tener salida a un humano</strong>."),
        ("¿Necesito la API oficial de WhatsApp?",
         "Para hacerlo en serio, sí. La <strong>API oficial de WhatsApp Business</strong> es la vía habilitada por Meta y la que no te expone a que te bloqueen el número. Las herramientas no oficiales son más baratas y son exactamente por las que la gente pierde su número."),
        ("¿Cuánto tarda en estar funcionando?",
         "Un bot por menú suele estar activo en <strong>una a dos semanas</strong>. Uno con inteligencia artificial conectado a catálogo o agenda lleva un poco más, sobre todo porque hay que ordenar la información con la que va a responder, que casi nunca está escrita en ningún lado."),
    ]

    prose = '''                <p>Antes de decidir si necesitás un chatbot, hacé este ejercicio: abrí WhatsApp y mirá tus últimos veinte mensajes de clientes. Contá cuántos son alguna variante de estas cinco preguntas:</p>
                <ol>
                    <li>¿Cuánto sale?</li>
                    <li>¿A qué hora abren?</li>
                    <li>¿Dónde están / hacen envíos?</li>
                    <li>¿Tenés turno / stock?</li>
                    <li>¿Cómo puedo pagar?</li>
                </ol>
                <p>En la mayoría de los negocios locales, ese puñado explica la enorme mayoría de los mensajes. Ninguna requiere tu criterio. Todas requieren tu tiempo.</p>

                <h2>El costo real no es tu tiempo</h2>
                <p>Perder minutos contestando lo mismo es molesto, pero no es lo caro. Lo caro es <strong>el mensaje que llega a las 23:40 y contestás a las 9 de la mañana</strong>.</p>
                <p>En servicios locales —una cerrajería, una veterinaria, un service de aire acondicionado— la persona que consulta a esa hora tiene un problema ahora. Si no le contestás, le escribe al siguiente de la lista de Google. Esa venta no se perdió por precio ni por calidad: se perdió por horario.</p>

                <h2>Qué conviene automatizar y qué no</h2>
                <p>La regla es simple: <strong>automatizá lo predecible, dejá en manos de una persona lo que requiere criterio.</strong></p>
                <h3>Automatizá sin dudarlo</h3>
                <ul>
                    <li>Precios y planes.</li>
                    <li>Horarios, dirección y cómo llegar.</li>
                    <li>Formas de pago, envíos, garantías.</li>
                    <li>Disponibilidad de turnos y agendarlos.</li>
                    <li>Estado de un pedido.</li>
                    <li>Derivación al área correcta.</li>
                </ul>
                <h3>Dejá siempre en manos de una persona</h3>
                <ul>
                    <li>Reclamos y clientes enojados.</li>
                    <li>Presupuestos que requieren evaluar un caso.</li>
                    <li>Negociación de precio o condiciones.</li>
                    <li>Cualquier consulta donde el cliente pida hablar con alguien.</li>
                </ul>

                <h2>Menú o inteligencia artificial</h2>
                <p>Un <strong>bot por menú</strong> ofrece opciones numeradas. Es barato, predecible y no se equivoca nunca. Si tus consultas entran en cinco o seis categorías claras, te alcanza y es lo que deberías hacer.</p>
                <p>Un <strong>bot con IA</strong> entiende preguntas escritas libremente: alguien escribe "hola tenés turno el jueves a la tarde para color?" y lo resuelve sin obligarlo a navegar opciones. Responde únicamente con la información de tu negocio que le cargaste, así que no inventa. Conviene cuando el volumen es alto y las preguntas son impredecibles.</p>
                <p>Un consejo honesto: <strong>empezá por el menú</strong>. Es más barato, lo tenés andando en días y te muestra con datos reales qué preguntas se repiten. Con eso en la mano, la decisión de sumar IA se toma con información en vez de con entusiasmo.</p>

                <h2>Los cinco errores que arruinan un chatbot</h2>
                <ol>
                    <li><strong>No dejar salir.</strong> Todo menú necesita una opción visible de "hablar con una persona". Sin eso, el bot se convierte en una trampa.</li>
                    <li><strong>Fingir que es humano.</strong> La gente lo detecta y se siente engañada. Aclaralo desde el saludo.</li>
                    <li><strong>Menús eternos.</strong> Más de seis opciones no se leen. Si necesitás más, ordenalas en dos niveles.</li>
                    <li><strong>Dejarlo abandonado.</strong> Un bot que da precios de hace ocho meses es peor que no tener bot.</li>
                    <li><strong>Automatizar solo la primera respuesta.</strong> Acá está la plata: la mayoría de las ventas no se pierden en el primer mensaje, se pierden en el seguimiento que nadie hizo.</li>
                </ol>

                <h2>La parte que casi nadie implementa: el seguimiento</h2>
                <p>Pensá en cuánta gente te preguntó el precio en los últimos treinta días y nunca más respondió. ¿A cuántos les volviste a escribir? En la mayoría de los negocios la respuesta es a ninguno.</p>
                <p>Un mensaje automático a las 48 horas —"Hola, ¿pudiste verlo? Cualquier duda quedo a disposición"— recupera una porción de esas conversaciones. No es magia: es simplemente hacer lo que nadie hace porque no da el tiempo. Lo mismo con recordatorios de turno, que reducen muchísimo el ausentismo, y con el pedido de reseña después de una compra.</p>
                <p>Cuando esto se conecta a un <a href="/crm-para-pymes">CRM</a>, cada consulta queda registrada con su estado y su próxima acción, y dejás de depender de la memoria de quien atendió.</p>

                <div class="callout">
                    <p><strong>Probalo antes de contratarlo:</strong> escribinos y te armamos un <a href="/automatizacion-whatsapp">bot de demostración</a> con las preguntas reales de tu negocio, para que veas cómo respondería. Sin costo.</p>
                </div>'''

    return _post(
        slug="chatbot-whatsapp-para-negocios",
        tldr=[
            "Automatizá <strong>lo predecible</strong>; dejá en manos de una persona lo que requiere criterio.",
            "Nunca automatices reclamos, negociaciones ni presupuestos que exigen evaluar un caso.",
            "<strong>Empezá por un bot de menú.</strong> Es más barato, no falla y te muestra qué preguntas se repiten.",
            "Todo menú necesita una salida visible a un humano. Sin eso, el bot es una trampa.",
            "La parte que más vende es el <strong>seguimiento</strong>, y es la que casi nadie implementa.",
        ],
        cta_top=("<strong>Probalo primero:</strong> te armamos un bot de demostración con las preguntas reales de tu negocio.",
                 "Quiero probarlo", "Quiero%20automatizar%20mi%20WhatsApp"),
        title="Chatbot de WhatsApp para negocios: qué automatizar y qué no",
        description="Qué conviene automatizar en WhatsApp y qué no, cuándo usar IA o un menú simple, y los 5 errores que arruinan un chatbot de negocio.",
        h1="Chatbot de WhatsApp: qué automatizar y qué no",
        lead="El 80% de los mensajes que respondés son las mismas cinco preguntas. Pero el costo real no es tu tiempo: es la consulta que llega a la medianoche y contestás a la mañana siguiente.",
        read=8,
        prose=prose,
        faq_items=faq_items,
        keywords=["chatbot whatsapp", "automatización de whatsapp", "chatbot para empresas",
                  "bot de whatsapp", "inteligencia artificial para negocios"],
        related=[
            ("/automatizacion-whatsapp", "Automatización de WhatsApp", "Lo implementamos nosotros, sobre API oficial de Meta."),
            ("/crm-para-pymes", "CRM para PyMEs", "Para que ninguna consulta quede sin seguimiento."),
            ("/ia", "IA & Automatización", "Todo lo que la IA puede hacer en tu negocio."),
            ("/blog/como-conseguir-clientes-por-instagram", "Clientes por Instagram", "Cómo generar las consultas que después vas a automatizar."),
        ],
    )


# ------------------------------------------------------------------ ARTÍCULO 4
def google_maps():
    faq_items = [
        ("¿Cómo hago para que mi negocio aparezca en Google Maps?",
         "Creás o reclamás tu ficha en <strong>Google Business Profile</strong> (antes Google My Business), verificás que el negocio es tuyo —normalmente por video, postal o teléfono— y completás la ficha entera. Es gratis. Una vez verificada, tu negocio empieza a aparecer en Maps y en el bloque de resultados locales del buscador."),
        ("¿Puedo aparecer en Google Maps sin local a la calle?",
         "Sí. Si atendés a domicilio o trabajás desde casa, se configura como <strong>negocio de servicio a domicilio</strong>: ocultás la dirección exacta y declarás las zonas donde trabajás. Es lo que corresponde para oficios, servicios técnicos y profesionales que van al cliente."),
        ("¿Cuánto tarda en aparecer?",
         "La verificación suele tardar de unos días a un par de semanas según el método. Después de verificada, la ficha aparece bastante rápido, aunque el <strong>posicionamiento</strong> dentro del mapa (aparecer entre los tres primeros) lleva más y depende de reseñas, cercanía y qué tan completa está la ficha."),
        ("¿Sirve de algo si ya tengo Instagram?",
         "Son cosas distintas y no se reemplazan. Instagram capta a quien te descubre navegando; Google Maps capta a quien <strong>ya te está buscando y quiere resolver ahora</strong>. Esa segunda intención es la que más convierte, y es gratis."),
        ("¿Puedo eliminar una reseña negativa?",
         "Solo si viola las políticas de Google (spam, insulto, competencia desleal, contenido falso evidente) y podés reportarla. Una reseña negativa legítima no se borra. Lo que sí podés —y conviene— es <strong>responderla bien</strong>: una respuesta serena y resolutiva a una crítica genera más confianza en quien la lee que no tener ninguna crítica."),
    ]

    prose = '''                <p>Si tu negocio atiende gente de tu zona, esta es probablemente la acción con mejor retorno por hora invertida que existe. Es gratis, se hace en una tarde y la mayoría de tus competidores la tiene a medias o directamente no la tiene.</p>
                <p>Cuando alguien busca "veterinaria cerca", "cerrajería Morón" o "gimnasio abierto ahora", Google no muestra primero los sitios web: muestra un <strong>bloque de tres negocios con mapa</strong>. Estar ahí vale más que estar primero en los resultados normales.</p>

                <h2>Paso 1: creá o reclamá tu ficha</h2>
                <p>Entrá a Google Business Profile y buscá tu negocio. Pueden pasar dos cosas: que no exista y lo crees, o que ya exista —Google a veces las genera solo— y tengas que reclamarlo. Ojo con esto último: si tu negocio ya aparece con datos viejos o mal cargados y nadie lo reclamó, esa información errónea está circulando hoy.</p>

                <h2>Paso 2: verificá</h2>
                <p>Google necesita confirmar que el negocio es tuyo. Hoy el método más común es un <strong>video de verificación</strong>: te pide grabar el local, el cartel, la calle y algo que demuestre que operás ahí (equipamiento, mercadería, la llave abriendo la puerta). Grabalo con luz, sin cortes, mostrando el número de la puerta y el cartel legibles. La mayoría de los rechazos son por videos apurados donde no se lee la dirección.</p>

                <h2>Paso 3: completá la ficha entera</h2>
                <p>Acá es donde se define casi todo, y donde casi todos aflojan.</p>
                <ul>
                    <li><strong>Categoría principal.</strong> Es el campo más importante de toda la ficha. Elegí la que describe exactamente lo que hacés, no una general. "Peluquería canina" rinde muchísimo más que "Tienda de mascotas" si eso es lo que hacés.</li>
                    <li><strong>Categorías secundarias.</strong> Sumá las que apliquen de verdad. No las llenes con cualquier cosa: Google lo penaliza.</li>
                    <li><strong>Horarios reales</strong>, incluidos feriados. Aparecer como "abierto" cuando estás cerrado genera reseñas de una estrella.</li>
                    <li><strong>Teléfono y sitio web.</strong> Si tenés <a href="/paginas-web">web propia</a>, cargala: las fichas con sitio web posicionan mejor.</li>
                    <li><strong>Servicios y productos</strong> cargados uno por uno. Cada uno es una oportunidad más de coincidir con una búsqueda.</li>
                    <li><strong>Fotos propias.</strong> Del frente (para que te reconozcan al llegar), del interior, del equipo y de lo que vendés. Las fotos de banco se notan y no generan confianza. Subí fotos nuevas cada tanto: la ficha se mantiene activa.</li>
                    <li><strong>Descripción</strong> que explique qué hacés y en qué zona, escrita en castellano normal.</li>
                </ul>

                <h2>Paso 4: reseñas, que es donde se gana</h2>
                <p>Las reseñas son el factor que más mueve tu posición en el paquete local, y el que más se descuida. Tres cosas concretas:</p>
                <ol>
                    <li><strong>Pedilas sistemáticamente.</strong> No "cuando te acordás": después de cada trabajo terminado o cada compra. El mejor momento es cuando el cliente está contento, que suele ser justo al terminar. Mandale el link directo por WhatsApp: si tiene que buscar dónde dejarla, no la deja.</li>
                    <li><strong>Respondelas todas.</strong> Las buenas y sobre todo las malas. Google valora la interacción, pero más importante: el próximo cliente lee cómo respondés. Una respuesta tranquila y resolutiva a una queja convence más que veinte elogios.</li>
                    <li><strong>Nunca las compres.</strong> Google las detecta, las borra y puede suspenderte la ficha. El daño de perder la ficha es enorme comparado con el beneficio.</li>
                </ol>

                <h2>Paso 5: mantenela viva</h2>
                <p>Una ficha abandonada pierde posiciones frente a una activa. Publicá novedades cada tanto (promociones, productos nuevos, cambios de horario), respondé las preguntas que deja la gente en la sección de preguntas y respuestas —podés cargar vos mismo las más frecuentes— y actualizá las fotos.</p>

                <h2>Lo que sostiene todo esto: tu web</h2>
                <p>Google cruza la información de tu ficha con lo que encuentra en el resto de internet. Si tu negocio tiene un <a href="/paginas-web">sitio web propio</a> que dice lo mismo (mismo nombre, misma dirección, mismo teléfono) y explica tus servicios en detalle, tu ficha se vuelve mucho más creíble y posiciona mejor.</p>
                <p>Esa consistencia de datos entre tu web, tu ficha y tus redes es de las señales más subestimadas del SEO local. Cuando los datos no coinciden, Google desconfía y te muestra menos.</p>

                <div class="callout">
                    <p><strong>Si no querés hacerlo vos:</strong> lo configuramos y optimizamos nosotros como parte del trabajo de <a href="/marketing-digital-zona-oeste">SEO local</a>. Escribinos y lo revisamos juntos sin costo.</p>
                </div>'''

    return _post(
        slug="aparecer-en-google-maps",
        tldr=[
            "Es <strong>gratis</strong>, se hace en una tarde y la mayoría de tus competidores lo tiene a medias.",
            "El campo más importante de toda la ficha es la <strong>categoría principal</strong>. Elegí la específica, no la general.",
            "Podés aparecer <strong>sin local a la calle</strong>: se configura como negocio de servicio a domicilio.",
            "Las <strong>reseñas respondidas</strong> son lo que más mueve tu posición, y lo que menos hace la competencia.",
            "Nunca compres reseñas: Google las detecta y puede suspenderte la ficha.",
        ],
        cta_top=("<strong>Si no querés hacerlo vos:</strong> lo configuramos y optimizamos nosotros. Escribinos y lo revisamos juntos.",
                 "Quiero que lo hagan ustedes", "Quiero%20optimizar%20mi%20ficha%20de%20Google"),
        title="Cómo aparecer en Google Maps con tu negocio (guía 2026)",
        description="Guía paso a paso para aparecer en Google Maps: crear y verificar tu ficha de Google Business Profile, elegir bien la categoría y sumar reseñas.",
        h1="Cómo hacer que tu negocio aparezca en Google Maps",
        lead="Es gratis, se hace en una tarde y la mayoría de tus competidores lo tiene a medias. Para un negocio local es, con diferencia, la acción con mejor retorno por hora invertida.",
        read=7,
        prose=prose,
        faq_items=faq_items,
        keywords=["aparecer en google maps", "google business profile", "google my business",
                  "seo local", "ficha de google negocio"],
        related=[
            ("/marketing-digital-zona-oeste", "SEO local en Zona Oeste", "Lo configuramos y optimizamos por vos."),
            ("/paginas-web", "Páginas web", "El sitio propio que sostiene y potencia tu ficha."),
            ("/blog/cuanto-cuesta-una-pagina-web-argentina", "¿Cuánto cuesta una web?", "De qué depende el precio y qué preguntar."),
            ("/marketing-digital-moron", "Marketing digital en Morón", "Cómo destacar donde hay más competencia."),
        ],
    )


# ---------------------------------------------------------------------- ÍNDICE
POSTS = [
    ("/blog/cuanto-cuesta-una-pagina-web-argentina",
     "Precios", "¿Cuánto cuesta una página web en Argentina?",
     "De qué depende realmente el precio, por qué dos presupuestos por “lo mismo” pueden ser los dos honestos y las 5 preguntas que tenés que hacer antes de contratar.", 8),
    ("/blog/como-conseguir-clientes-por-instagram",
     "Redes", "Cómo conseguir clientes por Instagram",
     "Publicás seguido y no entra ni una consulta. Qué cambiar en tu perfil, qué contenido se guarda y por qué los primeros dos segundos deciden todo.", 9),
    ("/blog/chatbot-whatsapp-para-negocios",
     "Automatización", "Chatbot de WhatsApp: qué automatizar y qué no",
     "Qué conviene automatizar, cuándo usar IA y cuándo un menú simple, los 5 errores que arruinan un bot y por qué el seguimiento es la parte que más vende.", 8),
    ("/blog/aparecer-en-google-maps",
     "SEO local", "Cómo aparecer en Google Maps con tu negocio",
     "Guía paso a paso: crear y verificar la ficha, elegir bien la categoría, conseguir reseñas y posicionar en el bloque de tres resultados del mapa.", 7),
]


def blog_index():
    path = "/blog"
    cards = "\n".join(f'''                <article class="post-card reveal">
                    <div class="post-meta"><span>{cat}</span><span>·</span><span>{read} min</span></div>
                    <h2><a href="{href}">{title}</a></h2>
                    <p>{desc}</p>
                    <a href="{href}" class="link-arrow">Leer el artículo {C.ARROW_SVG}</a>
                </article>''' for href, cat, title, desc, read in POSTS)

    schema = S.dump([
        S.breadcrumb([("Inicio", "/"), ("Blog", path)]),
        {
            "@type": "Blog",
            "@id": f"{S.SITE}{path}#blog",
            "url": S.SITE + path,
            "name": "Blog de Tu Negocio En Las Redes",
            "description": "Guías prácticas de marketing digital, páginas web, redes sociales y automatización para negocios de Zona Oeste.",
            "inLanguage": "es-AR",
            "publisher": S.BUSINESS_REF,
            "blogPost": [
                {"@type": "BlogPosting", "headline": t, "url": S.SITE + h, "datePublished": PUB}
                for h, _, t, _, _ in POSTS
            ],
        },
    ])

    return path, (
        C.head(title="Blog de Marketing Digital y Páginas Web | Tu Negocio En Las Redes",
               description="Guías prácticas de marketing digital: precios de páginas web, clientes por Instagram, chatbots de WhatsApp y cómo aparecer en Google Maps.",
               path=path, schema=schema, og_title="Blog | Tu Negocio En Las Redes")
        + C.nav()
        + C.breadcrumb([("Inicio", "/"), ("Blog", None)])
        + C.page_hero(
            "Blog",
            'Guías prácticas de<br><span class="gradient-text">marketing digital.</span>',
            "Lo que aplicamos con nuestros clientes, explicado para que puedas hacerlo vos. Sin humo, sin promesas de primer puesto en treinta días y sin vender lo que no necesitás.",
            ctas=[("/contacto", "Hablar con el equipo", "btn-primary", False),
                  ("/servicios", "Ver servicios", "btn-ghost", False)])
        + f'''
    <section class="section-dark">
        <div class="container">
            <div class="post-grid">
{cards}
            </div>
        </div>
    </section>
'''
        + C.related_section('Nuestros<br><span class="gradient-text">servicios.</span>', [
            ("/paginas-web", "Páginas web", "Demo gratis de tu sitio en 72 horas."),
            ("/gestion-de-redes", "Gestión de redes", "Estrategia, diseño y reels con objetivo."),
            ("/automatizacion-whatsapp", "Automatización de WhatsApp", "Chatbots que atienden 24/7."),
            ("/marketing-digital-zona-oeste", "SEO local en Zona Oeste", "Para que te encuentren en tu zona."),
        ])
        + C.cta_section(
            '¿Preferís que lo<br><span class="gradient-text">hagamos nosotros?</span>',
            "Te armamos una demo real de tu página web, con tu logo y tus colores,<br>sin costo y sin compromiso.",
            "Quiero mi demo gratis →", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web")
        + C.FOOTER
    )


ALL = [blog_index, precio_pagina_web, clientes_instagram, chatbot_whatsapp, google_maps]
