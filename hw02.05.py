import threading

# Завдання 1
# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран


def input_numbers(numbers: list[int], done_event: threading.Event) -> None:
    while True:
        user_input = input("Введіть число (порожній рядок — завершити): ")
        if user_input == "":
            break
        numbers.append(int(user_input))

    done_event.set()


def calculate_sum(
    numbers: list[int], result: dict[str, float], done_event: threading.Event
) -> None:
    done_event.wait()
    result["sum"] = sum(numbers)


def calculate_average(
    numbers: list[int], result: dict[str, float], done_event: threading.Event
) -> None:
    done_event.wait()
    if numbers:
        result["average"] = sum(numbers) / len(numbers)
    else:
        result["average"] = 0.0


def main() -> None:
    numbers: list[int] = []
    results: dict[str, float] = {}

    done_event = threading.Event()

    input_thread = threading.Thread(target=input_numbers, args=(numbers, done_event))
    sum_thread = threading.Thread(
        target=calculate_sum, args=(numbers, results, done_event)
    )
    avg_thread = threading.Thread(
        target=calculate_average, args=(numbers, results, done_event)
    )

    input_thread.start()
    sum_thread.start()
    avg_thread.start()

    input_thread.join()
    sum_thread.join()
    avg_thread.join()

    print("\nРезультати:")
    print(f"Список чисел: {numbers}")
    print(f"Сума: {results['sum']}")
    print(f"Середнє арифметичне: {results['average']}")


if __name__ == "__main__":
    main()
