import json

from fastapi import FastAPI
from pydantic import BaseModel

# import time
# import sys
# import datetime
# import pydantic
# Завдання 1
# start_time = datetime.datetime.now()
#
# while True:
#     print("Python version:", sys.version)
#     print("Message: hello")
#     print("Pydantic version:", pydantic.__version__)
#     print("Program started at:", start_time)
#     print("-" * 40)
#
#     time.sleep(2)

# Завдання 2
# Для сервера про книги з минулого заняття
# Збережіть усі необхідні бібліотеки
# pip freeze > requirements.txt
# Створіть Dockerfile:
# ● python:3.11-slim
# ● робоча директорія – /app
# ● встановіть потрібні бібліотеки
# ● скопіюйте увесь код
# ● запустіть основний файл
# Створіть образ та контейнер
# Напишіть клієнта який робить запити на сервер
# Виведіть логи контейнера
# Спробуйте запустити другий контейнер

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
        json.dump(
            [book.model_dump() for book in books], file, ensure_ascii=False, indent=4
        )


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
