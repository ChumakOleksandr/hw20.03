# базовий образ
# версія пайтона

FROM python:3.11-slim

# базова директорія(папка)
WORKDIR app

# скопіювати файли в образ
# скопіювати все
COPY ./ ./

# встановлення бібліотек
RUN pip install -r requirements.txt

# відкрити порт
EXPOSE 8080

# команда при запуску
CMD ["python3", "main.py"]
