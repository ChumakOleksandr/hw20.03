import json
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


# def calculate_sum(numbers: list[int], result: dict[str, float]) -> None:
#     result["sum"] = sum(numbers)
#
#
# def calculate_average(numbers: list[int], result: dict[str, float]) -> None:
#     result["average"] = sum(numbers) / len(numbers) if numbers else 0
#
#
# def main() -> None:
#     input_text = input("Введіть числа через пробіл: ")
#     string_numbers = input_text.split()
#     numbers = [int(number) for number in string_numbers]
#
#     results: dict[str, float] = {}
#
#     sum_thread = threading.Thread(target=calculate_sum, args=(numbers, results))
#     avg_thread = threading.Thread(target=calculate_average, args=(numbers, results))
#
#     sum_thread.start()
#     avg_thread.start()
#
#     sum_thread.join()
#     avg_thread.join()
#
#     print(f"Сума елементів: {results['sum']}")
#     print(f"Середнє арифметичне: {results['average']}")
#
#
# if __name__ == "__main__":
#     main()

# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.


# def read_numbers_from_file(path: str) -> list[int]:
#     with open(path, encoding="utf-8") as file:
#         content = file.read()
#         return [int(number) for number in content.split()]
#
#
# def write_even_numbers(numbers: list[int], result: dict[str, int]) -> None:
#     even_numbers = [num for num in numbers if num % 2 == 0]
#
#     with open("even.txt", "w", encoding="utf-8") as file:
#         file.write(" ".join(map(str, even_numbers)))
#
#     result["even_count"] = len(even_numbers)
#
#
# def write_odd_numbers(numbers: list[int], result: dict[str, int]) -> None:
#     odd_numbers = [num for num in numbers if num % 2 != 0]
#
#     with open("odd.txt", "w", encoding="utf-8") as file:
#         file.write(" ".join(map(str, odd_numbers)))
#
#     result["odd_count"] = len(odd_numbers)
#
#
# def main() -> None:
#     file_path = input("Введіть шлях до файлу з числами: ")
#
#     numbers = read_numbers_from_file(file_path)
#
#     results: dict[str, int] = {}
#
#     even_thread = threading.Thread(target=write_even_numbers, args=(numbers, results))
#     odd_thread = threading.Thread(target=write_odd_numbers, args=(numbers, results))
#
#     even_thread.start()
#     odd_thread.start()
#
#     even_thread.join()
#     odd_thread.join()
#
#     print(f"Кількість парних чисел: {results['even_count']}")
#     print(f"Кількість непарних чисел: {results['odd_count']}")
#
#
# if __name__ == "__main__":
#     main()

# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.


def search_word_in_json(file_path: str, word: str, result: dict[str, int]) -> None:
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

    text = str(data)

    count = text.count(word)
    result["count"] = count


def main() -> None:
    file_path = input("Введіть шлях до JSON-файлу: ")
    word = input("Введіть слово для пошуку: ")

    result: dict[str, int] = {}

    search_thread = threading.Thread(
        target=search_word_in_json, args=(file_path, word, result)
    )

    search_thread.start()
    search_thread.join()

    if result["count"] > 0:
        print(f"Слово '{word}' знайдено {result['count']} раз(ів) у JSON.")
    else:
        print(f"Слово '{word}' не знайдено у JSON.")


if __name__ == "__main__":
    main()
