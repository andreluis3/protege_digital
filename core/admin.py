from django.contrib import admin

from .models import Course, Lesson, LessonProgress, Module


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0
    fields = ("order", "title", "is_active")
    ordering = ("order",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "description", "slug")
    prepopulated_fields = {"slug": ("title",)}
    inlines = (ModuleInline,)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    fields = ("order", "title", "duration_minutes", "is_active")
    ordering = ("order",)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order", "is_active")
    list_filter = ("course", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")
    ordering = ("course", "order")
    inlines = (LessonInline,)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "order", "duration_minutes", "is_active")
    list_filter = ("module__course", "module", "is_active")
    list_editable = ("order", "duration_minutes", "is_active")
    search_fields = ("title", "description", "video_url")
    ordering = ("module__course", "module__order", "order")


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "completed", "completed_at", "updated_at")
    list_filter = ("completed", "lesson__module__course")
    search_fields = ("user__username", "user__email", "lesson__title")
    readonly_fields = ("updated_at",)
