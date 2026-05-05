from fastapi import FastAPI
from pydantic import BaseModel

# Завдання 1
# Напишіть сервер:
# ● шлях – /hello
# ● метод – POST
# Функція має повертати JSON об’єкт
# {"message": "Привіт з сервера!"}
# Запустіть сервер:
# ● host – localhost
# ● port – 8000
# uvicorn main:app --port 8000 –host localhost --reload
# Напишіть клієнта який робить запит на сервер

app = FastAPI()


class HelloResponse(BaseModel):
    message: str


@app.post("/hello", response_model=HelloResponse)
def hello() -> HelloResponse:
    return HelloResponse(message="Привіт з сервера!")
