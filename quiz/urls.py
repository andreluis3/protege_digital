from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.quiz_index, name="index"),
    path("certificado/<uuid:attempt_id>/", views.certificate_pdf, name="certificate"),
]
