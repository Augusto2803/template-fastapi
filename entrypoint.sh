#!/bin/bash

echo "Rodando as migrações..."
python -m alembic upgrade head || echo "Falha ao rodar migrações!"
echo "Migrações rodadas com sucesso!"

echo "Iniciando o servidor..."
exec uvicorn template_fastapi.main:app --host 0.0.0.0 --port 8000