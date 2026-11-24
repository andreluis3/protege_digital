from io import BytesIO

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, FileResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

from core.course_data import MODULES
from core.models import CourseLessonProgress
from .models import QuizAttempt
from .questions import QUESTIONS, PASSING_SCORE


def _course_is_complete(user):
    required_modules = [m for m in MODULES if not m.get("final")]
    for module in required_modules:
        total_lessons = len(module.get("lessons", []))
        completed = CourseLessonProgress.objects.filter(
            user=user, module_number=module["number"], completed=True
        ).count()
        if total_lessons == 0 or completed < total_lessons:
            return False
    return True


@login_required
def quiz_index(request):
    if not _course_is_complete(request.user):
        messages.warning(request, "Conclua as aulas dos módulos 01 a 06 para liberar o Desafio Final.")
        return redirect("core:curso")

    if request.method == "POST":
        answers = {question["id"]: request.POST.get(question["id"], "") for question in QUESTIONS}
        unanswered = [q for q in QUESTIONS if answers[q["id"]] not in {option[0] for option in q["options"]}]
        if unanswered:
            messages.error(request, "Responda às 10 questões antes de finalizar a avaliação.")
            return render(request, "quiz/index.html", {"questions": QUESTIONS})

        score = sum(1 for q in QUESTIONS if answers[q["id"]] == q["answer"])
        passed = score >= PASSING_SCORE
        attempt = QuizAttempt.objects.create(
            user=request.user, score=score, total_questions=len(QUESTIONS), passed=passed
        )
        return render(request, "quiz/result.html", {
            "attempt": attempt, "passing_score": PASSING_SCORE,
            "questions_count": len(QUESTIONS),
        })

    return render(request, "quiz/index.html", {"questions": QUESTIONS})


@login_required
def certificate_pdf(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, certificate_code=attempt_id, user=request.user, passed=True)
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=landscape(A4), rightMargin=22*mm, leftMargin=22*mm,
        topMargin=20*mm, bottomMargin=20*mm,
        title="Certificado Protege Digital", author="Protege Digital",
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle("CertificateTitle", parent=styles["Title"], fontName="Helvetica-Bold",
                           fontSize=28, leading=34, alignment=TA_CENTER, textColor=colors.HexColor("#174ea6"), spaceAfter=12)
    body = ParagraphStyle("CertificateBody", parent=styles["BodyText"], fontName="Helvetica",
                          fontSize=15, leading=24, alignment=TA_CENTER, textColor=colors.HexColor("#263238"))
    name_style = ParagraphStyle("StudentName", parent=body, fontName="Helvetica-Bold", fontSize=22, leading=28, textColor=colors.HexColor("#111827"))
    small = ParagraphStyle("CertificateSmall", parent=body, fontSize=9, leading=14, textColor=colors.HexColor("#64748b"))
    student_name = request.user.get_full_name() or request.user.email or request.user.get_username()
    date_text = timezone.localtime(attempt.created_at).strftime("%d/%m/%Y")
    story = [
        Spacer(1, 8*mm),
        Paragraph("PROTEGE DIGITAL", title),
        HRFlowable(width="72%", thickness=2, color=colors.HexColor("#3b82f6"), hAlign="CENTER", spaceBefore=4, spaceAfter=18),
        Paragraph("CERTIFICADO DE CONCLUSÃO", ParagraphStyle("SubTitle", parent=title, fontSize=17, leading=22, textColor=colors.HexColor("#334155"))),
        Spacer(1, 5*mm),
        Paragraph("Olá! Certificamos que", body),
        Spacer(1, 3*mm),
        Paragraph(student_name.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"), name_style),
        Spacer(1, 3*mm),
        Paragraph("concluiu o curso Protege Digital, realizando a avaliação final com aproveitamento.", body),
        Spacer(1, 4*mm),
        Paragraph(f"Resultado: <b>{attempt.score} de {attempt.total_questions} questões</b> · Data: <b>{date_text}</b>", body),
        Spacer(1, 12*mm),
        HRFlowable(width="35%", thickness=0.8, color=colors.HexColor("#94a3b8"), hAlign="CENTER"),
        Paragraph("Protege Digital · Educação e conscientização em segurança digital", small),
        Paragraph(f"Código de validação: {attempt.certificate_code}", small),
    ]
    doc.build(story)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="certificado-protege-digital.pdf", content_type="application/pdf")
