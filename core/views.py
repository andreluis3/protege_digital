from django.shortcuts import render


COURSE_MODULES = [
    {
        "number": "01",
        "icon": "assets/icons/shield_logo.png",
        "title": "Fundamentos da Segurança Digital",
        "description": "Aprenda os conceitos básicos para começar a se proteger no mundo digital.",
        "lessons": 3,
        "progress": 60,
        "status": "in-progress",
        "status_label": "Em andamento",
    },
    {
        "number": "02",
        "icon": "assets/resources/icons/cyber-criminal.png",
        "title": "Golpes, Phishing e Engenharia Social",
        "description": "Aprenda a identificar golpes, mensagens falsas e tentativas de manipulação.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "03",
        "icon": "assets/resources/icons/password.png",
        "title": "Senhas e Proteção de Contas",
        "description": "Aprenda a criar senhas mais seguras e proteger suas contas.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "04",
        "icon": "assets/resources/icons/cellphone1.png",
        "title": "Segurança no Celular e Computador",
        "description": "Conheça práticas para manter seus dispositivos protegidos.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "05",
        "icon": "assets/resources/icons/protected.png",
        "title": "Privacidade e Proteção de Dados",
        "description": "Entenda como cuidar melhor das suas informações pessoais.",
        "lessons": 3,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "06",
        "icon": "assets/resources/icons/websecurity.png",
        "title": "Navegação Segura",
        "description": "Aprenda a navegar pela internet de forma mais consciente e segura.",
        "lessons": 3,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
    },
    {
        "number": "07",
        "icon": "assets/resources/icons/award.png",
        "title": "Desafio Final",
        "description": "Teste seus conhecimentos e coloque em prática o que aprendeu.",
        "lessons": 1,
        "progress": 0,
        "status": "locked",
        "status_label": "Bloqueado",
    },
]


def home(request):
    return render(
        request,
        "core/home.html",
        {
            "modules": COURSE_MODULES,
        },
    )
    
    


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