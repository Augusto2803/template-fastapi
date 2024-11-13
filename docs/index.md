# Projeto Modelo FastAPI

Este projeto fornece uma base sólida para construir APIs escaláveis e de alto desempenho usando FastAPI. Ele integra ferramentas e bibliotecas essenciais para agilizar o desenvolvimento e garantir a qualidade do código.

## Funcionalidades

- **FastAPI**: Framework web moderno e rápido para construir APIs com Python 3.12.
- **Poetry**: Ferramenta de gerenciamento de dependências e empacotamento.
- **SQLAlchemy**: ORM poderoso para interações com banco de dados.
- **Alembic**: Migrações de banco de dados para gerenciar mudanças de esquema.
- **Configurações Pydantic**: Gerenciamento simplificado de configurações.
- **Hash de Senhas**: Manipulação segura de senhas com `pwdlib` e Argon2.
- **Taskipy**: Executor de tarefas para automatizar fluxos de trabalho.
- **Ruff**: Linter rápido e formatador de código.

## Instruções de Configuração

### Pré-requisitos

- Python 3.12
- [Poetry](https://python-poetry.org/)

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Augusto2803/template-fastapi.git
    cd template-fastapi
    ```

2. Instale as dependências:

    ```bash
    poetry install
    ```

### Migrações de Banco de Dados

Aplique migrações para configurar o esquema do banco de dados:

```bash
poetry run makemigrations "Migração inicial"
poetry run migrate
```

## Executando a Aplicação

Inicie o servidor de desenvolvimento:

```bash
poetry run uvicorn template_fastapi.main:app --reload
```

Acesse a API em `http://localhost:8000`.

## Qualidade do Código

- **Linting**: Verifique o código com Ruff.

  ```bash
  poetry run task lint
  ```

- **Formatação**: Formate o código com Ruff.

  ```bash
  poetry run task format
  ```
