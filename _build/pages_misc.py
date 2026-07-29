# -*- coding: utf-8 -*-
"""Páginas sueltas: 404."""

import chrome as C
import schemas as S


def not_found():
    path = "/404"
    html = C.head(
        title="Página no encontrada | Tu Negocio En Las Redes",
        description="La página que buscabas no existe o cambió de dirección. Volvé al inicio o mirá nuestros servicios de marketing digital, páginas web y automatización.",
        path=path,
        schema=S.dump([S.webpage(path, "Página no encontrada", "Error 404")]),
        og_title="Página no encontrada",
    )
    # noindex: no queremos la 404 en el índice de Google
    html = html.replace('<meta name="theme-color"',
                        '<meta name="robots" content="noindex, follow">\n    <meta name="theme-color"')

    html += C.nav()
    html += '''
    <header class="page-hero notfound">
        <div class="hero-bg">
            <div class="hero-orb hero-orb-1"></div>
            <div class="hero-orb hero-orb-2"></div>
            <div class="hero-grid"></div>
        </div>
        <div class="container">
            <span class="section-tag">Error 404</span>
            <div class="code gradient-text">404</div>
            <h1>Esta página no existe.</h1>
            <p>Puede que el enlace esté mal escrito o que la página haya cambiado de dirección. Te dejamos por dónde seguir.</p>
            <div class="page-hero-ctas">
                <a href="/" class="btn btn-primary">Volver al inicio</a>
                <a href="/contacto" class="btn btn-ghost">Escribinos</a>
            </div>
        </div>
    </header>
'''
    html += C.related_section('Lo que estabas<br><span class="gradient-text">buscando, quizás.</span>', [
        ("/paginas-web", "Páginas web", "Diseño y desarrollo de sitios profesionales. Demo gratis en 72 horas."),
        ("/gestion-de-redes", "Gestión de redes", "Estrategia, diseño y reels para que tu Instagram genere consultas."),
        ("/automatizacion-whatsapp", "Automatización de WhatsApp", "Chatbots con IA que atienden tu negocio 24/7."),
        ("/crm-para-pymes", "CRM para PyMEs", "Software a medida para no perder ninguna consulta."),
        ("/trabajos", "Trabajos", "Proyectos reales que desarrollamos, online funcionando hoy."),
        ("/blog", "Blog", "Guías prácticas de marketing digital, web y automatización."),
    ])
    html += C.FOOTER
    return path, html


ALL = [not_found]
