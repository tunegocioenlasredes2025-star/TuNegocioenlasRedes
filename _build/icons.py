# -*- coding: utf-8 -*-
"""Iconos Lucide inline (mismo set que ya usa el sitio)."""

_P = {
    "monitor":   '<rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/>',
    "smartphone":'<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    "zap":       '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>',
    "search":    '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "cart":      '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
    "share":     '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/>',
    "target":    '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "megaphone": '<path d="m3 11 18-5v12L3 13"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "bot":       '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    "message":   '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z"/>',
    "database":  '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>',
    "chart":     '<path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/>',
    "users":     '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "calendar":  '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    "shield":    '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    "sparkles":  '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .962 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.962 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/>',
    "gauge":     '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "pen":       '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    "camera":    '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3z"/><circle cx="12" cy="13" r="3"/>',
    "package":   '<path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "credit":    '<rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/>',
    "map":       '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    "clock":     '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "check":     '<path d="M20 6 9 17l-5-5"/>',
    "layers":    '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m6.08 10.37-3.5 1.59a1 1 0 0 0 0 1.83l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9a1 1 0 0 0 0-1.83l-3.5-1.6"/><path d="m6.08 15.37-3.5 1.59a1 1 0 0 0 0 1.83l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9a1 1 0 0 0 0-1.83l-3.5-1.6"/>',
    "refresh":   '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    "code":      '<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>',
}


def icon(name):
    return f'<svg viewBox="0 0 24 24">{_P[name]}</svg>'


def card(icon_name, title, text, tag=None, delay=""):
    tag_html = f'\n                    <span class="servicio-tag">{tag}</span>' if tag else ""
    cls = f"servicio-card reveal{(' ' + delay) if delay else ''}"
    return f'''                <div class="{cls}">
                    <div class="servicio-icon">{icon(icon_name)}</div>
                    <h3>{title}</h3>
                    <p>{text}</p>{tag_html}
                </div>'''


def grid(cards, section_class="servicios section-mid", tag=None, h2=None, sub=None):
    delays = ["", "delay-1", "delay-2"]
    body = "\n".join(card(*c[:4], delay=delays[i % 3]) for i, c in enumerate(cards))
    header = ""
    if h2:
        sub_html = f'\n                <p class="section-subtitle">{sub}</p>' if sub else ""
        tag_html = f'<span class="section-tag">{tag}</span>\n                ' if tag else ""
        header = f'''            <div class="section-header reveal">
                {tag_html}<h2>{h2}</h2>{sub_html}
            </div>
'''
    return f'''
    <section class="{section_class}">
        <div class="container">
{header}            <div class="servicios-grid">
{body}
            </div>
        </div>
    </section>
'''
