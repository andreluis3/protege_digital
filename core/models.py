from urllib.parse import parse_qs, urlparse

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


def validate_youtube_url(value):
    """Aceita somente URLs HTTPS de origens que o player pode incorporar."""
    if not value:
        return
    parsed = urlparse(value)
    allowed_hosts = {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}
    if parsed.scheme != "https" or parsed.hostname not in allowed_hosts:
        raise ValidationError("Informe uma URL HTTPS do YouTube.")


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("order",)
        constraints = [
            models.UniqueConstraint(fields=("course", "order"), name="unique_module_order_per_course"),
        ]
        indexes = [models.Index(fields=("course", "is_active", "order"))]

    def __str__(self):
        return f"{self.course.title} · {self.order}. {self.title}"


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    video_url = models.URLField(blank=True, validators=[validate_youtube_url])
    pdf = models.FileField(upload_to="lesson_pdfs/", blank=True)
    duration_minutes = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("order",)
        constraints = [
            models.UniqueConstraint(fields=("module", "order"), name="unique_lesson_order_per_module"),
        ]
        indexes = [models.Index(fields=("module", "is_active", "order"))]

    def __str__(self):
        return f"{self.module} · Aula {self.order}: {self.title}"

    @property
    def youtube_embed_url(self):
        """Converte formatos confiáveis do YouTube para a URL de incorporação."""
        if not self.video_url:
            return ""
        parsed = urlparse(self.video_url)
        if parsed.hostname == "youtu.be":
            video_id = parsed.path.strip("/").split("/")[0]
        elif parsed.path.startswith("/embed/"):
            video_id = parsed.path.split("/")[2] if len(parsed.path.split("/")) > 2 else ""
        else:
            video_id = parse_qs(parsed.query).get("v", [""])[0]
        return f"https://www.youtube.com/embed/{video_id}" if video_id else ""


class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lesson_progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="progress_records")
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("user", "lesson"), name="unique_progress_per_user_lesson"),
        ]
        indexes = [models.Index(fields=("user", "completed"))]

    def __str__(self):
        return f"{self.user} · {self.lesson}"

    def mark_completed(self):
        self.completed = True
        if not self.completed_at:
            self.completed_at = timezone.now()
        self.save(update_fields=("completed", "completed_at", "updated_at"))
