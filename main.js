// NAVBAR SCROLL
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });

// MOBILE NAV
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
let menuOpen = false;

function setMenu(open) {
    menuOpen = open;
    navMenu.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
    const [s1, s2, s3] = navToggle.querySelectorAll('span');
    if (open) {
        s1.style.transform = 'rotate(45deg) translate(5px, 5px)';
        s2.style.opacity = '0';
        s3.style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
        s1.style.transform = s2.style.opacity = s3.style.transform = '';
        s2.style.opacity = '';
    }
}

navToggle.addEventListener('click', () => setMenu(!menuOpen));
navMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));

// SCROLL REVEAL
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

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
if (statsEl) {
    new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            document.querySelectorAll('.stat-number').forEach(animateCounter);
            entries[0].target._obs.disconnect();
        }
    }, { threshold: 0.5 }).observe(statsEl);
    statsEl._obs = statsEl._obs || new IntersectionObserver(() => {});
}

// Better counter observer
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
