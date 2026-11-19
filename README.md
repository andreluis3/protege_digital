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

## Como instalar e executar

Copie o arquivo de variáveis de exemplo e gere uma `SECRET_KEY` aleatória. O
arquivo `.env` não é versionado; para que o Django leia as variáveis sem
dependências extras, carregue-o no shell antes de executar os comandos.

```bash
cp .env.example .env
# Edite .env e substitua SECRET_KEY por uma chave aleatória longa.
set -a; source .env; set +a
```

No Windows PowerShell, defina as mesmas variáveis de `.env` na sessão antes de
executar os comandos abaixo.

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Windows

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
- `/curso/` - dashboard do curso (requer login)
- `/curso/modulo/<módulo>/aula/<aula>/` - player (requer login)
- `/login/` - entrada por e-mail e senha
- `/cadastro/` - criação de conta
- `/quiz/` - placeholder de avaliações

## Autenticação e segurança

- O projeto usa o `User` padrão do Django: o e-mail normalizado é usado como
  identificador (`username`) e as senhas são geradas com `create_user()`, que
  aplica hash seguro. Não há senha em texto puro no banco.
- Cadastro valida nome, e-mail único sem distinguir maiúsculas/minúsculas,
  confirmação e os validadores nativos de senha do Django.
- Login cria uma sessão Django e aceita apenas destinos internos em `next`.
  Logout é uma requisição `POST` protegida por CSRF.
- As páginas de curso e player exigem autenticação no backend.

## Produção

Defina `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS` (separados por vírgula) e,
quando aplicável, `CSRF_TRUSTED_ORIGINS`. SQLite é o padrão local. Para uma
futura migração, `DATABASE_URL` aceita URLs `postgres://` ou `postgresql://`
(com o driver PostgreSQL instalado no ambiente de deploy). Cookies seguros e
HTTPS são ativados quando `DEBUG=False`; use `SECURE_SSL_REDIRECT=False` apenas
se o HTTPS for tratado de forma incompatível pela infraestrutura.

## Administração e testes

Crie um administrador após aplicar as migrations:

```bash
python manage.py createsuperuser
```

Para validar o projeto:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py test
```

Progresso das aulas, recuperação de senha, quizzes funcionais, certificados e
uploads continuam fora do escopo desta etapa.
