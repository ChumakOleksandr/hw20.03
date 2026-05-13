
FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./ ./

ENV HOST="0.0.0.0"
ENV PORT=8080

EXPOSE 8080

CMD ["python3", "main.py"]
