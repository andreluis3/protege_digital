MODULES = [
    {"number": 1, "title": "Fundamentos da Segurança Digital", "lessons": [
        {"title": "O que é segurança digital", "summary": "Conceitos básicos e por que se proteger.", "video": "", "pdf": ""},
        {"title": "Principais ameaças online", "summary": "Os riscos mais comuns no dia a dia.", "video": "", "pdf": ""},
    ]},
    {"number": 2, "title": "Golpes, Phishing e Engenharia Social", "lessons": []},
    {"number": 3, "title": "Senhas e Proteção de Contas", "lessons": []},
    {"number": 4, "title": "Segurança no Celular e Computador", "lessons": []},
    {"number": 5, "title": "Privacidade e Proteção de Dados", "lessons": []},
    {"number": 6, "title": "Navegação Segura", "lessons": []},
    {"number": 7, "title": "Desafio Final", "final": True, "lessons": [],
     "description": "Avaliação de 10 questões valendo certificado."},
]


def get_module(number):
    return next((m for m in MODULES if m["number"] == number), None)