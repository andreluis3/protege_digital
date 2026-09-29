from django.urls import path

from . import views


app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("curso/", views.curso, name="curso"),
    path("curso/modulo/<int:module_number>/aula/<int:lesson_number>/", views.player, name="player"),
]
