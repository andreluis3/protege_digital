from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import LoginForm, RegistrationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:curso")

    next_url = _safe_next_url(request)
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(request, user)
            return redirect(next_url or settings.LOGIN_REDIRECT_URL)
        form.add_error(None, "E-mail ou senha inválidos.")

    return render(request, "accounts/login.html", {"form": form, "next": next_url})


def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect("core:curso")

    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        try:
            form.save()
        except ValidationError as error:
            form.add_error("email", error)
        else:
            messages.success(request, "Cadastro realizado. Entre com seu e-mail e senha.")
            return redirect("accounts:login")

    return render(request, "accounts/cadastro.html", {"form": form})


@login_required
@require_POST
def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect(settings.LOGOUT_REDIRECT_URL)


def _safe_next_url(request):
    next_url = request.POST.get("next") or request.GET.get("next")
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return next_url
    return ""
