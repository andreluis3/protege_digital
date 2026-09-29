from django.http import Http404
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .course_data import get_module

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
        "number": 7,
        "title": "Desafio Final",
        "description": "Avaliação de 10 questões valendo certificado.",
        "icon": "assets/resources/icons/protected.png",
        "status": "locked",
        "status_label": "Em breve",
        "lessons": 0,
        "progress": 0,
        "slug": "desafio-final",
    }
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
    

def player(request, module_number, lesson_number=1):
    module = get_module(module_number)
    if not module or module.get("final"):
        raise Http404

    lessons = module["lessons"] or [{
        "title": "Aulas em breve",
        "summary": "As videoaulas deste módulo serão publicadas em breve.",
        "video": "",
        "pdf": "",
    }]

    if not 1 <= lesson_number <= len(lessons):
        raise Http404

    return render(request, "core/player.html", {
        "module": module,
        "lessons": lessons,
        "lesson": lessons[lesson_number - 1],
        "lesson_number": lesson_number,
        "prev_number": lesson_number - 1 if lesson_number > 1 else None,
        "next_number": lesson_number + 1 if lesson_number < len(lessons) else None,
    })