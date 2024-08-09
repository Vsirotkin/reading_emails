# Используем официальный образ Python на основе Alpine
FROM python:3.11.9-alpine

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем pipenv
RUN pip install pipenv

# Копируем Pipfile и Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Устанавливаем зависимости
RUN pipenv install --system --deploy

# Устанавливаем redis-cli
RUN apk add --no-cache redis

# Копируем проект
COPY . /app/

# Открываем порт
EXPOSE 8000
