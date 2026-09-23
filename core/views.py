from django.shortcuts import render


# =============================================================
# DADOS DO CURSO
# =============================================================
#
# Nesta etapa os módulos ainda são dados estáticos (sem model
# no banco). O formato já foi pensado para migrar depois para um
# app "learning" com models (Modulo, Aula, Progresso, Certificado)
# sem precisar mudar os templates: cada módulo carrega um "slug"
# (para futuras URLs de aula, ex: /curso/fundamentos-da-seguranca/)
# e um "next_lesson" (para a próxima aula sugerida na retomada).
# =============================================================

COURSE_MODULES = [
    {
        "number": "01",
        "slug": "fundamentos-da-seguranca-digital",
        "icon": "assets/resources/icons/shield_logo.png",
        "title": "Fundamentos da Segurança Digital",
        "description": "Aprenda os conceitos básicos para começar a se proteger no mundo digital.",
        "lessons": 3,
        "progress": 60,
        "status": "in-progress",
        "status_label": "Em andamento",
        # Aula sugerida ao retomar o curso (usada no "continue-card").
        # Quando existir um model de Aula, isso vira uma FK/consulta real.
        "next_lesson": {
            "number": 2,
            "title": "Por que a segurança digital é importante?",
        },
    },
    {
        "number": "02",
        "slug": "golpes-phishing-e-engenharia-social",
        "icon": "assets/resources/icons/cyber-criminal.png",
        "title": "Golpes, Phishing e Engenharia Social",
        "description": "Aprenda a identificar golpes, mensagens falsas e tentativas de manipulação.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
        "next_lesson": None,
    },
    {
        "number": "03",
        "slug": "senhas-e-protecao-de-contas",
        "icon": "assets/resources/icons/password.png",
        "title": "Senhas e Proteção de Contas",
        "description": "Aprenda a criar senhas mais seguras e proteger suas contas.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
        "next_lesson": None,
    },
    {
        "number": "04",
        "slug": "seguranca-no-celular-e-computador",
        "icon": "assets/resources/icons/cellphone1.png",
        "title": "Segurança no Celular e Computador",
        "description": "Conheça práticas para manter seus dispositivos protegidos.",
        "lessons": 4,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
        "next_lesson": None,
    },
    {
        "number": "05",
        "slug": "privacidade-e-protecao-de-dados",
        "icon": "assets/resources/icons/protected.png",
        "title": "Privacidade e Proteção de Dados",
        "description": "Entenda como cuidar melhor das suas informações pessoais.",
        "lessons": 3,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
        "next_lesson": None,
    },
    {
        "number": "06",
        "slug": "navegacao-segura",
        "icon": "assets/resources/icons/websecurity.png",
        "title": "Navegação Segura",
        "description": "Aprenda a navegar pela internet de forma mais consciente e segura.",
        "lessons": 3,
        "progress": 0,
        "status": "not-started",
        "status_label": "Não iniciado",
        "next_lesson": None,
    },
    {
        "number": "07",
        "slug": "desafio-final",
        "icon": "assets/resources/icons/award.png",
        "title": "Desafio Final",
        "description": "Teste seus conhecimentos e coloque em prática o que aprendeu.",
        "lessons": 1,
        "progress": 0,
        "status": "locked",
        "status_label": "Bloqueado",
        "next_lesson": None,
    },
]


def _with_computed_fields(modules):
    """
    Preenche campos derivados que os templates usam, para não
    duplicar essa conta em cada componente (aulas concluídas a
    partir do progresso, por exemplo). Fonte única da verdade
    continua sendo "progress".
    """
    enriched = []
    for module in modules:
        module = dict(module)
        module["completed_lessons"] = round(
            module["progress"] / 100 * module["lessons"]
        )
        enriched.append(module)
    return enriched


def _course_stats(modules):
    total_modules = len(modules)
    total_lessons = sum(module["lessons"] for module in modules)
    in_progress = sum(1 for module in modules if module["status"] == "in-progress")
    completed = sum(1 for module in modules if module["status"] == "completed")
    return {
        "total_modules": total_modules,
        "total_lessons": total_lessons,
        "in_progress": in_progress,
        "completed": completed,
    }


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
    modules = _with_computed_fields(COURSE_MODULES)
    current_module = modules[0]

    return render(
        request,
        "core/curso.html",
        {
            "modules": modules,
            "current_module": current_module,
            "stats": _course_stats(modules),
        },
    )