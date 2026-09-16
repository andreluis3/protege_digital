from django.shortcuts import render


def login_placeholder(request):
    return render(request, "accounts/login.html")


def cadastro_placeholder(request):
    return render(request, "accounts/cadastro.html")
