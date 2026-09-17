from django.shortcuts import render


COURSE_MODULES = [
    {
        "number": "01",
        "icon": "🛡️",
        "title": "Fundamentos da Segurança Digital",
        "description": "Aprenda os conceitos básicos para começar a se proteger no mundo digital.",
        "lessons": 3,
        "progress": 60,
        "status": "in-progress",
        "status_label": "Em andamento",
    },
    {
        "number": "02",
        "icon": "🎣",
        "title": "Golpes, Phishing e Engenharia Social",
        "description": "Aprenda a identificar golpes, mensagens falsas e tentativas de manipulação.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "03",
        "icon": "🔐",
        "title": "Senhas e Proteção de Contas",
        "description": "Aprenda a criar senhas mais seguras e proteger suas contas.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "04",
        "icon": "📱",
        "title": "Segurança no Celular e Computador",
        "description": "Conheça práticas para manter seus dispositivos protegidos.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "05",
        "icon": "👤",
        "title": "Privacidade e Proteção de Dados",
        "description": "Entenda como cuidar melhor das suas informações pessoais.",
        "lessons": 3,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "06",
        "icon": "🌐",
        "title": "Navegação Segura",
        "description": "Aprenda a navegar pela internet de forma mais consciente e segura.",
        "lessons": 3,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "07",
        "icon": "🏆",
        "title": "Desafio Final",
        "description": "Teste seus conhecimentos e coloque em prática o que aprendeu.",
        "lessons": 1,
        "progress": 0,
        "status": "locked",
        "status_label": "Bloqueado",
    },
]


def home(request):
    return render(request, "core/home.html")


def sobre(request):
    return render(request, "core/sobre.html")


def curso(request):
    return render(
        request,
        "core/curso.html",
        {
            "modules": COURSE_MODULES,
            "current_module": COURSE_MODULES[0],
        },
    )
