import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
from core.models import validate_youtube_url


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("slug", models.SlugField(unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ("title",)},
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ("is_active", models.BooleanField(default=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="modules", to="core.course")),
            ],
            options={"ordering": ("order",), "indexes": [models.Index(fields=["course", "is_active", "order"], name="core_module_course__idx")], "constraints": [models.UniqueConstraint(fields=("course", "order"), name="unique_module_order_per_course")]},
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ("video_url", models.URLField(blank=True, validators=[validate_youtube_url])),
                ("pdf", models.FileField(blank=True, upload_to="lesson_pdfs/")),
                ("duration_minutes", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="lessons", to="core.module")),
            ],
            options={"ordering": ("order",), "indexes": [models.Index(fields=["module", "is_active", "order"], name="core_lesson_module__idx")], "constraints": [models.UniqueConstraint(fields=("module", "order"), name="unique_lesson_order_per_module")]},
        ),
        migrations.CreateModel(
            name="LessonProgress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("completed", models.BooleanField(default=False)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="progress_records", to="core.lesson")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="lesson_progress", to=settings.AUTH_USER_MODEL)),
            ],
            options={"indexes": [models.Index(fields=["user", "completed"], name="core_lesson_user_id_9_idx")], "constraints": [models.UniqueConstraint(fields=("user", "lesson"), name="unique_progress_per_user_lesson")]},
        ),
        migrations.CreateModel(
            name="CourseLessonProgress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("module_number", models.PositiveSmallIntegerField()),
                ("lesson_number", models.PositiveSmallIntegerField(default=1)),
                ("started_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("completed", models.BooleanField(default=False)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="course_lesson_progress", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ("module_number", "lesson_number"), "constraints": [models.UniqueConstraint(fields=("user", "module_number", "lesson_number"), name="unique_course_lesson_progress")]},
        ),
    ]
