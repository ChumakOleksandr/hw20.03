from fastapi import FastAPI

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

# app = FastAPI()
#
#
# class HelloResponse(BaseModel):
#     message: str
#
#
# @app.post("/hello", response_model=HelloResponse)
# def hello() -> HelloResponse:
#     return HelloResponse(message="Привіт з сервера!")

# Завдання 2
# Напишіть сервер1:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8000
# Напишіть сервер2:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8001
# Запустіть обида сервери на localhost

app = FastAPI()


@app.get("/greeting")
def greeting():
    return {"respond": "Привіт з сервера1"}
