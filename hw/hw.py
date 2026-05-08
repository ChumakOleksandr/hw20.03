import json

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

FILMS_FILE = "films.json"


class Film(BaseModel):
    id: int
    title: str
    director: str
    year: int


def load_films() -> list[Film]:
    with open(FILMS_FILE, encoding="utf-8") as file:
        data = json.load(file)
        return [Film(**item) for item in data]


def save_films(films: list[Film]) -> None:
    with open(FILMS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            [film.model_dump() for film in films],
            file,
            ensure_ascii=False,
            indent=4,
        )


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    films = load_films()
    for film in films:
        if film.id == movie_id:
            return film

    return {"message": "Фільм не знайдено"}


@app.post("/movies")
def add_movie(new_film: Film):
    films = load_films()

    for film in films:
        if film.id == new_film.id:
            return {"message": "Фільм з таким ID вже існує"}

    films.append(new_film)
    save_films(films)
    return {"message": "Фільм додано", "film": new_film}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    films = load_films()
    updated_films = [film for film in films if film.id != movie_id]

    if len(updated_films) == len(films):
        return {"message": "Фільм не знайдено"}

    save_films(updated_films)
    return {"message": f"Фільм з id {movie_id} видалено"}
