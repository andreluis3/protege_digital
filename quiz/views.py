from django.shortcuts import render


def quiz_placeholder(request):
    return render(request, "quiz/index.html")
