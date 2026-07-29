# -*- coding: utf-8 -*-
"""Constructores de JSON-LD para las landings generadas."""

import json
from chrome import SITE, WA_MATEO

BUSINESS_REF = {"@id": f"{SITE}/#business"}

# Coordenadas del centro del área de cobertura (Ituzaingó, Buenos Aires)
GEO = {"@type": "GeoCoordinates", "latitude": -34.6583, "longitude": -58.6706}


def dump(graph):
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent=6)


def breadcrumb(trail):
    """trail: lista de (nombre, path). path relativo con barra inicial."""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": SITE + path}
            for i, (name, path) in enumerate(trail, start=1)
        ],
    }


def webpage(path, name, description, page_type="WebPage"):
    return {
        "@type": page_type,
        "@id": f"{SITE}{path}#webpage",
        "url": SITE + path,
        "name": name,
        "description": description,
        "inLanguage": "es-AR",
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": BUSINESS_REF,
        "publisher": BUSINESS_REF,
    }


def service(name, service_type, description, path, area="Zona Oeste, Buenos Aires", offers=None):
    s = {
        "@type": "Service",
        "@id": f"{SITE}{path}#service",
        "name": name,
        "serviceType": service_type,
        "description": description,
        "url": SITE + path,
        "areaServed": area if isinstance(area, list) else {"@type": "AdministrativeArea", "name": area},
        "provider": {
            "@type": "ProfessionalService",
            "@id": f"{SITE}/#business",
            "name": "Tu Negocio En Las Redes",
            "url": SITE + "/",
            "telephone": "+" + WA_MATEO,
        },
        "availableChannel": {
            "@type": "ServiceChannel",
            "serviceUrl": SITE + path,
            "servicePhone": {"@type": "ContactPoint", "telephone": "+" + WA_MATEO, "contactType": "sales"},
        },
    }
    if offers:
        s["hasOfferCatalog"] = {
            "@type": "OfferCatalog",
            "name": name,
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": o}} for o in offers
            ],
        }
    return s


def faq(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in items
        ],
    }


def local_business(city, path, description, areas):
    """LocalBusiness por localidad, con geo y horarios."""
    return {
        "@type": "ProfessionalService",
        "@id": f"{SITE}{path}#localbusiness",
        "name": f"Tu Negocio En Las Redes — Agencia de Marketing Digital en {city}",
        "description": description,
        "url": SITE + path,
        "telephone": "+" + WA_MATEO,
        "priceRange": "$$",
        "currenciesAccepted": "ARS",
        "paymentAccepted": "Efectivo, Transferencia bancaria, Mercado Pago",
        "image": f"{SITE}/og-image.jpg",
        "logo": f"{SITE}/logo-512.png",
        "parentOrganization": BUSINESS_REF,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": city,
            "addressRegion": "Buenos Aires",
            "addressCountry": "AR",
        },
        "geo": GEO,
        "areaServed": [{"@type": "City", "name": a} for a in areas],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "09:00", "closes": "19:00",
        }, {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": "Saturday", "opens": "10:00", "closes": "14:00",
        }],
        "sameAs": ["https://instagram.com/tunegocioenlasredes_"],
    }


def article(path, headline, description, published, modified=None, keywords=None):
    return {
        "@type": "BlogPosting",
        "@id": f"{SITE}{path}#article",
        "headline": headline,
        "description": description,
        "url": SITE + path,
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}{path}"},
        "datePublished": published,
        "dateModified": modified or published,
        "inLanguage": "es-AR",
        "image": f"{SITE}/og-image.jpg",
        "keywords": keywords or [],
        "author": {"@type": "Organization", "name": "Tu Negocio En Las Redes", "url": SITE + "/"},
        "publisher": {
            "@type": "Organization",
            "name": "Tu Negocio En Las Redes",
            "url": SITE + "/",
            "logo": {"@type": "ImageObject", "url": f"{SITE}/logo-512.png", "width": 512, "height": 512},
        },
    }


def strip_tags(html):
    import re
    txt = re.sub(r"<[^>]+>", "", html)
    return re.sub(r"\s+", " ", txt).strip()
