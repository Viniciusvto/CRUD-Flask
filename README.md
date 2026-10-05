# CRUD Flask

API REST de tarefas feita com Flask, com uma página web para criar, listar, editar, concluir e apagar tarefas pelo navegador.

**Acesse online:** https://crud-flask-xzuf.onrender.com/tarefas

> Hospedado no plano gratuito do Render: se o serviço estiver inativo, o primeiro acesso pode levar cerca de 1 minuto.

## Funcionalidades

- API REST com as operações de CRUD (`POST`, `GET`, `PUT`, `DELETE`)
- Página `/tarefas` com formulário e botões que chamam a API via `fetch`
- Templates HTML renderizados com Jinja2
- Deploy no Render com Gunicorn

## Tecnologias

- Python 3
- Flask
- Gunicorn
- HTML, CSS e JavaScript

## Estrutura

```
.
├── meu_projeto/
│   ├── app.py              # aplicação Flask e rotas
│   └── templates/
│       ├── homepage.html   # página inicial
│       ├── tarefas.html    # interface do CRUD
│       └── usuarios.html   # página de boas-vindas ao usuário
├── Procfile                # comando de start em produção
└── requirements.txt        # dependências
```

## Como rodar localmente

```bash
# clonar o repositório
git clone git@github.com:Viniciusvto/CRUD-Flask.git
cd CRUD-Flask

# criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate        # no Windows: venv\Scripts\activate

# instalar as dependências
pip install -r requirements.txt

# iniciar o servidor
cd meu_projeto
python app.py
```

Acesse http://127.0.0.1:5000/tarefas no navegador.

## Rotas

### Páginas

| Rota | Descrição |
|------|-----------|
| `GET /` | Página inicial |
| `GET /tarefas` | Interface para gerenciar as tarefas |
| `GET /usuarios/<nome_usuario>` | Página de boas-vindas ao usuário |

### API

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/tasks` | Cria uma tarefa |
| `GET` | `/tasks` | Lista todas as tarefas |
| `GET` | `/tasks/<id>` | Busca uma tarefa pelo id |
| `PUT` | `/tasks/<id>` | Atualiza uma tarefa |
| `DELETE` | `/tasks/<id>` | Apaga uma tarefa |

#### Exemplos

Criar uma tarefa (`title` é obrigatório, `description` é opcional):

```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar Flask", "description": "Ler a documentação"}'
```

Resposta (`201`):

```json
{
  "message": "Task created successfully",
  "task": {
    "id": 1,
    "title": "Estudar Flask",
    "description": "Ler a documentação",
    "completed": false
  }
}
```

Marcar como concluída (só os campos enviados são alterados):

```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

Apagar:

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

## Deploy

O projeto está hospedado no [Render](https://render.com), com deploy automático a cada push na branch `main`. Configuração do serviço:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn --chdir meu_projeto app:app`

## Limitações

As tarefas ficam armazenadas em memória, então são perdidas sempre que o servidor reinicia ou um novo deploy é feito. O próximo passo é usar um banco de dados.
