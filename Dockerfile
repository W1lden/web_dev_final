# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Открываем порт и запускаем сервер
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
