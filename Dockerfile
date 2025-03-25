FROM python:3.12.5-slim-bookworm

ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt update && apt install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
