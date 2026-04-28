import json
import pickle
from typing import cast

# Завдання 1
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

JSON_FILE = "products.json"
PICKLE_FILE = "products.pkl"


def add_product(products: list[str]) -> None:
    name: str = input("Введіть назву товару: ")
    products.append(name)
    print("Товар додано.")


def show_products(products: list[str]) -> None:
    if not products:
        print("Список товарів порожній.")
        return

    print("Список товарів:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product}")


def save_json(products: list[str]) -> None:
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print("Дані збережено у JSON.")


def load_json() -> list[str]:
    try:
        with open(JSON_FILE, encoding="utf-8") as f:
            data = json.load(f)
            return cast(list[str], data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Не вдалося завантажити JSON.")
        return []


def save_pickle(products: list[str]) -> None:
    with open(PICKLE_FILE, "wb") as f:
        pickle.dump(products, f)
    print("Дані збережено у pickle.")


def load_pickle() -> list[str]:
    try:
        with open(PICKLE_FILE, "rb") as f:
            data = pickle.load(f)
            return cast(list[str], data)
    except (FileNotFoundError, pickle.UnpicklingError):
        print("Не вдалося завантажити pickle.")
        return []


def menu() -> None:
    products: list[str] = []

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати товар")
        print("2. Показати товари")
        print("3. Зберегти у JSON")
        print("4. Завантажити з JSON")
        print("5. Зберегти у pickle")
        print("6. Завантажити з pickle")
        print("7. Вийти")

        choice: str = input("Оберіть пункт: ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            show_products(products)
        elif choice == "3":
            save_json(products)
        elif choice == "4":
            products = load_json()
        elif choice == "5":
            save_pickle(products)
        elif choice == "6":
            products = load_pickle()
        elif choice == "7":
            print("До побачення!")
            break
        else:
            print("Невірний вибір!")


if __name__ == "__main__":
    menu()
