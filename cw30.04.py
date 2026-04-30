import threading

# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.


def find_max(numbers: list[int]) -> None:
    max_value = max(numbers)
    print(f"Максимальне значення: {max_value}")


def find_min(numbers: list[int]) -> None:
    min_value = min(numbers)
    print(f"Мінімальне значення: {min_value}")


def main() -> None:
    user_input = input("Введіть числа через пробіл: ")
    numbers = [int(num) for num in user_input.split()]

    t1 = threading.Thread(target=find_max, args=(numbers,))
    t2 = threading.Thread(target=find_min, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
