// NAVBAR SCROLL
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });

// MOBILE NAV — con bloqueo de scroll a prueba de iOS Safari
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
let menuOpen = false;
let scrollLockY = 0;

function lockScroll() {
    scrollLockY = window.scrollY || document.documentElement.scrollTop;
    document.body.style.position = 'fixed';
    document.body.style.top = `-${scrollLockY}px`;
    document.body.style.left = '0';
    document.body.style.right = '0';
    document.body.style.width = '100%';
}

function unlockScroll() {
    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.left = '';
    document.body.style.right = '';
    document.body.style.width = '';
    // Restaurar la posición sin animación (evita el "salto" al cerrar)
    const prevBehavior = document.documentElement.style.scrollBehavior;
    document.documentElement.style.scrollBehavior = 'auto';
    window.scrollTo(0, scrollLockY);
    document.documentElement.style.scrollBehavior = prevBehavior;
}

function setMenu(open) {
    menuOpen = open;
    navMenu.classList.toggle('open', open);
    navToggle.classList.toggle('active', open);
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.classList.toggle('menu-open', open);

    if (open) lockScroll();
    else unlockScroll();
}

navToggle.addEventListener('click', () => setMenu(!menuOpen));
navMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
// Cerrar con Escape
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && menuOpen) setMenu(false); });

// SCROLL REVEAL
// Antes esto usaba IntersectionObserver y tenia un bug grave: si el visitante
// scrolleaba rapido (una rueda de mouse mueve 2000px de una), las secciones
// pasaban volando entre frames, el observer no llegaba a registrarlas y
// quedaban invisibles PARA SIEMPRE. La pagina se veia con huecos negros.
//
// Ahora se revisa la posicion real en cada scroll: si el borde superior de un
// elemento ya cruzo el pliegue, se revela. No se puede "perder" nada, porque
// los que quedaron arriba tienen top negativo y tambien entran.
const revealPendientes = [...document.querySelectorAll('.reveal')];

function revisarReveal() {
    const limite = window.innerHeight - 60;
    for (let i = revealPendientes.length - 1; i >= 0; i--) {
        if (revealPendientes[i].getBoundingClientRect().top < limite) {
            revealPendientes[i].classList.add('visible');
            revealPendientes.splice(i, 1);
        }
    }
    if (!revealPendientes.length) {
        window.removeEventListener('scroll', pedirRevision);
        window.removeEventListener('resize', pedirRevision);
    }
}

let revisionPedida = false;
function pedirRevision() {
    if (revisionPedida) return;
    revisionPedida = true;
    requestAnimationFrame(() => { revisionPedida = false; revisarReveal(); });
}

window.addEventListener('scroll', pedirRevision, { passive: true });
window.addEventListener('resize', pedirRevision, { passive: true });
revisarReveal();
// Red de seguridad: si algo sale mal, a los 4 segundos se muestra todo igual.
setTimeout(() => revealPendientes.splice(0).forEach(el => el.classList.add('visible')), 4000);

// COUNTER ANIMATION
function animateCounter(el) {
    const target = parseInt(el.dataset.target);
    const duration = 1600;
    const start = performance.now();
    const update = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        // toLocaleString para que 2600 se lea 2.600 y no 2600
        el.textContent = Math.round(eased * target).toLocaleString('es-AR');
        if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
}

// Se mira .stats-grid y no .stats: en el home los numeros se mudaron
// adentro de la franja de prueba y la seccion .stats ya no existe.
const statsEl = document.querySelector('.stats-grid');

// COUNTER OBSERVER
const counterObs = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
        document.querySelectorAll('.stat-number').forEach(animateCounter);
        counterObs.disconnect();
    }
}, { threshold: 0.4 });
if (statsEl) counterObs.observe(statsEl);

// SMOOTH SCROLL
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
        const target = document.querySelector(anchor.getAttribute('href'));
        if (target) {
            e.preventDefault();
            const y = target.getBoundingClientRect().top + window.pageYOffset - 80;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    });
});

// CONTACT FORM → WhatsApp
//
// OJO: hoy el formulario NO guarda el lead en ningun lado. Arma el mensaje y
// abre WhatsApp; si la persona cierra esa pestana antes de tocar "enviar", la
// consulta se perdio y no queda rastro de que existio.
//
// LEAD_ENDPOINT queda vacio A PROPOSITO: no hay todavia un endpoint real
// (Formspree, una funcion de Vercel, un Apps Script). Cuando exista, se pega
// la URL aca y el guardado se enciende solo, sin tocar nada mas.
const LEAD_ENDPOINT = '';

const contactForm = document.getElementById('contactForm');
if (contactForm) {
    const estado = document.getElementById('formEstado');
    const campo = (n) => contactForm.querySelector(`[name="${n}"]`);
    const valor = (n) => { const c = campo(n); return c ? c.value.trim() : ''; };

    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const nombre = valor('nombre');
        const negocio = valor('negocio');
        const tel = valor('telefono');
        const servicio = valor('servicio');
        const msg = valor('mensaje');

        const text = [
            `Hola! Soy ${nombre}${negocio ? ' de ' + negocio : ''}.`,
            `Quiero información sobre: ${servicio}.`,
            tel ? `Mi WhatsApp: ${tel}.` : '',
            msg
        ].filter(Boolean).join(' ');

        const url = `https://wa.me/5491150089069?text=${encodeURIComponent(text)}`;

        // WhatsApp se abre PRIMERO y siempre. Si el guardado falla, tarda o
        // esta apagado, la consulta llega igual: nunca se pierde un lead por
        // esperar a un fetch.
        // Sin 'noopener' en los features: pasarlo hace que window.open devuelva
        // siempre null y entonces no hay forma de distinguir "abrio bien" de
        // "el navegador lo bloqueo". Se corta el opener a mano justo despues.
        const ventana = window.open(url, '_blank');
        if (ventana) { try { ventana.opener = null; } catch (_) {} }

        if (LEAD_ENDPOINT) {
            try {
                fetch(LEAD_ENDPOINT, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ nombre, negocio, telefono: tel, servicio, mensaje: msg,
                                           origen: location.pathname }),
                    keepalive: true
                }).catch(() => { /* el lead ya viaja por WhatsApp */ });
            } catch (_) { /* idem */ }
        }

        if (estado) {
            estado.hidden = false;
            if (ventana) {
                estado.innerHTML = 'Listo: te abrimos WhatsApp con el mensaje ya escrito. ' +
                    '<strong>Tocá enviar ahí</strong> para que nos llegue.';
            } else {
                // El navegador bloqueo la ventana emergente: se le da el link a mano
                // en vez de dejarlo creyendo que mando algo.
                estado.innerHTML = 'Tu navegador bloqueó la ventana de WhatsApp. ' +
                    `<a href="${url}" target="_blank" rel="noopener">Abrila desde acá</a> ` +
                    'para mandarnos la consulta.';
            }
            estado.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    });
}

// IA PROGRESS BAR animation on scroll
const progressBar = document.querySelector('.ia-progress-bar');
if (progressBar) {
    const targetWidth = progressBar.style.width;
    progressBar.style.width = '0%';
    new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            setTimeout(() => { progressBar.style.transition = 'width 1.5s ease'; progressBar.style.width = targetWidth; }, 300);
        }
    }, { threshold: 0.5 }).observe(progressBar);
}

// COMPARTIR ARTÍCULO
// Usa la hoja de compartir nativa del celular; en escritorio copia el link.
document.querySelectorAll('.js-share').forEach(btn => {
    btn.addEventListener('click', async () => {
        const url = btn.dataset.url;
        const title = btn.dataset.title || document.title;
        if (navigator.share) {
            try { await navigator.share({ title, url }); } catch (e) { /* el usuario canceló */ }
        } else {
            copyLink(url, btn);
        }
    });
});

document.querySelectorAll('.js-copy').forEach(btn => {
    btn.addEventListener('click', () => copyLink(btn.dataset.url, btn));
});

async function copyLink(url, btn) {
    const original = btn.innerHTML;
    try {
        await navigator.clipboard.writeText(url);
    } catch (e) {
        // Fallback para navegadores sin permiso de portapapeles
        const ta = document.createElement('textarea');
        ta.value = url;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); } catch (_) {}
        document.body.removeChild(ta);
    }
    btn.textContent = '¡Link copiado!';
    setTimeout(() => { btn.innerHTML = original; }, 1800);
}

// VIDEO DEL REEL
// preload="none" y sin autoplay: el archivo pesa, asi que solo se descarga
// cuando el visitante decide verlo.
(() => {
    const video = document.getElementById('reelBriones');
    const boton = document.getElementById('reelPlay');
    if (!video || !boton) return;

    boton.addEventListener('click', () => {
        video.controls = true;
        video.play();
        boton.classList.add('oculto');
    });
    video.addEventListener('pause', () => {
        if (video.currentTime === 0 || video.ended) boton.classList.remove('oculto');
    });
})();

// ─────────────────────────────────────────────────────────────────────
// MEDICIÓN GA4
// Un único listener delegado en document. No hace falta tocar el HTML ni
// volver a enganchar nada cuando se agrega un botón nuevo: cualquier link a
// wa.me que aparezca mañana se mide solo.
//
// IMPORTANTE: en GA4 hay que marcar a mano como conversión los eventos
// "click_whatsapp" y "form_submit" (Administrar → Eventos → marcar como
// evento clave). Enviarlos no alcanza para que cuenten como conversión.
// ─────────────────────────────────────────────────────────────────────

function tnrEvento(nombre, params) {
    // Si el visitante bloquea el script de Google (bloqueadores, Brave), gtag
    // no existe: se ignora en silencio en vez de romper el click.
    if (typeof gtag === 'function') gtag('event', nombre, params || {});
}

// De qué parte de la página salió el click. Sirve para saber cuál de los
// ocho botones de WhatsApp es el que realmente trae las consultas.
function tnrUbicacion(el) {
    const marcado = el.closest('[data-ga-ubicacion]');
    if (marcado) return marcado.dataset.gaUbicacion;
    if (el.closest('.mobile-cta')) return 'barra_mobile';
    if (el.classList.contains('whatsapp-float') || el.closest('.whatsapp-float')) return 'boton_flotante';
    if (el.closest('.navbar')) return 'navbar';
    if (el.closest('.footer')) return 'footer';
    if (el.closest('.hero')) return 'hero';
    if (el.closest('.demo-section')) return 'demo';
    if (el.closest('.video-reel')) return 'video';
    if (el.closest('.trabajos, .trabajo-card')) return 'casos';
    if (el.closest('.problema')) return 'la_realidad';
    if (el.closest('.contacto-form')) return 'formulario';
    const seccion = el.closest('section');
    return seccion ? (seccion.className.trim().split(/\s+/)[0] || 'seccion') : 'otro';
}

document.addEventListener('click', (e) => {
    const a = e.target.closest('a');
    if (!a) return;
    const href = a.getAttribute('href') || '';

    if (href.indexOf('wa.me') !== -1 || href.indexOf('api.whatsapp.com') !== -1) {
        tnrEvento('click_whatsapp', {
            ubicacion: tnrUbicacion(a),
            pagina: location.pathname
        });
        return;
    }

    // Salida al sitio de un cliente desde el portfolio
    const tarjeta = a.closest('.trabajo-card, .portfolio-card');
    if (tarjeta && /^https?:/i.test(href) && href.indexOf('tunegocioenlasredes') === -1) {
        const titulo = tarjeta.querySelector('h3, h2');
        tnrEvento('click_ver_sitio', {
            proyecto: titulo ? titulo.textContent.trim() : href,
            pagina: location.pathname
        });
    }
}, true);

// Envío del formulario de contacto (el detalle de qué se manda está en el
// handler del formulario; acá solo se mide que ocurrió).
document.addEventListener('submit', (e) => {
    const f = e.target;
    if (f && f.id === 'contactForm') {
        const s = f.querySelector('[name="servicio"]');
        tnrEvento('form_submit', {
            pagina: location.pathname,
            servicio: s ? s.value : ''   // dato no personal: sirve para saber que se pide mas
        });
    }
}, true);

// Reproducción del video del método
(() => {
    const video = document.getElementById('reelBriones');
    if (!video) return;
    video.addEventListener('play', () => {
        tnrEvento('play_video', { video: 'metodo-briones' });
    }, { once: true });
})();

// Scroll al 90% de la página: una sola vez por sesión y por página.
(() => {
    const clave = 'tnr_scroll90_' + location.pathname;
    let yaFue = false;
    try { yaFue = sessionStorage.getItem(clave) === '1'; } catch (_) { /* modo privado */ }
    if (yaFue) return;

    let pedido = false;
    function revisar() {
        if (pedido) return;
        pedido = true;
        requestAnimationFrame(() => {
            pedido = false;
            const alto = document.documentElement.scrollHeight - window.innerHeight;
            if (alto <= 0) return;
            if ((window.scrollY / alto) < 0.9) return;
            window.removeEventListener('scroll', revisar);
            try { sessionStorage.setItem(clave, '1'); } catch (_) {}
            tnrEvento('scroll_90', { pagina: location.pathname });
        });
    }
    window.addEventListener('scroll', revisar, { passive: true });
})();

// ─────────────────────────────────────────────────────────────────────
// ANIMACIONES v3 (septiembre 2026)
// Todo con CSS + un poco de JS, sin librerias: el sitio sigue pesando
// lo mismo. Si el visitante pidio "reducir movimiento" en su sistema, lo
// que se mueve solo queda quieto.
// ─────────────────────────────────────────────────────────────────────
const tnrCalma = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const tnrPunteroFino = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

// Barra de progreso de lectura + navbar que se esconde al bajar + barra de
// CTA mobile que aparece cuando el boton del hero sale de pantalla.
(() => {
    const barra = document.querySelector('.scroll-progress');
    const nav = document.getElementById('navbar');
    const ctaMobile = document.querySelector('.mobile-cta');
    const ctaHero = document.querySelector('.h-ctas, .page-hero-ctas');
    let ultimoY = window.scrollY;
    let pedido = false;

    function actualizar() {
        pedido = false;
        const y = window.scrollY;
        const alto = document.documentElement.scrollHeight - window.innerHeight;
        if (barra && alto > 0) barra.style.transform = `scaleX(${Math.min(y / alto, 1)})`;

        if (nav && !document.body.classList.contains('menu-open')) {
            const bajando = y > ultimoY + 4;
            const subiendo = y < ultimoY - 4;
            if (bajando && y > 320) nav.classList.add('nav-oculta');
            else if (subiendo || y < 80) nav.classList.remove('nav-oculta');
        }
        ultimoY = y;

        if (ctaMobile) {
            const mostrar = ctaHero ? ctaHero.getBoundingClientRect().bottom < 0 : y > 240;
            ctaMobile.classList.toggle('visible', mostrar);
        }
    }
    window.addEventListener('scroll', () => {
        if (!pedido) { pedido = true; requestAnimationFrame(actualizar); }
    }, { passive: true });
    actualizar();
})();

// Contadores del hero: arrancan solos al cargar (estan a la vista).
(() => {
    const nums = document.querySelectorAll('.h-proof .count');
    if (!nums.length || tnrCalma) return;
    nums.forEach(el => { el.dataset.final = el.textContent; el.textContent = '0'; });
    setTimeout(() => nums.forEach(animateCounter), 700);
})();

// Celular del hero: va pasando por sitios reales que hicimos. Las capturas
// 2 y 3 se piden recien despues del load, para no competir con lo que
// importa en la primera carga.
(() => {
    const pantalla = document.getElementById('phoneScreen');
    if (!pantalla) return;
    const imgs = [...pantalla.querySelectorAll('img')];
    const nombre = document.getElementById('phoneName');
    let i = 0;
    imgs[0].classList.add('on');

    window.addEventListener('load', () => {
        imgs.forEach(img => { if (img.dataset.src) img.src = img.dataset.src; });
        if (tnrCalma || imgs.length < 2) return;
        setInterval(() => {
            if (document.hidden) return;
            const actual = imgs[i];
            i = (i + 1) % imgs.length;
            const sig = imgs[i];
            if (!sig.complete) { i = (i - 1 + imgs.length) % imgs.length; return; }
            actual.classList.remove('on'); actual.classList.add('off');
            sig.classList.remove('off'); sig.classList.add('on');
            setTimeout(() => actual.classList.remove('off'), 900);
            if (nombre) nombre.textContent = sig.dataset.name || '';
        }, 3200);
    });
})();

// Poster del video: se carga despues del load (antes pesaba 44 KB en la
// primera carga para un video que casi nadie reproduce enseguida).
window.addEventListener('load', () => {
    document.querySelectorAll('video[data-poster]').forEach(v => { v.poster = v.dataset.poster; });
});

// Pestañas de servicios. Sin JS se ven los tres paneles, uno abajo del otro.
(() => {
    const tabs = [...document.querySelectorAll('.tabs [role="tab"]')];
    if (!tabs.length) return;
    function elegir(tab, foco) {
        tabs.forEach(t => {
            const activo = t === tab;
            t.setAttribute('aria-selected', activo ? 'true' : 'false');
            t.tabIndex = activo ? 0 : -1;
            const panel = document.getElementById(t.getAttribute('aria-controls'));
            if (!panel) return;
            panel.hidden = !activo;
            if (activo) { panel.classList.remove('entra'); void panel.offsetWidth; panel.classList.add('entra'); }
        });
        if (foco) tab.focus();
    }
    tabs.forEach((t, n) => {
        t.addEventListener('click', () => elegir(t));
        t.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') elegir(tabs[(n + 1) % tabs.length], true);
            if (e.key === 'ArrowLeft') elegir(tabs[(n - 1 + tabs.length) % tabs.length], true);
        });
    });
    elegir(tabs.find(t => t.getAttribute('aria-selected') === 'true') || tabs[0]);
})();

// Carril de trabajos: flechas en escritorio y arrastrar con el mouse.
(() => {
    const rail = document.getElementById('rail');
    if (!rail) return;
    document.querySelectorAll('[data-rail]').forEach(b => b.addEventListener('click', () => {
        const card = rail.querySelector('.w-card');
        const paso = card ? card.getBoundingClientRect().width + 14 : 320;
        rail.scrollBy({ left: paso * Number(b.dataset.rail), behavior: 'smooth' });
    }));
    if (!tnrPunteroFino) return;
    let x0 = 0, s0 = 0, arrastrando = false, movio = false;
    rail.addEventListener('pointerdown', (e) => {
        if (e.pointerType !== 'mouse' || e.target.closest('a, button, summary')) return;
        arrastrando = true; movio = false; x0 = e.clientX; s0 = rail.scrollLeft;
        rail.classList.add('dragging');
    });
    window.addEventListener('pointermove', (e) => {
        if (!arrastrando) return;
        const dx = e.clientX - x0;
        if (Math.abs(dx) > 4) movio = true;
        rail.scrollLeft = s0 - dx;
    });
    window.addEventListener('pointerup', () => {
        if (!arrastrando) return;
        arrastrando = false; rail.classList.remove('dragging');
    });
    rail.addEventListener('click', (e) => { if (movio) { e.preventDefault(); movio = false; } }, true);
})();

// Botones "magneticos" y tarjetas que se inclinan hacia el mouse.
// Solo con mouse: en el celular no hay hover y seria ruido.
(() => {
    if (!tnrPunteroFino || tnrCalma) return;
    document.querySelectorAll('.btn-primary, .btn-sun, .nav-cta, .rail-btn').forEach(b => {
        b.addEventListener('mousemove', (e) => {
            const r = b.getBoundingClientRect();
            const dx = (e.clientX - r.left - r.width / 2) * 0.18;
            const dy = (e.clientY - r.top - r.height / 2) * 0.28;
            b.style.transform = `translate(${dx}px, ${dy}px)`;
        });
        b.addEventListener('mouseleave', () => { b.style.transform = ''; });
    });
    document.querySelectorAll('.w-card, .trabajo-card, .app-card, .team-card').forEach(c => {
        c.addEventListener('mousemove', (e) => {
            const r = c.getBoundingClientRect();
            const px = (e.clientX - r.left) / r.width - 0.5;
            const py = (e.clientY - r.top) / r.height - 0.5;
            c.style.transform = `perspective(900px) rotateY(${px * 6}deg) rotateX(${-py * 6}deg) translateY(-6px)`;
        });
        c.addEventListener('mouseleave', () => { c.style.transform = ''; });
    });
})();
