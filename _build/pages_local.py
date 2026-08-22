# -*- coding: utf-8 -*-
"""
Landings de SEO local.

Ojo: NO son la misma página con el nombre del barrio cambiado. Google
penaliza eso como doorway pages. Cada una describe el tejido comercial
real de su localidad y tiene FAQ, ejemplos y ángulo propios.
"""

import chrome as C
import schemas as S
import icons as I
import components as CO

HUB = "/marketing-digital-zona-oeste"


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


def _page(*, path, city, title, description, og_title, h1, lead, prose, cards,
          cards_head, faq_items, related, areas, parent=True, tldr=None, cta_top=None):
    prose = CO.lead_block(prose, tldr, cta_top)
    trail = [("Inicio", "/")]
    if parent:
        trail.append(("Zona Oeste", HUB))
    trail.append((city, path))

    crumb = [("Inicio", "/")]
    if parent:
        crumb.append(("Zona Oeste", HUB))
    crumb.append((city, None))

    schema = S.dump([
        S.breadcrumb(trail),
        S.webpage(path, og_title, description),
        S.local_business(city, path, description, areas),
        S.faq(faq_items),
    ])
    return path, (
        C.head(title=title, description=description, path=path, schema=schema, og_title=og_title)
        + C.nav()
        + C.breadcrumb(crumb)
        + C.page_hero(f"Marketing digital en {city}", h1, lead)
        + _prose(prose)
        + I.grid(cards, tag="Servicios", h2=cards_head[0], sub=cards_head[1])
        + C.faq_section(faq_items, heading=f'Preguntas de negocios<br>de <span class="gradient-text">{city}.</span>')
        + C.related_section('Otras zonas y<br><span class="gradient-text">servicios.</span>', related)
        + C.cta_section(
            f'¿Empezamos por una demo gratis<br>de tu <span class="gradient-text">página web?</span>',
            f"Trabajamos con negocios de {city} y alrededores. Te armamos una demo real de tu sitio,<br>con tu logo y tus colores, sin costo y sin compromiso.",
            "Quiero mi demo gratis →",
            "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web")
        + C.FOOTER
    )


SERVICE_CARDS = [
    ("monitor", "Páginas web", "Sitios rápidos y mobile-first que convierten visitas en consultas por WhatsApp.", "Demo gratis"),
    ("share", "Gestión de redes", "Estrategia, diseño y reels para que tu Instagram genere clientes.", "Contenido con objetivo"),
    ("megaphone", "Publicidad digital", "Meta y Google Ads segmentados al radio real de tu negocio.", "Costo por consulta medido"),
    ("bot", "Automatización con IA", "Chatbots que responden 24/7 precios, horarios y turnos.", "Sin esperas"),
    ("database", "CRM a medida", "Para no perder el seguimiento de ninguna consulta.", "Software propio"),
    ("cart", "Tiendas online", "Catálogo, carrito, Mercado Pago y envíos por zona.", "Vender sin atender"),
]


# ------------------------------------------------------------------- ITUZAINGÓ
def ituzaingo():
    faq_items = [
        ("¿Trabajan con negocios de Ituzaingó?",
         "Sí, es nuestra zona. Somos de <strong>Zona Oeste</strong> y buena parte de nuestros clientes están en Ituzaingó, Castelar y Morón. Podemos coordinar una reunión presencial si preferís charlarlo en persona en vez de por videollamada."),
        ("¿Cuánto cuesta una página web en Ituzaingó?",
         "El precio no cambia por la localidad, cambia por lo que el sitio tiene que resolver: no es lo mismo una landing page que una web institucional o una tienda online. Te hacemos primero la <strong>demo gratis</strong> y recién con eso a la vista te pasamos un precio cerrado."),
        ("Mi negocio no aparece en Google Maps, ¿lo pueden resolver?",
         "Sí, y para un comercio de Ituzaingó suele ser lo más rentable que se puede hacer primero. Configuramos y optimizamos tu <strong>ficha de Google Business Profile</strong>: categoría correcta, zona de cobertura, horarios, fotos y estrategia de reseñas. Es lo que hace que aparezcas en el mapa cuando alguien busca tu rubro cerca."),
        ("¿Sirve hacer publicidad para un negocio chico de barrio?",
         "Sí, justamente porque se puede segmentar por radio geográfico. Podés mostrar tus anuncios solo a gente que está a pocos kilómetros de tu local, en Ituzaingó Norte, Sur, Villa Udaondo o Parque Leloir. Eso hace que un presupuesto chico rinda mucho más que en una campaña abierta."),
        ("Vendo en Parque Leloir, que es distinto al centro. ¿Cambia algo?",
         "Cambia bastante. Parque Leloir tiene un perfil residencial de quintas y casas, con demanda de servicios de mayor ticket: construcción, paisajismo, piletas, seguridad, eventos, servicio doméstico especializado. Ahí la estrategia se parece más a la de un servicio premium (autoridad, portfolio visual, reseñas) que a la de un comercio de paso."),
    ]

    prose = '''                <h2>Ituzaingó tiene un comercio de barrio fuerte y muy poco digitalizado</h2>
                <p>Ituzaingó dejó de ser parte del partido de Morón en los años noventa y desde entonces creció con identidad propia. Hoy convive un centro comercial denso alrededor de la estación del Sarmiento y las avenidas Rivadavia y Ratti, con zonas residenciales muy distintas entre sí: Ituzaingó Norte y Sur, Villa Udaondo y Parque Leloir.</p>
                <p>Esa mezcla genera una oportunidad concreta. Hay muchísimos comercios y profesionales con clientela fiel y buena reputación en el barrio, pero <strong>sin presencia digital</strong>: no aparecen en Google Maps con la categoría correcta, no tienen web, y su Instagram es una cuenta con doscientos seguidores y la última publicación de hace ocho meses.</p>
                <p>Mientras tanto, la gente de Ituzaingó busca en Google exactamente como en cualquier otro lado: "cerrajería cerca", "veterinaria Ituzaingó", "gimnasio Villa Udaondo". El que aparece primero se lleva la consulta, aunque no sea el mejor del rubro.</p>

                <h2>Por dónde conviene empezar</h2>
                <p>Para un negocio local de Ituzaingó, el orden que mejor funciona casi siempre es este:</p>
                <ol>
                    <li><strong>Google Business Profile.</strong> Es gratis, es lo más rápido y es lo que te mete en el mapa. Categoría correcta, horarios reales, fotos actualizadas y un sistema para pedir reseñas.</li>
                    <li><strong>Página web propia.</strong> Le da a Google algo que indexar y te saca de depender de que Instagram te muestre. Además es lo que sostiene tu ficha del mapa: los negocios con web propia posicionan mejor en el paquete local.</li>
                    <li><strong>Instagram con estrategia.</strong> Contenido pensado para tu zona, no publicaciones sueltas.</li>
                    <li><strong>Publicidad segmentada por radio.</strong> Solo cuando lo anterior ya está, porque si no estás pagando para llevar gente a un lugar que no convierte.</li>
                </ol>

                <h2>Rubros con los que más trabajamos en la zona</h2>
                <p>Gastronomía, gimnasios y estudios de entrenamiento, estética y peluquerías, salud (consultorios, kinesiología, nutrición), estudios contables y jurídicos, oficios (electricistas, plomeros, cerrajeros), indumentaria, veterinarias y salones de eventos. Podés ver <a href="/trabajos">algunos de esos proyectos funcionando</a>: varios son de acá.</p>

                <h2>Somos de acá</h2>
                <p>No es un detalle menor. Conocemos las zonas, sabemos que no es lo mismo un comercio sobre Rivadavia que un servicio en Parque Leloir, y podemos juntarnos a tomar un café en vez de mandarte un PDF. Si preferís charlarlo en persona, <a href="/contacto">escribinos</a> y coordinamos.</p>'''

    return _page(
        path="/marketing-digital-ituzaingo",
        tldr=[
            "Ituzaingó tiene un comercio de barrio fuerte y <strong>muy poco digitalizado</strong>: hacer lo básico bien ya te pone adelante.",
            "El orden que mejor rinde: <strong>ficha de Google primero</strong>, después web propia, después Instagram, y recién ahí publicidad.",
            "<strong>Parque Leloir juega distinto</strong> al centro: perfil residencial de quintas y servicios de mayor ticket.",
            "Somos de acá: podemos juntarnos a charlarlo en persona.",
        ],
        cta_top=("<strong>¿Arrancamos?</strong> Te hacemos la demo de tu página web, con tu logo y tus colores, sin costo.",
                 "Quiero mi demo gratis", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"),
        city="Ituzaingó",
        title="Agencia de Marketing Digital en Ituzaingó | Páginas Web y Redes",
        description="Agencia de marketing digital en Ituzaingó: páginas web, gestión de redes, Google Business Profile y publicidad local. Demo de tu web gratis.",
        og_title="Agencia de Marketing Digital en Ituzaingó",
        h1='Agencia de <span class="gradient-text">marketing digital</span><br>en Ituzaingó.',
        lead="Páginas web, gestión de redes, publicidad y automatización para comercios, profesionales y PyMEs de Ituzaingó, Villa Udaondo y Parque Leloir. Somos de la zona: podemos juntarnos a charlarlo en persona.",
        prose=prose,
        cards=SERVICE_CARDS,
        cards_head=('Qué hacemos por los<br><span class="gradient-text">negocios de Ituzaingó.</span>',
                    "Podés contratar un servicio suelto o el conjunto. Empezamos siempre por lo que más impacto tenga en tu caso."),
        faq_items=faq_items,
        areas=["Ituzaingó", "Villa Udaondo", "Parque Leloir", "Castelar", "Morón"],
        related=[
            ("/marketing-digital-moron", "Marketing digital en Morón", "El centro comercial más competitivo del oeste."),
            ("/marketing-digital-castelar", "Marketing digital en Castelar", "Comercios de cercanía y gastronomía."),
            ("/paginas-web", "Páginas web", "Demo gratis de tu sitio en 72 horas."),
            ("/publicidad-digital", "Publicidad digital", "Anuncios segmentados al radio real de tu local."),
        ],
    )


# ----------------------------------------------------------------------- MORÓN
def moron():
    faq_items = [
        ("¿Por qué es más difícil posicionar un negocio en Morón?",
         "Porque Morón es cabecera de partido y concentra la mayor densidad comercial del oeste. Eso significa <strong>más competencia por las mismas búsquedas</strong>: hay muchas más peluquerías, gimnasios y estudios contables compitiendo por \"cerca mío\" que en una localidad más chica. No es imposible, pero exige hacer bien lo que el resto hace a medias: reseñas, contenido propio y ficha de Google trabajada."),
        ("¿Cuánto cuesta anunciar en Google en Morón?",
         "El costo por clic en Morón suele ser más alto que en localidades vecinas justamente por la competencia. Por eso trabajamos con <strong>palabras clave más específicas</strong> y palabras clave negativas: en vez de pelear por \"peluquería\", que es carísima y trae de todo, vamos por búsquedas con intención concreta que convierten mucho mejor y cuestan menos."),
        ("Mi negocio está en Castelar o Haedo, ¿cuenta como Morón?",
         "Administrativamente sí: <strong>Castelar y Haedo pertenecen al partido de Morón</strong>. Pero para el buscador son localidades distintas y la gente busca por el nombre de su barrio, no por el partido. Si estás en Castelar conviene trabajar esa localidad específicamente; mirá la <a href=\"/marketing-digital-castelar\">página de Castelar</a>."),
        ("¿Sirve tener local a la calle y además web?",
         "Muchísimo, y es la combinación que mejor rinde. El local te da algo que la competencia puramente online no tiene: <strong>ficha de Google Maps con dirección real y reseñas</strong>. Sumarle una web propia potencia esa ficha y te deja captar también a quien busca sin saber todavía dónde queda tu negocio."),
        ("¿Cuánto tarda en posicionar un negocio de Morón en Google?",
         "Depende de por qué búsqueda. La <strong>ficha de Google Business Profile</strong> puede empezar a moverse en semanas, porque no depende de la antigüedad del sitio. El posicionamiento orgánico de una web nueva en una zona competitiva como Morón es más lento: primeros movimientos entre el <strong>segundo y el tercer mes</strong>, consolidación entre el <strong>cuarto y el sexto</strong>. Cualquiera que te prometa primer puesto en un mes en Morón no conoce el mercado o te está mintiendo."),
        ("Mi competencia aparece primero en el mapa. ¿Cómo los paso?",
         "Casi siempre por tres cosas, en este orden: <strong>cantidad y frescura de reseñas</strong>, qué tan completa está la ficha (categoría principal correcta, servicios cargados, fotos recientes, horarios exactos) y si tenés <strong>sitio web propio</strong> enlazado. En Morón lo que más se descuida es responder las reseñas: un negocio con 40 reseñas respondidas le suele ganar a uno con 120 mudas."),
        ("¿Conviene invertir en Google Ads en una zona tan competitiva?",
         "Sí, pero con precisión. En Morón el costo por clic es más alto que en localidades vecinas, así que trabajar con términos genéricos quema presupuesto rápido. La estrategia que funciona es ir por <strong>búsquedas específicas con intención concreta</strong>, sumar palabras clave negativas para no pagar clics que nunca iban a comprar, y apoyarse fuerte en remarketing."),
        ("¿Trabajan con profesionales, no solo con comercios?",
         "Sí. Estudios contables, abogados, consultorios, arquitectos e inmobiliarias son de los casos donde la web pesa más, porque la decisión se toma por confianza: la persona compara tres opciones, mira quién transmite más solidez y escribe. Ahí una web bien hecha define la consulta."),
    ]

    prose = '''                <h2>Morón compite distinto al resto del oeste</h2>
                <p>Morón es la cabecera del partido y el centro comercial más denso de la zona oeste. Su casco céntrico, con la peatonal, el Palacio Municipal y la Catedral, concentra una cantidad de comercios y servicios que no tiene ninguna de las localidades vecinas. Sumale la Universidad de Morón, que trae circulación de público joven todo el año.</p>
                <p>Para un negocio esto tiene una consecuencia directa: <strong>competís con muchos más</strong>. Cuando alguien busca "peluquería en Morón" o "estudio contable Morón", Google tiene decenas de opciones para elegir. En una localidad más chica alcanza con estar; en Morón hay que estar mejor.</p>

                <h2>Qué define quién aparece primero</h2>
                <p>En búsquedas locales con alta competencia, tres factores explican casi todo el resultado:</p>
                <ul>
                    <li><strong>Reseñas.</strong> Cantidad, puntaje y —esto es lo que casi nadie hace— que estén respondidas. Un negocio con cuarenta reseñas respondidas le gana casi siempre a uno con ciento veinte reseñas mudas.</li>
                    <li><strong>Ficha completa.</strong> Categoría principal correcta, categorías secundarias, servicios cargados, horarios reales, fotos recientes y publicaciones. La mayoría de las fichas de Morón están cargadas a medias.</li>
                    <li><strong>Sitio web propio.</strong> Google usa tu web para entender de qué se trata tu negocio. Sin web, la ficha queda coja frente a competidores que sí tienen.</li>
                </ul>

                <h2>Publicidad en un mercado caro</h2>
                <p>En Morón la pauta cuesta más porque hay más gente pujando por las mismas palabras. La respuesta no es poner más presupuesto: es <strong>ser más preciso</strong>. Búsquedas específicas en vez de genéricas, palabras clave negativas para no pagar clics que nunca iban a comprar, y remarketing sobre quien ya te visitó. Un presupuesto chico bien dirigido rinde más que uno grande mal segmentado. Lo desarrollamos en <a href="/publicidad-digital">publicidad digital</a>.</p>

                <h2>Morón no es una sola zona comercial</h2>
                <p>Una confusión que sale cara al segmentar publicidad: <strong>el partido de Morón incluye Castelar, Haedo, El Palomar y Villa Sarmiento</strong>, además del casco céntrico. Son mercados con perfiles distintos y precios distintos.</p>
                <ul>
                    <li><strong>Centro de Morón.</strong> La mayor densidad comercial del oeste, con la peatonal, el Palacio Municipal y la Catedral. Mucho tránsito peatonal, mucha competencia por las mismas búsquedas y costo por clic más alto.</li>
                    <li><strong>Haedo y Villa Sarmiento.</strong> Más residenciales, con comercio de cercanía y clientela de barrio que vuelve. Acá pesa muchísimo más la reseña y el boca a boca digital que la pauta.</li>
                    <li><strong>Castelar.</strong> Tiene identidad propia y la gente lo busca por su nombre, no por el partido. Si estás ahí, mirá la <a href="/marketing-digital-castelar">página de Castelar</a>.</li>
                    <li><strong>El Palomar.</strong> Zona con movimiento propio alrededor de la estación, con menos competencia digital que el centro.</li>
                </ul>
                <p>Si segmentás una campaña a "Morón" a secas, le estás pagando a Google o a Meta por mostrarle tu negocio a gente que quizás no cruza nunca hasta tu local. Nosotros trabajamos con <strong>radio real desde tu dirección</strong>, no con el nombre del partido.</p>

                <h2>Qué buscan realmente los clientes en Morón</h2>
                <p>Hay una diferencia grande entre lo que un negocio cree que la gente busca y lo que efectivamente escribe. En una zona con esta densidad comercial, las búsquedas que convierten casi nunca son las genéricas:</p>
                <table>
                    <thead>
                        <tr><th>Lo que el negocio quiere posicionar</th><th>Lo que la gente realmente escribe</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>peluquería</td><td>peluquería cerca abierta ahora</td></tr>
                        <tr><td>estudio contable</td><td>contador monotributo Morón</td></tr>
                        <tr><td>gimnasio</td><td>gimnasio Morón precios</td></tr>
                        <tr><td>cerrajería</td><td>cerrajero urgente 24hs Morón</td></tr>
                        <tr><td>agencia de marketing</td><td>quién me hace una página web en Morón</td></tr>
                    </tbody>
                </table>
                <p>La columna de la derecha tiene menos volumen, pero <strong>mucha más intención de compra y muchísima menos competencia</strong>. Es donde se gana. La columna de la izquierda es donde todos pelean y casi nadie convierte.</p>

                <h2>El contenido como diferencial</h2>
                <p>Cuando todos tus competidores hacen lo mismo, el contenido propio es lo que rompe el empate. Un estudio contable que publica sobre monotributo, un gimnasio que muestra rutinas y resultados reales, una veterinaria que explica planes de vacunación: eso genera búsquedas que la competencia no está capturando y construye autoridad. Es lo que trabajamos en <a href="/gestion-de-redes">gestión de redes</a> y en el <a href="/blog">blog</a>.</p>'''

    return _page(
        path="/marketing-digital-moron",
        tldr=[
            "Morón es el <strong>mercado más competitivo del oeste</strong>: hay muchos más negocios peleando por las mismas búsquedas.",
            "Tres factores explican casi todo el resultado local: <strong>reseñas respondidas, ficha completa y sitio web propio</strong>.",
            "La pauta cuesta más acá. La respuesta no es más presupuesto, es <strong>más precisión</strong>.",
            "Cuando todos hacen lo mismo, el <strong>contenido propio</strong> es lo que rompe el empate.",
        ],
        cta_top=("<strong>¿Competís en Morón?</strong> Revisamos tu ficha de Google y tu web, y te decimos qué te está frenando.",
                 "Quiero que lo revisen", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"),
        city="Morón",
        title="Agencia de Marketing Digital en Morón | Páginas Web y Publicidad",
        description="Agencia de marketing digital en Morón: páginas web, SEO local, ficha de Google y campañas segmentadas para el mercado más competitivo del oeste.",
        og_title="Agencia de Marketing Digital en Morón",
        h1='Agencia de <span class="gradient-text">marketing digital</span><br>en Morón.',
        lead="Morón es el mercado más competitivo del oeste: hay muchos más negocios peleando por las mismas búsquedas. Te ayudamos a destacar con web propia, ficha de Google trabajada y campañas precisas.",
        prose=prose,
        cards=SERVICE_CARDS,
        cards_head=('Qué hacemos por los<br><span class="gradient-text">negocios de Morón.</span>',
                    "En un mercado competitivo la diferencia no la hace hacer más, sino hacer bien lo que el resto hace a medias."),
        faq_items=faq_items,
        areas=["Morón", "Castelar", "Haedo", "El Palomar", "Villa Sarmiento", "Ituzaingó"],
        related=[
            ("/marketing-digital-castelar", "Marketing digital en Castelar", "Localidad del partido de Morón, con demanda propia."),
            ("/marketing-digital-ituzaingo", "Marketing digital en Ituzaingó", "Comercio de barrio y zona de quintas."),
            ("/publicidad-digital", "Publicidad digital", "Cómo rendir en un mercado con costo por clic alto."),
            ("/paginas-web", "Páginas web", "El activo que sostiene tu posicionamiento local."),
        ],
    )


# -------------------------------------------------------------------- CASTELAR
def castelar():
    faq_items = [
        ("¿Castelar es parte de Morón?",
         "Sí, <strong>Castelar pertenece al partido de Morón</strong>, igual que Haedo y El Palomar. Pero a la hora de buscar en Google la gente escribe \"Castelar\", no \"partido de Morón\". Por eso conviene trabajar la localidad de forma específica: categoría de Google con la dirección real, contenido que la mencione y campañas segmentadas a ese radio."),
        ("Mi negocio está en Castelar Norte. ¿Cambia la estrategia?",
         "Un poco sí. Castelar Norte y Castelar Sur tienen perfiles de consumo distintos, y eso se nota en qué tipo de negocio funciona y a qué precio. Cuando armamos las campañas segmentamos por radio real y no por \"Castelar\" a secas, así no pagás por mostrarle tu negocio a alguien que nunca va a cruzar las vías para llegar."),
        ("Tengo un local gastronómico. ¿Qué me conviene primero?",
         "Para gastronomía el orden suele ser: <strong>ficha de Google impecable</strong> (fotos de los platos, menú cargado, horarios exactos, reseñas respondidas), después Instagram con contenido de producto real, y recién después publicidad. Un dato concreto: las fotos propias de los platos rinden muchísimo más que las de banco, y el menú cargado en la ficha es de lo que más clics genera."),
        ("¿Me sirve una tienda online si vendo en un local de Castelar?",
         "Depende del volumen y del tipo de producto. Si vendés pocas unidades de ticket alto y te gusta asesorar, un catálogo con WhatsApp te alcanza. Si vendés muchas unidades que no requieren explicación y ya te cansaste de responder \"¿cuánto sale?\" todo el día, la <a href=\"/tiendas-online\">tienda online</a> se justifica sola."),
        ("¿Hacen reuniones presenciales en Castelar?",
         "Sí. Estamos a minutos, así que si preferís charlarlo cara a cara coordinamos sin problema. Muchos clientes arrancan así y después seguimos por WhatsApp."),
    ]

    prose = '''                <h2>Castelar: mucho comercio de cercanía y mucho emprendedor</h2>
                <p>Castelar pertenece al partido de Morón, pero tiene una identidad comercial propia bien marcada. La zona alrededor de la estación y de las avenidas Arias y Rivadavia concentra un comercio de cercanía muy activo: gastronomía, indumentaria, estética, servicios y una cantidad enorme de emprendimientos chicos que funcionan desde casa.</p>
                <p>Esa última categoría es la más interesante y la más desatendida. Hay muchísimos <strong>emprendedores de Castelar vendiendo exclusivamente por Instagram</strong>: pastelería, indumentaria infantil, deco, cosmética, catering. Funcionan bien hasta que chocan con el mismo techo: dependen del alcance del algoritmo, atienden cada venta a mano y no tienen dónde aparecer cuando alguien los busca en Google.</p>

                <h2>El techo de vender solo por Instagram</h2>
                <p>Instagram es excelente para que te descubran, pero tiene tres límites que aparecen siempre:</p>
                <ul>
                    <li><strong>No controlás el alcance.</strong> Si el algoritmo cambia, tus ventas cambian, y no hay nada que puedas hacer.</li>
                    <li><strong>No aparecés en Google.</strong> El que busca "tortas personalizadas Castelar" no te encuentra nunca, porque un perfil de Instagram no compite en esa búsqueda.</li>
                    <li><strong>Atendés cada venta a mano.</strong> Cada consulta de precio, stock y envío te consume tiempo que no escala.</li>
                </ul>
                <p>Los tres se resuelven con lo mismo: una <a href="/paginas-web">web propia</a> que aparezca en Google y, según el volumen, <a href="/automatizacion-whatsapp">automatización de WhatsApp</a> para las consultas repetidas.</p>

                <h2>Gastronomía en Castelar: lo que más mueve la aguja</h2>
                <p>Si tenés un local gastronómico, hay una acción que rinde más que cualquier otra y es gratis: <strong>tener la ficha de Google impecable</strong>. Fotos propias de los platos (no de banco), el menú cargado dentro de la ficha, horarios exactos incluyendo feriados, y responder todas las reseñas, sobre todo las malas. La mayoría de los locales de la zona tienen esto a medias, así que hacerlo bien te pone adelante sin invertir un peso en pauta.</p>

                <h2>Cómo trabajamos con negocios de Castelar</h2>
                <p>Arrancamos con una charla para entender qué vendés y a quién. Después te armamos la <strong>demo gratis</strong> de tu página, la ves funcionando y decidís. Si lo que necesitás primero no es una web sino ordenar tu Instagram o tu ficha de Google, te lo vamos a decir aunque signifique venderte menos.</p>'''

    return _page(
        path="/marketing-digital-castelar",
        tldr=[
            "Castelar pertenece al partido de Morón, pero <strong>la gente busca “Castelar”</strong>, no el partido.",
            "Hay muchísimos emprendedores vendiendo <strong>solo por Instagram</strong>, y ahí aparece el techo.",
            "Ese techo tiene tres partes: no controlás el alcance, no aparecés en Google y atendés cada venta a mano.",
            "Para gastronomía, la <strong>ficha de Google impecable</strong> rinde más que cualquier otra acción, y es gratis.",
        ],
        cta_top=("<strong>¿Vendés solo por Instagram?</strong> Te mostramos cómo se vería tu web propia, sin costo.",
                 "Quiero mi demo gratis", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"),
        city="Castelar",
        title="Agencia de Marketing Digital en Castelar | Páginas Web y Redes",
        description="Agencia de marketing digital en Castelar: páginas web, tiendas online y gestión de Instagram para comercios y emprendedores. Demo gratis.",
        og_title="Agencia de Marketing Digital en Castelar",
        h1='Agencia de <span class="gradient-text">marketing digital</span><br>en Castelar.',
        lead="Páginas web, tiendas online y gestión de redes para comercios y emprendedores de Castelar Norte y Sur. Especialmente si hoy vendés solo por Instagram y ya sentís el techo.",
        prose=prose,
        cards=SERVICE_CARDS,
        cards_head=('Qué hacemos por los<br><span class="gradient-text">negocios de Castelar.</span>',
                    "Desde emprendimientos que venden por Instagram hasta locales con años en la zona."),
        faq_items=faq_items,
        areas=["Castelar", "Morón", "Ituzaingó", "Haedo", "Villa Sarmiento"],
        related=[
            ("/marketing-digital-moron", "Marketing digital en Morón", "Castelar pertenece al partido de Morón."),
            ("/marketing-digital-ituzaingo", "Marketing digital en Ituzaingó", "La localidad vecina, con otro perfil comercial."),
            ("/tiendas-online", "Tiendas online", "Si ya vendés por Instagram y querés dejar de atender cada venta."),
            ("/gestion-de-redes", "Gestión de redes", "Para que tu Instagram genere consultas y no solo likes."),
        ],
    )


# ------------------------------------------------------------------ ZONA OESTE
def zona_oeste():
    faq_items = [
        ("¿Qué localidades cubren en Zona Oeste?",
         "Trabajamos principalmente con <strong>Ituzaingó, Morón, Castelar, Haedo, Ramos Mejía, El Palomar, Hurlingham, Merlo, Padua, Moreno y San Justo</strong>. Es la zona que conocemos y donde podemos coordinar reuniones presenciales. También atendemos clientes del resto del país de forma remota."),
        ("¿Necesito estar en Zona Oeste para trabajar con ustedes?",
         "No. Todo el trabajo se puede hacer a distancia y tenemos clientes fuera de la zona. Pero si estás cerca hay una ventaja real: entendemos el contexto de tu mercado, sabemos contra quién competís y podemos juntarnos en persona."),
        ("¿Qué es el SEO local y por qué me importa?",
         "Es el conjunto de acciones que hacen que aparezcas cuando alguien busca tu rubro <strong>con intención de zona</strong>: \"gimnasio cerca\", \"cerrajería Morón\", \"veterinaria abierta ahora\". Involucra tu ficha de Google Business Profile, las reseñas, la coherencia de tus datos de contacto en toda la web y el contenido local de tu sitio. Para un negocio de barrio suele ser el canal más rentable que existe."),
        ("¿Cuánto tarda en verse el resultado en Google?",
         "La ficha de Google Business Profile puede mover el amperímetro en <strong>semanas</strong>. El posicionamiento orgánico de un sitio web es más lento: los primeros movimientos se ven entre el <strong>segundo y el tercer mes</strong> y la consolidación entre el <strong>cuarto y el sexto</strong>. Cualquiera que te prometa primer puesto en treinta días te está mintiendo o va a hacer algo que después te va a costar caro."),
        ("¿Trabajan con negocios chicos o solo con empresas?",
         "Mayormente con negocios chicos y medianos: comercios, profesionales independientes, emprendedores y PyMEs familiares. Es el perfil con el que mejor trabajamos, porque las decisiones se toman rápido y los resultados se ven directo en la facturación."),
        ("¿Qué diferencia hay entre ustedes y una agencia grande?",
         "Que hablás directamente con quien hace el trabajo. No hay ejecutivo de cuentas que traduce lo que dijiste a un equipo que nunca vas a conocer. Somos chicos a propósito: eso nos permite responder rápido y hacernos cargo de lo que entregamos."),
    ]

    prose = '''                <h2>Zona Oeste es un mercado enorme y todavía poco digitalizado</h2>
                <p>El corredor oeste del conurbano —el que sigue la traza del Ferrocarril Sarmiento y el Acceso Oeste— concentra millones de personas repartidas en los partidos de Morón, Ituzaingó, Hurlingham, Tres de Febrero, Merlo, Moreno y La Matanza. Es uno de los tejidos comerciales más densos del país.</p>
                <p>Y sin embargo, una proporción altísima de esos negocios sigue trabajando digitalmente como en 2015: sin web, con la ficha de Google a medias o directamente sin reclamar, y con un Instagram que se actualiza cuando alguien se acuerda.</p>
                <p>Eso es un problema para ellos y una <strong>oportunidad concreta para el que sí lo hace bien</strong>. En la mayoría de los rubros locales del oeste, hacer lo básico correctamente ya te pone adelante de la mayoría de tu competencia.</p>

                <h2>Qué significa "hacer lo básico" en un negocio local</h2>
                <ol>
                    <li><strong>Reclamar y optimizar Google Business Profile.</strong> Gratis, rápido y el mayor retorno por hora invertida que existe para un negocio con local.</li>
                    <li><strong>Tener sitio web propio.</strong> Es lo que Google lee para entender qué hacés, y lo que sostiene tu posición en el mapa.</li>
                    <li><strong>Datos de contacto consistentes.</strong> El mismo nombre, la misma dirección y el mismo teléfono en tu web, tu ficha y tus redes. Cuando no coinciden, Google desconfía.</li>
                    <li><strong>Un sistema de reseñas.</strong> Pedirlas de forma sistemática después de cada trabajo, y responderlas todas.</li>
                    <li><strong>Contenido que mencione tu zona.</strong> Naturalmente, no repitiendo el nombre del barrio quince veces.</li>
                </ol>

                <h2>Nuestra cobertura</h2>
                <p>Trabajamos con negocios de toda la zona y tenemos páginas específicas para las localidades donde más clientes tenemos:</p>
                <ul>
                    <li><a href="/marketing-digital-ituzaingo">Marketing digital en Ituzaingó</a> — comercio de barrio, Villa Udaondo y Parque Leloir.</li>
                    <li><a href="/marketing-digital-moron">Marketing digital en Morón</a> — el mercado más competitivo del oeste.</li>
                    <li><a href="/marketing-digital-castelar">Marketing digital en Castelar</a> — comercio de cercanía y emprendedores.</li>
                </ul>
                <p>También trabajamos en Haedo, Ramos Mejía, El Palomar, Hurlingham, Merlo, Padua, Moreno y San Justo.</p>

                <h2>Todo lo que hacemos, en un solo lugar</h2>
                <p>La ventaja de trabajar con una sola agencia es que las piezas encajan: la <a href="/paginas-web">web</a> está pensada para recibir el tráfico de la <a href="/publicidad-digital">publicidad</a>, las <a href="/gestion-de-redes">redes</a> alimentan la web, la <a href="/automatizacion-whatsapp">automatización</a> responde las consultas que generan las dos, y el <a href="/crm-para-pymes">CRM</a> registra todo para que no se pierda ninguna. Cuando cada cosa la hace un proveedor distinto, esa cadena se corta en algún lado y nadie se hace cargo.</p>'''

    return _page(
        path=HUB,
        tldr=[
            "El corredor oeste es uno de los tejidos comerciales más densos del país y sigue <strong>muy poco digitalizado</strong>.",
            "En la mayoría de los rubros locales, <strong>hacer lo básico bien ya te pone adelante</strong> de casi toda tu competencia.",
            "Lo básico son cinco cosas: ficha de Google, sitio propio, datos de contacto consistentes, reseñas y contenido local.",
            "La ficha de Google puede mover el amperímetro en <strong>semanas</strong>; el orgánico, entre el segundo y el sexto mes.",
        ],
        cta_top=("<strong>Empezá por lo que más rinde:</strong> te armamos la demo de tu web y revisamos tu ficha de Google, sin costo.",
                 "Quiero mi demo gratis", "Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"),
        city="Zona Oeste",
        title="Marketing Digital en Zona Oeste | Tu Negocio En Las Redes",
        description="Agencia de marketing digital en Zona Oeste: páginas web, SEO local, redes, publicidad e IA. Ituzaingó, Morón, Castelar, Haedo y alrededores.",
        og_title="Agencia de Marketing Digital en Zona Oeste",
        h1='Agencia de <span class="gradient-text">marketing digital</span><br>en Zona Oeste.',
        lead="Trabajamos con comercios, profesionales y PyMEs de Ituzaingó, Morón, Castelar, Haedo, Ramos Mejía, Merlo y alrededores. Somos de acá y hablás siempre con quien hace el trabajo.",
        prose=prose,
        cards=SERVICE_CARDS,
        cards_head=('Todo lo que hacemos<br><span class="gradient-text">por tu negocio.</span>',
                    "Podés contratar un servicio suelto o el conjunto. Lo importante es que las piezas encajen entre sí."),
        faq_items=faq_items,
        areas=["Ituzaingó", "Morón", "Castelar", "Haedo", "Ramos Mejía", "El Palomar",
               "Hurlingham", "Merlo", "Moreno", "San Justo"],
        parent=False,
        related=[
            ("/marketing-digital-ituzaingo", "Ituzaingó", "Comercio de barrio, Villa Udaondo y Parque Leloir."),
            ("/marketing-digital-moron", "Morón", "El centro comercial más competitivo del oeste."),
            ("/marketing-digital-castelar", "Castelar", "Comercios de cercanía y emprendedores de Instagram."),
            ("/servicios", "Todos los servicios", "El detalle completo de lo que hacemos."),
        ],
    )


ALL = [zona_oeste, ituzaingo, moron, castelar]
