from django.contrib import admin

from .models import QuizAttempt


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "score", "total_questions", "passed", "created_at")
    list_filter = ("passed", "created_at")
    search_fields = ("user__username", "user__email", "certificate_code")
    readonly_fields = ("certificate_code", "created_at")
