FROM python:3.12-slim

ENV POETRY_VIRTUALENVS_CREATE=false
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry config installer.max-workers 10 \
    && poetry install --no-interaction --no-ansi --only main

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["/app/entrypoint.sh"]