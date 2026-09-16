(function () {
    const root = document.documentElement;
    const storageKey = "protege-digital-theme";

    function getPreferredTheme() {
        const savedTheme = localStorage.getItem(storageKey);

        if (savedTheme === "light" || savedTheme === "dark") {
            return savedTheme;
        }

        return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }

    function applyTheme(theme) {
        root.setAttribute("data-theme", theme);
        document.querySelectorAll("[data-theme-icon]").forEach((icon) => {
            icon.textContent = theme === "dark" ? "☀️" : "🌙";
        });
    }

    applyTheme(getPreferredTheme());

    window.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
            button.addEventListener("click", function () {
                const nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
                localStorage.setItem(storageKey, nextTheme);
                applyTheme(nextTheme);
            });
        });
    });
})();
