import json

from fastapi import FastAPI
from pydantic import BaseModel
from settings import settings

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int


def load_books() -> list[Book]:
    with open(settings.data_file_path, encoding="utf-8") as file:
        data = json.load(file)
        return [Book(**item) for item in data]


def save_books(books: list[Book]) -> None:
    with open(settings.data_file_path, "w", encoding="utf-8") as file:
        json.dump(
            [book.model_dump() for book in books],
            file,
            ensure_ascii=False,
            indent=4,
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

    if settings.max_books is not None and len(books) >= settings.max_books:
        return {"message": "Досягнуто максимальної кількості книг"}

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
