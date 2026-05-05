import json

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

# app = FastAPI()
#
#
# @app.get("/greeting")
# def greeting():
#     return {"respond": "Привіт з сервера1"}

# Завдання 4
# Напишіть сервер для симуляції роботи бібліотеки.
# Дані про книги знаходяться у файлі books.json
# Напишіть модель на pydentic для книги з такими
# даними:
# ● id
# ● title
# ● author
# ● year
# ● pages
# Функціонал:
# 1. Отримання всіх книг
# ○ шлях – books
# ○ метод – GET
# 2. Отримання даних за ID книги
# ○ шлях – books/{book_id}
# ○ метод – GET
# 3. Додавання нової книги
# ○ шлях – books
# ○ метод – POST
# 4. Видалення книги за ID
# ○ шлях – books/{book_id}
# ○ метод – DELETE

app = FastAPI()

BOOKS_FILE = "books.json"


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int


def load_books() -> list[Book]:
    with open(BOOKS_FILE, encoding="utf-8") as file:
        data = json.load(file)
        return [Book(**item) for item in data]


def save_books(books: list[Book]) -> None:
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump([book.dict() for book in books], file, ensure_ascii=False, indent=4)


@app.get("/books")
def get_books():
    return load_books()


@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    books = load_books()
    for book in books:
        if book.id == book_id:
            return book

    return {"message": "Книга не знайдена"}


@app.post("/books")
def add_book(new_book: Book):
    books = load_books()

    for book in books:
        if book.id == new_book.id:
            return {"message": "Книга з таким ID вже існує"}

    books.append(new_book)
    save_books(books)
    return {"message": "Книгу додано", "book": new_book}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    books = load_books()
    new_books = [book for book in books if book.id != book_id]

    if len(new_books) == len(books):
        return {"message": "Книга не знайдена"}

    save_books(new_books)
    return {"message": f"Книга з id {book_id} видалена"}
