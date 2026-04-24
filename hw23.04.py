import json
import random

# Завдання 1
# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями


STATS_FILE = "stats.json"


def load_stats():
    try:
        with open(STATS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"wins": 0, "losses": 0}


def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)


def show_stats(stats):
    print(f"Перемоги: {stats['wins']}")
    print(f"Програші: {stats['losses']}")


def play_game(stats):
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("\nЯ загадал число від 1 до 100.")
    print("Спробуй вгадати!")

    while attempts < max_attempts:
        guess = int(input("Введіть число: "))
        attempts += 1

        if guess < secret_number:
            print("Більше")
        elif guess > secret_number:
            print("Менше")
        else:
            print("Ви вгадали!")
            print(f"Кількість спроб: {attempts}")
            stats["wins"] += 1
            return

    print(f"Ви програли. Загадане число було: {secret_number}")
    stats["losses"] += 1


def menu():
    stats = load_stats()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Почати нову гру")
        print("2. Показати результат")
        print("3. Зберегти дані")
        print("4. Завантажити дані")
        print("5. Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            play_game(stats)
        elif choice == "2":
            show_stats(stats)
        elif choice == "3":
            save_stats(stats)
            print("Дані збережено.")
        elif choice == "4":
            stats = load_stats()
            print("Дані завантажено.")
        elif choice == "5":
            save_stats(stats)
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    menu()
