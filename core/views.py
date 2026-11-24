from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .course_data import MODULES, get_module
from .models import CourseLessonProgress


def _module_cards(user):
    cards = []
    for source in MODULES:
        module = dict(source)
        lessons = module.get("lessons", [])
        total = len(lessons)
        records = list(CourseLessonProgress.objects.filter(user=user, module_number=module["number"]))
        completed = sum(1 for record in records if record.completed)
        started = bool(records)
        module["lessons"] = total
        module["completed_lessons"] = completed
        module["progress"] = round(completed * 100 / total) if total else 0
        if module.get("final"):
            required_modules = [m for m in MODULES if not m.get("final")]
            ready = all(
                len(m.get("lessons", [])) > 0
                and CourseLessonProgress.objects.filter(
                    user=user, module_number=m["number"], completed=True
                ).count() >= len(m.get("lessons", []))
                for m in required_modules
            )
            module["status"] = "available" if ready else "locked"
            module["status_label"] = "Disponível" if ready else "Conclua as aulas"
        elif total and completed == total:
            module["status"] = "completed"
            module["status_label"] = "Concluído"
        elif started:
            module["status"] = "in-progress"
            module["status_label"] = "Em andamento"
        else:
            module["status"] = "not-started"
            module["status_label"] = "Não iniciado"
        module["next_lesson"] = next((i for i, lesson in enumerate(lessons, 1)
                                      if not any(r.lesson_number == i and r.completed for r in records)), 1 if total else None)
        cards.append(module)
    return cards


def _course_stats(modules):
    content_modules = [m for m in modules if not m.get("final")]
    return {
        "total_modules": len(modules),
        "total_lessons": sum(m["lessons"] for m in content_modules),
        "in_progress": sum(m["status"] == "in-progress" for m in content_modules),
        "completed": sum(m["status"] == "completed" for m in content_modules),
    }


def home(request):
    return render(request, "core/home.html", {"modules": MODULES})


def sobre(request):
    return render(request, "core/sobre.html")


@login_required
def curso(request):
    modules = _module_cards(request.user)
    content_modules = [m for m in modules if not m.get("final")]
    current_module = next((m for m in content_modules if m["status"] == "in-progress"), None)
    if current_module is None:
        current_module = next((m for m in content_modules if m["status"] != "completed"), content_modules[0])
    total_lessons = sum(m["lessons"] for m in content_modules)
    completed_lessons = sum(m["completed_lessons"] for m in content_modules)
    overall_progress = round(completed_lessons * 100 / total_lessons) if total_lessons else 0
    return render(request, "core/curso.html", {
        "modules": modules,
        "current_module": current_module,
        "stats": _course_stats(modules),
        "overall_progress": overall_progress,
        "completed_lessons": completed_lessons,
        "display_name": request.user.get_full_name() or request.user.email or request.user.get_username(),
    })


@login_required
def player(request, module_number, lesson_number=1):
    module = get_module(module_number)
    if not module or module.get("final"):
        raise Http404
    lessons = module["lessons"]
    if not 1 <= lesson_number <= len(lessons):
        raise Http404

    progress, _ = CourseLessonProgress.objects.get_or_create(
        user=request.user,
        module_number=module_number,
        lesson_number=lesson_number,
    )
    if request.method == "POST" and request.POST.get("action") == "complete":
        if not progress.completed:
            progress.completed = True
            progress.completed_at = timezone.now()
            progress.save(update_fields=("completed", "completed_at", "updated_at"))
        return redirect("core:player", module_number=module_number, lesson_number=lesson_number)

    completed_count = CourseLessonProgress.objects.filter(
        user=request.user, module_number=module_number, completed=True
    ).count()
    return render(request, "core/player.html", {
        "module": module,
        "lessons": lessons,
        "lesson": lessons[lesson_number - 1],
        "lesson_number": lesson_number,
        "prev_number": lesson_number - 1 if lesson_number > 1 else None,
        "next_number": lesson_number + 1 if lesson_number < len(lessons) else None,
        "lesson_completed": progress.completed,
        "completed_count": completed_count,
    })
