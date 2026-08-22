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
// threshold 0 (no 0.1): un bloque de texto largo puede medir varios miles de px,
// y entonces el 10% de su alto nunca entra en pantalla y nunca se revelaba.
// Con 0 + rootMargin, se revela apenas su borde superior cruza el pliegue.
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// COUNTER ANIMATION
function animateCounter(el) {
    const target = parseInt(el.dataset.target);
    const duration = 1600;
    const start = performance.now();
    const update = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target);
        if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
}

const statsEl = document.querySelector('.stats');

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
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const inputs = contactForm.querySelectorAll('input, select, textarea');
        const nombre = inputs[0].value || '';
        const negocio = inputs[1].value || '';
        const tel = inputs[2].value || '';
        const servicio = inputs[3].value || '';
        const msg = inputs[4].value || '';

        const text = [
            `Hola! Soy ${nombre}${negocio ? ' de ' + negocio : ''}.`,
            `Quiero información sobre: ${servicio}.`,
            tel ? `Mi WhatsApp: ${tel}.` : '',
            msg ? msg : ''
        ].filter(Boolean).join(' ');

        window.open(`https://wa.me/5491150089069?text=${encodeURIComponent(text)}`, '_blank');
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

// VIDEO DE FONDO DEL HERO
// El <source> se inyecta desde acá y no en el HTML: así el navegador no baja
// medio mega en un celular, donde el video ni se muestra.
(() => {
    const video = document.getElementById('heroVideo');
    if (!video) return;

    const quiereMenosMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const pantallaChica = window.matchMedia('(max-width: 768px)').matches;
    // Si el usuario está con datos limitados o ahorro de datos, no lo cargamos
    const con = navigator.connection || {};
    const conexionPobre = con.saveData === true || /^([23]g|slow-2g)$/.test(con.effectiveType || '');

    if (quiereMenosMovimiento || pantallaChica || conexionPobre) return;

    [['/videos/hero-web.webm', 'video/webm'], ['/videos/hero-web.mp4', 'video/mp4']]
        .forEach(([src, type]) => {
            const s = document.createElement('source');
            s.src = src;
            s.type = type;
            video.appendChild(s);
        });

    video.load();
    video.play().catch(() => { /* si el navegador lo bloquea, queda el poster */ });
})();
