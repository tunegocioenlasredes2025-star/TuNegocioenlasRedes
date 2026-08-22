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
