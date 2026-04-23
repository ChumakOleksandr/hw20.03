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
