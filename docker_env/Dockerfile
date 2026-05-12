
FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./ ./

ENV LOGIN=student123

CMD ["python3", "-u", "practice.py"]
