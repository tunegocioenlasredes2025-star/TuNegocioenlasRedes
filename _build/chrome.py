# -*- coding: utf-8 -*-
"""
Chrome compartido (head, nav, footer, CTA) para las landings generadas.

Las 6 páginas originales (index, servicios, ia, trabajos, nosotros, contacto)
siguen siendo HTML a mano. Este módulo sólo alimenta las páginas nuevas.
Si cambiás el nav o el footer, cambialos acá Y en esas 6.
"""

SITE = "https://www.tunegocioenlasredes.com.ar"
WA_MATEO = "5491150089069"
WA_SANTI = "5491122883750"

WA_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">'
          '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 '
          '1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 '
          '0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 '
          '4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 '
          '7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 '
          '01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 '
          '6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 '
          '11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 '
          '11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>')

ARROW_SVG = '<svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'


def head(*, title, description, path, schema, og_title=None, og_desc=None, page_type="website"):
    """path: ruta limpia con barra inicial, ej '/paginas-web'"""
    url = SITE + path
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <title>{title}</title>
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="{page_type}">
    <meta property="og:site_name" content="Tu Negocio En Las Redes">
    <meta property="og:title" content="{og_title or title}">
    <meta property="og:description" content="{og_desc or description}">
    <meta property="og:image" content="{SITE}/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="Tu Negocio En Las Redes - agencia de marketing digital, paginas web e IA en Zona Oeste">
    <meta property="og:locale" content="es_AR">
    <meta property="og:url" content="{url}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title or title}">
    <meta name="twitter:description" content="{og_desc or description}">
    <meta name="twitter:image" content="{SITE}/og-image.jpg">
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#060d1e">
    <meta name="google-site-verification" content="4Of5Hx8LEJC8QyjvEbFUF_-j8gUQ2gm2ILo7uYJ9NiU">
    <script>document.documentElement.classList.add('js')</script>
    <link rel="preload" href="/fonts/jakarta/PlusJakartaSans-latin.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/fonts.css">
    <link rel="stylesheet" href="/styles.css">
    <script type="application/ld+json">
{schema}
    </script>
</head>
<body>

    <a href="https://wa.me/{WA_MATEO}?text=Hola!%20Quiero%20saber%20m%C3%A1s%20sobre%20sus%20servicios" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Contactar por WhatsApp">
        {WA_SVG}
        <span class="whatsapp-tooltip">¡Escribinos!</span>
    </a>
'''


def nav(active=""):
    items = [("/", "Inicio"), ("/servicios", "Servicios"), ("/ia", "IA &amp; Automatización"),
             ("/trabajos", "Trabajos"), ("/nosotros", "Nosotros"), ("/contacto", "Contacto")]
    lis = "\n".join(
        f'                <li><a href="{href}" class="nav-link{" active" if href == active else ""}">{label}</a></li>'
        for href, label in items)
    return f'''
    <nav class="navbar scrolled" id="navbar">
        <div class="nav-container">
            <a href="/" class="nav-logo"><img src="/logo-256.png" alt="Tu Negocio En Las Redes - agencia de marketing digital en Zona Oeste" class="nav-logo-img" width="256" height="256" fetchpriority="high"></a>
            <button class="nav-toggle" id="navToggle" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
            <ul class="nav-menu" id="navMenu">
{lis}
                <li><a href="https://wa.me/{WA_MATEO}?text=Quiero%20una%20demo%20gratis" class="nav-cta" target="_blank">Demo Gratis →</a></li>
            </ul>
        </div>
    </nav>
'''


def breadcrumb(trail):
    """trail: lista de (nombre, href|None). El último debe llevar href None."""
    lis = []
    for name, href in trail:
        if href:
            lis.append(f'                <li><a href="{href}">{name}</a></li>')
        else:
            lis.append(f'                <li><span aria-current="page">{name}</span></li>')
    inner = "\n".join(lis)
    return f'''
    <nav class="breadcrumb" aria-label="Migas de pan">
        <div class="container">
            <ol>
{inner}
            </ol>
        </div>
    </nav>
'''


def page_hero(tag, h1, lead, ctas=None):
    ctas = ctas or [
        (f"https://wa.me/{WA_MATEO}?text=Quiero%20una%20demo%20gratis", "Quiero mi demo gratis →", "btn-primary", True),
        ("/contacto", "Hablar con el equipo", "btn-ghost", False),
    ]
    blank = ' target="_blank" rel="noopener"'
    btns = "\n".join(
        f'                <a href="{href}" class="btn {cls}"{blank if ext else ""}>{label}</a>'
        for href, label, cls, ext in ctas)
    return f'''
    <header class="page-hero">
        <div class="hero-bg">
            <div class="hero-orb hero-orb-1"></div>
            <div class="hero-orb hero-orb-2"></div>
            <div class="hero-grid"></div>
        </div>
        <div class="container">
            <span class="section-tag">{tag}</span>
            <h1>{h1}</h1>
            <p>{lead}</p>
            <div class="page-hero-ctas">
{btns}
            </div>
        </div>
    </header>
'''


def faq_section(items, intro="Preguntas frecuentes", heading=None):
    """items: lista de (pregunta, respuesta_html)"""
    heading = heading or 'Lo que todos preguntan<br><span class="gradient-text">antes de empezar.</span>'
    blocks = "\n".join(f'''                <details class="faq-item">
                    <summary>{q}</summary>
                    <div class="faq-answer"><p>{a}</p></div>
                </details>''' for q, a in items)
    return f'''
    <section class="faq section-dark">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">{intro}</span>
                <h2>{heading}</h2>
            </div>
            <div class="faq-list reveal delay-1">
{blocks}
            </div>
        </div>
    </section>
'''


def related_section(title, links):
    """links: lista de (href, titulo, descripcion)"""
    cards = "\n".join(
        f'''                <a href="{href}">
                    <strong>{t}</strong>
                    <span>{d}</span>
                </a>''' for href, t, d in links)
    return f'''
    <section class="section-mid">
        <div class="container">
            <div class="section-header reveal">
                <span class="section-tag">Seguí explorando</span>
                <h2>{title}</h2>
            </div>
            <div class="related reveal delay-1">
{cards}
            </div>
        </div>
    </section>
'''


def cta_section(h2, p, btn_text="Quiero mi demo gratis →", wa_text="Quiero%20mi%20demo%20gratis"):
    return f'''
    <section class="demo-section reveal">
        <div class="container">
            <div class="demo-card">
                <div class="demo-badge">GRATIS</div>
                <h2>{h2}</h2>
                <p>{p}</p>
                <a href="https://wa.me/{WA_MATEO}?text={wa_text}" class="btn btn-primary btn-large" target="_blank" rel="noopener">{btn_text}</a>
                <span class="demo-note">Sin costo. Sin compromiso. Con resultado.</span>
            </div>
        </div>
    </section>
'''


FOOTER = f'''
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <img src="/logo-256.png" alt="Tu Negocio En Las Redes" class="footer-logo-img" width="256" height="256" loading="lazy" decoding="async">
                    <p>Modernizamos negocios con marketing, automatización e inteligencia artificial.</p>
                    <a href="https://instagram.com/tunegocioenlasredes_" class="footer-ig" target="_blank" rel="noopener">@tunegocioenlasredes_</a>
                </div>
                <div class="footer-links">
                    <h4>Servicios</h4>
                    <ul>
                        <li><a href="/paginas-web">Páginas Web</a></li>
                        <li><a href="/tiendas-online">Tiendas Online</a></li>
                        <li><a href="/gestion-de-redes">Gestión de Redes</a></li>
                        <li><a href="/publicidad-digital">Publicidad Digital</a></li>
                        <li><a href="/automatizacion-whatsapp">Automatización WhatsApp</a></li>
                        <li><a href="/crm-para-pymes">CRM para PyMEs</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Zonas</h4>
                    <ul>
                        <li><a href="/marketing-digital-ituzaingo">Ituzaingó</a></li>
                        <li><a href="/marketing-digital-moron">Morón</a></li>
                        <li><a href="/marketing-digital-castelar">Castelar</a></li>
                        <li><a href="/marketing-digital-zona-oeste">Zona Oeste</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Empresa</h4>
                    <ul>
                        <li><a href="/nosotros">Nosotros</a></li>
                        <li><a href="/trabajos">Trabajos</a></li>
                        <li><a href="/blog">Blog</a></li>
                        <li><a href="/contacto">Contacto</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Contacto directo</h4>
                    <a href="https://wa.me/{WA_MATEO}" target="_blank" rel="noopener">Mateo: 11 5008-9069</a>
                    <a href="https://wa.me/{WA_SANTI}" target="_blank" rel="noopener">Santiago: 11 2288-3750</a>
                    <a href="https://instagram.com/tunegocioenlasredes_" target="_blank" rel="noopener">Instagram</a>
                    <a href="https://wa.me/{WA_MATEO}?text=Quiero%20mi%20demo%20gratis" class="footer-cta-btn" target="_blank" rel="noopener">Demo Gratis →</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2026 Tu Negocio En Las Redes. Zona Oeste, Buenos Aires.</p>
                <p>Diseño y desarrollo por <strong>Tu Negocio En Las Redes</strong></p>
            </div>
        </div>
    </footer>

    <script src="/main.js"></script>
</body>
</html>
'''
