from django.urls import path

from . import views


app_name = "accounts"

urlpatterns = [
    path("login/", views.login_placeholder, name="login"),
    path("cadastro/", views.cadastro_placeholder, name="cadastro"),
]
