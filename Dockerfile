FROM python:3.11

ARG OPENAI_API_KEY

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev

COPY . .

ENV OPENAI_API_KEY=${OPENAI_API_KEY}

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "6666"]