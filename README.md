# Protege Digital

Protege Digital é uma plataforma educacional gratuita voltada à conscientização da comunidade sobre segurança digital.

O projeto faz parte de uma atividade de extensão universitária de Engenharia da Computação, relacionada ao ODS 10 - Redução das Desigualdades, com foco em inclusão digital e democratização do conhecimento sobre segurança da informação.

Nesta primeira versão, o repositório entrega uma base arquitetural Django organizada e uma Home/Landing Page responsiva com modo claro e escuro.

## Stack

- Python
- Django
- SQLite
- Django Templates
- HTML5
- CSS3
- JavaScript
- Google Fonts

## Arquitetura

```text
protege-digital/
├── accounts/          # autenticação, perfil e dados de usuário futuramente
├── backend/           # services, utils e integrações compartilhadas futuras
├── config/            # configurações globais do Django
├── core/              # páginas públicas e institucionais
├── frontend/          # templates globais e componentes reutilizáveis
├── quiz/              # perguntas, respostas, avaliações e resultados futuramente
├── static/            # CSS, JavaScript e imagens globais
├── media_cursos/      # vídeos, PDFs e capas de cursos futuramente
├── templates/         # templates globais adicionais
├── manage.py
└── requirements.txt
```

## Como instalar no Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Como instalar no Windows

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Como acessar

Depois de iniciar o servidor, acesse:

```text
http://127.0.0.1:8000/
```

## Páginas preparadas

- `/` - Home
- `/sobre/` - placeholder institucional
- `/curso/` - placeholder do curso
- `/login/` - placeholder de autenticação
- `/cadastro/` - placeholder de cadastro
- `/quiz/` - placeholder de avaliações

## Observações

Funcionalidades como login completo, cadastro, progresso, quizzes funcionais, uploads, certificados, APIs e painel customizado ainda não foram implementadas. A estrutura foi preparada para receber essas evoluções em etapas futuras.
