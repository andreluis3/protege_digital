document.addEventListener('DOMContentLoaded', function () {
    var frames = document.querySelectorAll('.threat-frame');

    if (!frames.length) {
        return;
    }

    // Sem suporte a IntersectionObserver: mostra tudo direto, sem animação
    if (!('IntersectionObserver' in window)) {
        frames.forEach(function (frame) {
            frame.classList.add('is-visible');
        });
        return;
    }

    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -40px 0px'
    });

    frames.forEach(function (frame, index) {
        frame.style.setProperty('--stagger', index);
        observer.observe(frame);
    });
});