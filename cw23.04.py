import json
from typing import cast

# Завдання 1
# Є словник з логінами(ключ) та паролями(значення)
# користувачів. Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна паролю
#  вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.

FILE_NAME: str = "users.json"


def load_users() -> dict[str, str]:
    try:
        with open(FILE_NAME, encoding="utf-8") as f:
            return cast(dict[str, str], json.load(f))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_users(users: dict[str, str]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def add_user(users: dict[str, str], login: str, password: str) -> None:
    if login in users:
        print("Користувач вже існує!")
        return

    users[login] = password
    save_users(users)
    print("Користувача додано.")


def delete_user(users: dict[str, str], login: str) -> None:
    if login not in users:
        print("Користувача не існує!")
        return

    del users[login]
    save_users(users)
    print("Користувача видалено.")


def change_password(users: dict[str, str], login: str, new_password: str) -> None:
    if login not in users:
        print("Користувача не існує!")
        return

    users[login] = new_password
    save_users(users)
    print("Пароль змінено.")


def login_system(users: dict[str, str], login: str, password: str) -> bool:
    if login in users and users[login] == password:
        print("Вхід успішний")
        return True
    else:
        print("Невірний логін або пароль")
        return False


users: dict[str, str] = load_users()

add_user(users, "ivan", "12345")
add_user(users, "olga", "qwerty")

login_system(users, "ivan", "12345")

change_password(users, "ivan", "newpass")

delete_user(users, "olga")

# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
#  save(fiename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за
# замовчуванням cart.json)


class Cart:
    def __init__(self, user: str):
        self._user: str = user
        self._items: list[str] = []
        self._total: float = 0.0

    def add(self, item: str, price: float) -> None:
        self._items.append(item)
        self._total += price

    def delete(self, item: str, price: float) -> None:
        if item in self._items:
            self._items.remove(item)
            self._total -= price
            if self._total < 0:
                self._total = 0
        else:
            print("Товару немає у кошику")

    def info(self) -> None:
        print(f"Користувач: {self._user}")
        print(f"Товари: {self._items}")
        print(f"Загальна сума: {self._total}")

    def save(self, filename: str = "cart.json") -> None:
        data = {
            "user": self._user,
            "items": self._items,
            "total": self._total,
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self, filename: str = "cart.json") -> None:
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)

        self._user = data["user"]
        self._items = data["items"]
        self._total = data["total"]


art = Cart("Іван")

art.add("Хліб", 25)
art.add("Молоко", 40)

art.info()
art.save()

new_cart = Cart("")
new_cart.load()
new_cart.info()

# Завдання 3
# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу
# Напишіть код, де завантажується налаштування і
# створюються відповідні змінні size, background_color, …

with open("settings.json", encoding="utf-8") as f:
    settings: dict = json.load(f)

size: list[int] = settings["size"]
background_color: str = settings["background_color"]
button_color: str = settings["button_color"]
button_position: list[int] = settings["button_position"]
instruction: str = settings["instruction"]


print("Size:", size)
print("Background color:", background_color)
print("Button color:", button_color)
print("Button position:", button_position)
print("Instruction:", instruction)
