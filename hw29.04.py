import json
import pickle
from typing import cast

# Завдання 1
# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

JSON_FILE = "bands.json"
PICKLE_FILE = "bands.pkl"

Bands = dict[str, list[str]]


def add_band(bands: Bands, band_name: str) -> None:
    if band_name in bands:
        print("Такий гурт вже існує.")
        return
    bands[band_name] = []
    print("Гурт додано.")


def add_album(bands: Bands, band_name: str, album: str) -> None:
    if band_name not in bands:
        print("Такого гурту не існує.")
        return
    bands[band_name].append(album)
    print("Альбом додано.")


def show_bands(bands: Bands) -> None:
    if not bands:
        print("Список гуртів порожній.")
        return

    for band, albums in bands.items():
        print(f"{band}: {albums}")


def save_bands_json(bands: Bands) -> None:
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(bands, f, ensure_ascii=False, indent=4)
    print("Дані збережено у JSON.")


def load_bands_json() -> Bands:
    try:
        with open(JSON_FILE, encoding="utf-8") as f:
            data = json.load(f)
            return cast(Bands, data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Не вдалося завантажити JSON.")
        return {}


def save_bands_pickle(bands: Bands) -> None:
    with open(PICKLE_FILE, "wb") as f:
        pickle.dump(bands, f)
    print("Дані збережено у pickle.")


def load_bands_pickle() -> Bands:
    try:
        with open(PICKLE_FILE, "rb") as f:
            data = pickle.load(f)
            return cast(Bands, data)
    except (FileNotFoundError, pickle.UnpicklingError):
        print("Не вдалося завантажити pickle.")
        return {}


def bands_menu() -> None:
    bands: Bands = {}

    while True:
        print("\n--- МЕНЮ МУЗИЧНИХ ГУРТІВ ---")
        print("1. Додати гурт")
        print("2. Додати альбом")
        print("3. Показати всі гурти")
        print("4. Зберегти у JSON")
        print("5. Завантажити з JSON")
        print("6. Зберегти у pickle")
        print("7. Завантажити з pickle")
        print("8. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            add_band(bands, input("Назва гурту: "))
        elif choice == "2":
            add_album(bands, input("Назва гурту: "), input("Назва альбому: "))
        elif choice == "3":
            show_bands(bands)
        elif choice == "4":
            save_bands_json(bands)
        elif choice == "5":
            bands = load_bands_json()
        elif choice == "6":
            save_bands_pickle(bands)
        elif choice == "7":
            bands = load_bands_pickle()
        elif choice == "8":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    bands_menu()
