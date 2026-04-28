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

# Завдання 2
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.


class Student:
    def __init__(self, name: str, specialization: str):
        self._name: str = name
        self._specialization: str = specialization
        self._grades: list[int] = []

    def add_grade(self, grade: int) -> None:
        self._grades.append(grade)

    def _average_grade(self) -> float:
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def show_info(self) -> None:
        print(f"Ім'я: {self._name}")
        print(f"Спеціалізація: {self._specialization}")
        print(f"Середня оцінка: {self._average_grade():.2f}")
        print("-" * 30)


def save_students_json(
    students: list[Student], filename: str = "students.json"
) -> None:
    data = [
        {
            "name": s._name,
            "specialization": s._specialization,
            "grades": s._grades,
        }
        for s in students
    ]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_students_json(filename: str = "students.json") -> list[Student]:
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)

    students: list[Student] = []
    for item in cast(list[dict], data):
        student = Student(item["name"], item["specialization"])
        student._grades = item["grades"]
        students.append(student)

    return students


def save_students_pickle(
    students: list[Student], filename: str = "students.pkl"
) -> None:
    with open(filename, "wb") as f:
        pickle.dump(students, f)


def load_students_pickle(filename: str = "students.pkl") -> list[Student]:
    with open(filename, "rb") as f:
        data = pickle.load(f)
        return cast(list[Student], data)


if __name__ == "__main__":
    s1 = Student("Іван", "Програмування")
    s1.add_grade(90)
    s1.add_grade(85)

    s2 = Student("Олена", "Дизайн")
    s2.add_grade(88)
    s2.add_grade(92)

    s3 = Student("Андрій", "Кібербезпека")
    s3.add_grade(75)
    s3.add_grade(80)

    students = [s1, s2, s3]

    save_students_json(students)
    save_students_pickle(students)

    students_from_json = load_students_json()
    students_from_pickle = load_students_pickle()

    print("Дані з JSON:")
    for student in students_from_json:
        student.show_info()

    print("Дані з pickle:")
    for student in students_from_pickle:
        student.show_info()

# Завдання 3
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


BANDS_JSON_FILE = "bands.json"
BANDS_PICKLE_FILE = "bands.pkl"


def add_band(bands: dict[str, list[str]], band_name: str) -> None:
    if band_name in bands:
        print("Такий гурт вже існує.")
        return
    bands[band_name] = []
    print("Гурт додано.")


def add_album(bands: dict[str, list[str]], band_name: str, album: str) -> None:
    if band_name not in bands:
        print("Такого гурту не існує.")
        return
    bands[band_name].append(album)
    print("Альбом додано.")


def show_bands(bands: dict[str, list[str]]) -> None:
    if not bands:
        print("Список гуртів порожній.")
        return

    for band, albums in bands.items():
        print(f"{band}: {albums}")


def save_bands_json(bands: dict[str, list[str]]) -> None:
    with open(BANDS_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(bands, f, ensure_ascii=False, indent=4)
    print("Дані збережено у JSON.")


def load_bands_json() -> dict[str, list[str]]:
    try:
        with open(BANDS_JSON_FILE, encoding="utf-8") as f:
            data = json.load(f)
            return cast(dict[str, list[str]], data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Не вдалося завантажити JSON.")
        return {}


def save_bands_pickle(bands: dict[str, list[str]]) -> None:
    with open(BANDS_PICKLE_FILE, "wb") as f:
        pickle.dump(bands, f)
    print("Дані збережено у pickle.")


def load_bands_pickle() -> dict[str, list[str]]:
    try:
        with open(BANDS_PICKLE_FILE, "rb") as f:
            data = pickle.load(f)
            return cast(dict[str, list[str]], data)
    except (FileNotFoundError, pickle.UnpicklingError):
        print("Не вдалося завантажити pickle.")
        return {}


def bands_menu() -> None:
    bands: dict[str, list[str]] = {}

    while True:
        print("\n--- МЕНЮ ГУРТІВ ---")
        print("1. Додати гурт")
        print("2. Додати альбом")
        print("3. Показати гурти")
        print("4. Зберегти у JSON")
        print("5. Завантажити з JSON")
        print("6. Зберегти у pickle")
        print("7. Завантажити з pickle")
        print("8. Вийти")

        choice = input("Оберіть пункт: ")

        if choice == "1":
            add_band(bands, input("Назва гурту: "))
        elif choice == "2":
            add_album(
                bands,
                input("Назва гурту: "),
                input("Назва альбому: "),
            )
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
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    bands_menu()
