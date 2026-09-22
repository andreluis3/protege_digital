window.addEventListener("DOMContentLoaded", function () {
    const navToggle = document.querySelector("[data-nav-toggle]");
    const navPanel = document.querySelector("[data-nav-panel]");

    if (navToggle && navPanel) {
        navToggle.addEventListener("click", function () {
            const isOpen = navPanel.classList.toggle("is-open");
            navToggle.setAttribute("aria-expanded", String(isOpen));
            navToggle.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
            document.body.classList.toggle("nav-open", isOpen);
        });

        navPanel.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", function () {
                navPanel.classList.remove("is-open");
                navToggle.setAttribute("aria-expanded", "false");
                navToggle.setAttribute("aria-label", "Abrir menu");
                document.body.classList.remove("nav-open");
            });
        });

        window.addEventListener("resize", function () {
            if (window.innerWidth >= 980) {
                navPanel.classList.remove("is-open");
                navToggle.setAttribute("aria-expanded", "false");
                document.body.classList.remove("nav-open");
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-progress]").forEach((element) => {
        const progress = Number(element.dataset.progress);

        if (!Number.isNaN(progress)) {
            element.style.width = `${progress}%`;
        }
    });
});
