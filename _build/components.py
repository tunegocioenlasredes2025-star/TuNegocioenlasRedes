# -*- coding: utf-8 -*-
"""
Componentes que salieron del checklist SEO de 26 puntos:
TL;DR, CTA intercalado, tabla comparativa y barra para compartir.
"""

import urllib.parse
from chrome import SITE, WA_MATEO

TLDR_ICON = ('<svg viewBox="0 0 24 24"><path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 '
             '6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/></svg>')

SHARE_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
              'stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/>'
              '<circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/>'
              '<line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>')

WA_ICON = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967'
           '-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463'
           '-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149'
           '-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5'
           '-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 '
           '1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 '
           '1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>')

COPY_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2"/>'
             '<path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>')


def tldr(items, label="En 30 segundos"):
    """Key takeaways. Va apenas arranca el contenido, antes del primer H2."""
    lis = "\n".join("                        <li>" + i + "</li>" for i in items)
    return ('                <div class="tldr">\n'
            '                    <span class="tldr-label">' + TLDR_ICON + label + '</span>\n'
            '                    <ul>\n' + lis + '\n'
            '                    </ul>\n'
            '                </div>')


def cta_inline(text, btn="Quiero mi demo gratis",
               wa_text="Quiero%20una%20demo%20gratis%20de%20p%C3%A1gina%20web"):
    """CTA corto para intercalar después del primer párrafo, sin cortar la lectura."""
    return ('                <div class="cta-inline">\n'
            '                    <p>' + text + '</p>\n'
            '                    <a href="https://wa.me/' + WA_MATEO + '?text=' + wa_text +
            '" class="btn btn-primary" target="_blank" rel="noopener">' + btn + '</a>\n'
            '                </div>')


def table(headers, rows, caption=None):
    """Tabla comparativa. Google las lee bien y son candidatas a fragmento destacado."""
    th = "".join("<th>" + h + "</th>" for h in headers)
    trs = "\n".join("                        <tr>" + "".join("<td>" + c + "</td>" for c in r) + "</tr>"
                    for r in rows)
    cap = ('                        <caption>' + caption + '</caption>\n') if caption else ""
    return ('                <table>\n' + cap +
            '                    <thead>\n                        <tr>' + th + '</tr>\n                    </thead>\n'
            '                    <tbody>\n' + trs + '\n                    </tbody>\n'
            '                </table>')


def share_bar(path, title):
    """Botones para compartir: API nativa del celular + WhatsApp, LinkedIn y copiar link."""
    url = SITE + path
    wa = urllib.parse.quote(title + " " + url)
    enc = urllib.parse.quote(url, safe="")
    t = urllib.parse.quote(title)
    return ('\n    <section class="section-dark" style="padding-top:0">\n'
            '        <div class="container">\n'
            '            <div class="share">\n'
            '                <span class="share-label">Compartir</span>\n'
            '                <button type="button" class="js-share" data-url="' + url + '" data-title="' + t + '">'
            + SHARE_ICON + 'Compartir</button>\n'
            '                <a class="share-btn" href="https://wa.me/?text=' + wa + '" target="_blank" rel="noopener">'
            + WA_ICON + 'WhatsApp</a>\n'
            '                <a class="share-btn" href="https://www.linkedin.com/sharing/share-offsite/?url=' + enc +
            '" target="_blank" rel="noopener">'
            '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04'
            '-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 '
            '5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.55V9h3.57v11.45zM22.22 '
            '0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 '
            '22.22 0z"/></svg>LinkedIn</a>\n'
            '                <button type="button" class="js-copy" data-url="' + url + '">'
            + COPY_ICON + 'Copiar link</button>\n'
            '            </div>\n'
            '        </div>\n'
            '    </section>\n')


def insert_cta_after_first_p(prose, cta_html):
    """
    Mete el CTA justo después del primer párrafo del contenido.
    Ahí el lector ya entendió de qué va la página pero todavía no se fue.
    """
    i = prose.find("</p>")
    if i == -1:
        return prose
    i += len("</p>")
    return prose[:i] + "\n\n" + cta_html + "\n" + prose[i:]


def lead_block(prose, tldr_items=None, cta_args=None):
    """
    Prepara el arranque del contenido: TL;DR arriba de todo y CTA después del
    primer párrafo. Se llama desde cada generador para no repetir la lógica.
    """
    if cta_args:
        prose = insert_cta_after_first_p(prose, cta_inline(*cta_args))
    if tldr_items:
        prose = tldr(tldr_items) + "\n\n" + prose
    return prose
