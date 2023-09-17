FROM python:3.8

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install --no-dev

COPY . /app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "6666"]