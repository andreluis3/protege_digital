MODULES = [
    {
        "number": 1,
        "title": "Fundamentos da Segurança Digital",
        "description": "Aprenda os conceitos básicos para começar a se proteger no mundo digital.",
        "icon": "assets/resources/icons/shield_logo.png",
        "lessons": [{
            "title": "O que é segurança digital",
            "summary": "Nesta aula, você vai conhecer o conceito de segurança digital e entender por que proteger seus dados, dispositivos e informações pessoais é tão importante no dia a dia.",
            "video": "https://www.youtube-nocookie.com/embed/w1GcXrDLR-A?start=9&rel=0&modestbranding=1",
            "pdf": "",
        }],
    },
    {
        "number": 2,
        "title": "Golpes, Phishing e Engenharia Social",
        "description": "Aprenda a identificar golpes, mensagens falsas e tentativas de manipulação.",
        "icon": "assets/resources/icons/cyber-criminal.png",
        "lessons": [{
            "title": "Golpes digitais e phishing",
            "summary": "Nesta aula, você vai aprender a reconhecer golpes digitais, identificar tentativas de phishing e observar sinais de alerta em mensagens, links e páginas suspeitas.",
            "video": "https://www.youtube-nocookie.com/embed/k1nSZCidlks?start=2&rel=0&modestbranding=1",
            "pdf": "",
        }],
    },
    {
        "number": 3,
        "title": "Senhas e Proteção de Contas",
        "description": "Aprenda a criar senhas mais seguras e proteger suas contas.",
        "icon": "assets/resources/icons/password.png",
        "lessons": [{
            "title": "A importância de ter boas senhas",
            "summary": "Nesta aula, vamos entender por que utilizar senhas fortes e seguras é fundamental para proteger nossas informações pessoais e evitar acessos não autorizados. Você aprenderá boas práticas para criar senhas difíceis de descobrir, evitar combinações previsíveis e não reutilizar a mesma senha em diferentes plataformas.",
            "video": "https://www.youtube-nocookie.com/embed/RLLzeWv-wOA?rel=0&modestbranding=1",
            "pdf": "",
        }],
    },
    {
        "number": 4,
        "title": "Segurança no Celular e Computador",
        "description": "Conheça práticas para manter seus dispositivos protegidos.",
        "icon": "assets/resources/icons/cellphone1.png",
        "lessons": [{
            "title": "Dispositivos Seguros",
            "summary": "Nesta aula, você vai aprender cuidados importantes para proteger seu celular e computador, identificar aplicativos suspeitos, realizar downloads seguros e manter seus dispositivos atualizados.",
            "video": "https://www.youtube-nocookie.com/embed/IGyIn0N9jT4?rel=0&modestbranding=1",
            "pdf": "",
        }],
    },
    {
        "number": 5,
        "title": "Privacidade e Proteção de Dados",
        "description": "Aprenda a proteger suas contas e aumentar sua segurança digital.",
        "icon": "assets/resources/icons/protected.png",
        "lessons": [{
            "title": "Autenticação em Duas Etapas",
            "summary": "Nesta aula, você vai entender como funciona a verificação em duas etapas, por que ela é importante e como utilizar esse recurso para adicionar uma camada extra de proteção às suas contas digitais.",
            "video": "https://www.youtube-nocookie.com/embed/Cm1N2rIGm8Q?rel=0&modestbranding=1",
            "pdf": "",
        }],
    },
    {
        "number": 6,
        "title": "Navegação Segura",
        "description": "Aprenda a navegar pela internet de forma mais consciente e segura.",
        "icon": "assets/resources/icons/websecurity.png",
        "lessons": [{
            "title": "Navegação Segura na Internet",
            "summary": "Nesta aula, você vai aprender a identificar sites suspeitos, reconhecer links maliciosos e tomar cuidados ao utilizar redes Wi-Fi públicas, tornando sua navegação na internet mais segura.",
            "video": "https://www.youtube-nocookie.com/embed/45SjnaQjvXw?rel=0&modestbranding=1",
            "pdf": "",
        }],
    },
    {
        "number": 7,
        "title": "Desafio Final",
        "description": "Avaliação final para revisar os conhecimentos do curso.",
        "icon": "assets/resources/icons/protected.png",
        "final": True,
        "lessons": [],
    },
]


def get_module(number):
    return next(
        (module for module in MODULES if module["number"] == number),
        None
    )
