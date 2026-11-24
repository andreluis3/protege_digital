"""Banco de questões elaborado a partir dos temas previstos no roteiro do Protege Digital."""

QUESTIONS = [
    {
        "id": "q1",
        "text": "Qual é o principal objetivo da segurança digital no uso cotidiano da tecnologia?",
        "options": [
            ("a", "Proteger informações, contas e dispositivos contra riscos digitais."),
            ("b", "Impedir qualquer pessoa de utilizar a internet."),
            ("c", "Deixar todos os arquivos públicos para facilitar o acesso."),
            ("d", "Eliminar a necessidade de atualizar os dispositivos."),
        ],
        "answer": "a",
    },
    {
        "id": "q2",
        "text": "Você recebe uma mensagem inesperada dizendo que sua conta será bloqueada e pedindo para clicar imediatamente em um link. O que deve fazer?",
        "options": [
            ("a", "Clicar rapidamente para evitar o bloqueio."),
            ("b", "Encaminhar a mensagem para todos os contatos."),
            ("c", "Não clicar e verificar a informação diretamente no canal oficial do serviço."),
            ("d", "Responder a mensagem informando sua senha."),
        ],
        "answer": "c",
    },
    {
        "id": "q3",
        "text": "Qual situação é um sinal comum de tentativa de phishing?",
        "options": [
            ("a", "Uma atualização iniciada nas configurações do próprio aparelho."),
            ("b", "Uma mensagem suspeita que imita uma empresa e tenta obter dados por um link."),
            ("c", "Um aviso que você mesmo abriu dentro do aplicativo oficial."),
            ("d", "Uma conversa presencial com alguém conhecido."),
        ],
        "answer": "b",
    },
    {
        "id": "q4",
        "text": "Qual alternativa representa uma boa prática para criar senhas?",
        "options": [
            ("a", "Usar apenas o próprio nome e o ano de nascimento."),
            ("b", "Escolher uma senha curta e fácil de adivinhar."),
            ("c", "Repetir a mesma senha em todos os serviços."),
            ("d", "Criar uma senha longa, difícil de adivinhar e diferente para cada conta."),
        ],
        "answer": "d",
    },
    {
        "id": "q5",
        "text": "Por que não é recomendado reutilizar a mesma senha em vários serviços?",
        "options": [
            ("a", "Porque uma senha nunca pode ser digitada mais de uma vez."),
            ("b", "Porque o acesso a uma conta pode facilitar o acesso a outras contas que usam a mesma senha."),
            ("c", "Porque senhas diferentes deixam a internet mais lenta."),
            ("d", "Porque todos os serviços compartilham obrigatoriamente suas senhas."),
        ],
        "answer": "b",
    },
    {
        "id": "q6",
        "text": "Qual atitude ajuda a manter celulares e computadores mais protegidos?",
        "options": [
            ("a", "Manter o sistema e os aplicativos atualizados."),
            ("b", "Desativar todas as atualizações de segurança."),
            ("c", "Instalar aplicativos de qualquer site desconhecido."),
            ("d", "Ignorar alertas de segurança do dispositivo."),
        ],
        "answer": "a",
    },
    {
        "id": "q7",
        "text": "Ao instalar um aplicativo, o que é mais seguro fazer quando ele solicita permissões?",
        "options": [
            ("a", "Aceitar todas as permissões sem ler."),
            ("b", "Conceder acesso a todos os dados, mesmo sem necessidade."),
            ("c", "Verificar se cada permissão é necessária para a função do aplicativo."),
            ("d", "Compartilhar a senha do aparelho com o desenvolvedor."),
        ],
        "answer": "c",
    },
    {
        "id": "q8",
        "text": "Qual comportamento contribui para a privacidade e a proteção de dados pessoais?",
        "options": [
            ("a", "Publicar documentos pessoais em redes sociais abertas."),
            ("b", "Compartilhar endereço e documentos com qualquer pessoa que solicitar."),
            ("c", "Deixar dados pessoais visíveis em todos os perfis."),
            ("d", "Compartilhar apenas os dados necessários e revisar as configurações de privacidade."),
        ],
        "answer": "d",
    },
    {
        "id": "q9",
        "text": "Ao navegar na internet, você encontra um site desconhecido oferecendo um prêmio e solicitando seus dados pessoais. Qual é a melhor atitude?",
        "options": [
            ("a", "Preencher tudo para garantir o prêmio."),
            ("b", "Desconfiar da oferta e verificar a legitimidade do site antes de fornecer qualquer dado."),
            ("c", "Informar também a senha do seu e-mail."),
            ("d", "Baixar qualquer arquivo indicado pelo site."),
        ],
        "answer": "b",
    },
    {
        "id": "q10",
        "text": "O cadeado/HTTPS no endereço de um site garante, sozinho, que ele é legítimo e confiável?",
        "options": [
            ("a", "Sim, todo site com HTTPS é necessariamente verdadeiro."),
            ("b", "Sim, ele garante que a oferta e o conteúdo do site não são golpes."),
            ("c", "Não. HTTPS protege a conexão, mas ainda é necessário conferir o endereço e a legitimidade do site."),
            ("d", "Não, porque HTTPS significa que a conexão está sempre desprotegida."),
        ],
        "answer": "c",
    },
]

PASSING_SCORE = 8  # Acima de 7 acertos em 10 questões.
