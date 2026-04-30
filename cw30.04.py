import threading

# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.


# def find_max(numbers: list[int], result: dict[str, int]) -> None:
#     result["max"] = max(numbers)
#
#
# def find_min(numbers: list[int], result: dict[str, int]) -> None:
#     result["min"] = min(numbers)
#
#
# def main() -> None:
#     input_text = input("Введіть числа через пробіл: ")
#     string_numbers = input_text.split()
#     numbers = [int(number) for number in string_numbers]
#
#     results: dict[str, int] = {}
#
#     max_thread = threading.Thread(target=find_max, args=(numbers, results))
#     min_thread = threading.Thread(target=find_min, args=(numbers, results))
#
#     max_thread.start()
#     min_thread.start()
#
#     max_thread.join()
#     min_thread.join()
#
#     print(f"Максимальне значення: {results['max']}")
#     print(f"Мінімальне значення: {results['min']}")
#
#
# if __name__ == "__main__":
#     main()

# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.


def calculate_sum(numbers: list[int], result: dict[str, float]) -> None:
    result["sum"] = sum(numbers)


def calculate_average(numbers: list[int], result: dict[str, float]) -> None:
    result["average"] = sum(numbers) / len(numbers) if numbers else 0


def main() -> None:
    input_text = input("Введіть числа через пробіл: ")
    string_numbers = input_text.split()
    numbers = [int(number) for number in string_numbers]

    results: dict[str, float] = {}

    sum_thread = threading.Thread(target=calculate_sum, args=(numbers, results))
    avg_thread = threading.Thread(target=calculate_average, args=(numbers, results))

    sum_thread.start()
    avg_thread.start()

    sum_thread.join()
    avg_thread.join()

    print(f"Сума елементів: {results['sum']}")
    print(f"Середнє арифметичне: {results['average']}")


if __name__ == "__main__":
    main()
