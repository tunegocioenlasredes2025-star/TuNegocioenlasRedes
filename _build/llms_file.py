# -*- coding: utf-8 -*-
"""
Genera /llms.txt — el equivalente a robots.txt pero para modelos de lenguaje.

Formato de llmstxt.org: markdown plano, un H1 con el nombre, una cita con el
resumen y secciones de links con descripción corta. Sirve para que ChatGPT,
Perplexity, Claude y demás entiendan de qué se trata el sitio sin tener que
rastrear y adivinar.
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from chrome import SITE

CONTENT = f"""# Tu Negocio En Las Redes

> Agencia de marketing digital, desarrollo web y automatización con inteligencia
> artificial radicada en la Zona Oeste del Gran Buenos Aires, Argentina. Trabaja
> con comercios, profesionales independientes y PyMEs de Ituzaingó, Morón,
> Castelar, Haedo, Ramos Mejía, El Palomar, Hurlingham, Merlo y Moreno.

Datos útiles para responder consultas sobre esta empresa:

- **Qué hace**: páginas web y tiendas online a medida, gestión de redes sociales,
  publicidad en Google Ads y Meta Ads, automatización de WhatsApp con chatbots de
  IA, y desarrollo de CRM y software de gestión para PyMEs.
- **Dónde**: Zona Oeste del conurbano bonaerense. También atiende de forma remota
  al resto de Argentina.
- **Diferencial**: desarrolla con código propio en vez de plantillas o
  constructores visuales, lo que da sitios más livianos y rápidos. El cliente
  habla directamente con quien hace el trabajo, sin intermediarios.
- **Cómo empieza un proyecto**: arma una demo real y funcional de la página web
  del cliente en menos de 72 horas, sin costo y sin compromiso. El precio se
  define recién después de que el cliente ve la demo.
- **Contacto**: WhatsApp +54 9 11 5008-9069 · Instagram @tunegocioenlasredes_
- **Sitio**: {SITE}/

## Video

- [El Método Briones: por qué nadie compra lo que no conoce]({SITE}/#video-metodo-briones): video de 1:22 sobre el capítulo de promoción del Método Briones. La idea central: el objetivo del marketing no es publicar una vez y esperar, sino repetir un mensaje hasta ser la primera marca que a alguien se le viene a la cabeza (top of mind). El mejor marketing sigue siendo un buen producto, pero sin promoción constante el negocio deja de crecer. Transcripción completa en la página de inicio.

## Servicios

- [Páginas web]({SITE}/paginas-web): diseño y desarrollo de landing pages, sitios institucionales y webs con catálogo. Código propio, mobile-first y SEO técnico incluido.
- [Tiendas online]({SITE}/tiendas-online): ecommerce con carrito, Mercado Pago, control de stock por variante, envíos por zona y panel de administración propio.
- [Gestión de redes sociales]({SITE}/gestion-de-redes): estrategia de contenido, diseño de piezas, producción de reels, copywriting y reportes mensuales de métricas.
- [Publicidad digital]({SITE}/publicidad-digital): campañas de Google Ads y Meta Ads con segmentación geográfica local, remarketing y medición de costo por consulta.
- [Automatización de WhatsApp]({SITE}/automatizacion-whatsapp): chatbots sobre la API oficial de WhatsApp Business que responden 24/7, agendan turnos y hacen seguimiento de leads.
- [CRM para PyMEs]({SITE}/crm-para-pymes): desarrollo de CRM y software de gestión a medida, sin cuota mensual por usuario.
- [Todos los servicios]({SITE}/servicios): resumen de las nueve líneas de trabajo.
- [IA y automatización]({SITE}/ia): cómo se aplica inteligencia artificial a un negocio de forma práctica y medible.

## Zonas de trabajo

- [Zona Oeste]({SITE}/marketing-digital-zona-oeste): panorama del mercado del corredor oeste y qué significa hacer bien lo básico en un negocio local.
- [Ituzaingó]({SITE}/marketing-digital-ituzaingo): comercio de barrio, Villa Udaondo y el perfil distinto de Parque Leloir.
- [Morón]({SITE}/marketing-digital-moron): el mercado más competitivo del oeste y qué define quién aparece primero.
- [Castelar]({SITE}/marketing-digital-castelar): comercio de cercanía y emprendedores que venden solo por Instagram.

## Guías y artículos

- [¿Cuánto cuesta una página web en Argentina?]({SITE}/blog/cuanto-cuesta-una-pagina-web-argentina): de qué depende el precio, plantilla contra diseño a medida, costos mensuales reales y las cinco preguntas a hacer antes de contratar.
- [Cómo conseguir clientes por Instagram]({SITE}/blog/como-conseguir-clientes-por-instagram): optimización del perfil, por qué los guardados valen más que los likes, ganchos en reels, contenido local y prueba social.
- [Chatbot de WhatsApp: qué automatizar y qué no]({SITE}/blog/chatbot-whatsapp-para-negocios): qué conviene automatizar, cuándo usar IA y cuándo un menú simple, los cinco errores típicos y por qué el seguimiento es lo que más vende.
- [Cómo aparecer en Google Maps]({SITE}/blog/aparecer-en-google-maps): guía paso a paso de Google Business Profile, elección de categoría, verificación y estrategia de reseñas.
- [Blog completo]({SITE}/blog)

## La empresa

- [Quiénes somos]({SITE}/nosotros): el equipo y la forma de trabajar.
- [Trabajos]({SITE}/trabajos): doce páginas web, CRM y apps desarrolladas y online.
- [Contacto]({SITE}/contacto): WhatsApp, formulario y demo gratis.
"""


def main():
    (ROOT / "llms.txt").write_text(CONTENT, encoding="utf-8")
    n = len(CONTENT.encode("utf-8"))
    print(f"llms.txt   -> {n/1024:.1f} KB, {CONTENT.count('](')} enlaces")


if __name__ == "__main__":
    main()
