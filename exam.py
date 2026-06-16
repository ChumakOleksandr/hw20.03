from datetime import datetime

# Частина 1: Основи Python
# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.(включно)

# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
#
# start = min(a, b)
# end = max(a, b)
#
# total = 0
#
# for i in range(start, end + 1):
#     total += i
#
# print(f"Сума чисел у діапазоні: {total}")

# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

# total = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
#
# print(f"Сума парних чисел: {total}")

# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

# text = input("Введіть рядок: ")
#
# for ch in text:
#     print(ch)

# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
#
# even_list = []
#
# for num in nums:
#     if num % 2 == 0:
#         even_list.append(num)
#
# print("Парні числа:", even_list)

# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

# def get_capital_words(lst):
#     result = []
#
#     for word in lst:
#         if word and word[0].isupper():
#             result.append(word)
#
#     return result
#
#
# words = input("Введіть рядки через пробіл: ").split()
#
# capital_words = get_capital_words(words)
#
# print(f"Рядки з великої літери: {capital_words}")

# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

# def find_python_lines(lst):
#     result = []
#
#     for line in lst:
#         if "Python" in line:
#             result.append(line)
#
#     return result
#
#
# lines = input("Введіть рядки через ';': ").split(";")
#
# filtered = find_python_lines(lines)
#
# print("Рядки з 'Python':")
# for line in filtered:
#     print(line)

# Частина 2: Об'єктно-орієнтоване програмування (ООП)
# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.


class WebPage:
    def __init__(
        self, title: str, content: str, publish_date: datetime | None = None
    ) -> None:
        self._title = title
        self._content = content
        self._publish_date = publish_date or datetime.now()

    def display(self) -> None:
        print(f"\nЗаголовок: {self._title}")
        print(f"Дата: {self._publish_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Вміст: {self._content}")


class WebSite:
    def __init__(self, name: str, url: str) -> None:
        self._name = name
        self._url = url
        self._pages: list[WebPage] = []

    def add_page(self, page: WebPage) -> None:
        self._pages.append(page)
        print("Сторінку додано!")

    def remove_page(self, title: str) -> None:
        for page in self._pages:
            if page._title == title:
                self._pages.remove(page)
                print("Сторінку видалено!")
                return
        print("Сторінку не знайдено!")

    def display_info(self) -> None:
        print(f"\nСайт: {self._name}")
        print(f"URL: {self._url}")
        print("Сторінки:")

        if not self._pages:
            print("Немає сторінок.")
        else:
            for page in self._pages:
                page.display()

    def search_pages(self, keyword: str) -> list[WebPage]:
        result: list[WebPage] = []
        keyword = keyword.lower()

        for page in self._pages:
            if keyword in page._title.lower() or keyword in page._content.lower():
                result.append(page)

        return result


def main_menu() -> None:
    site: WebSite | None = None

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Створити сайт")
        print("2. Додати сторінку")
        print("3. Видалити сторінку")
        print("4. Показати інформацію про сайт")
        print("5. Пошук сторінок")
        print("0. Вийти")

        choice: str = input("Ваш вибір: ")

        if choice == "1":
            name = input("Назва сайту: ")
            url = input("URL: ")
            site = WebSite(name, url)
            print("Сайт створено!")

        elif choice == "2":
            if not site:
                print("Спочатку створіть сайт!")
                continue

            title = input("Заголовок: ")
            content = input("Вміст: ")
            page = WebPage(title, content)
            site.add_page(page)

        elif choice == "3":
            if not site:
                print("Спочатку створіть сайт!")
                continue

            title = input("Заголовок для видалення: ")
            site.remove_page(title)

        elif choice == "4":
            if not site:
                print("Сайт не створено!")
                continue

            site.display_info()

        elif choice == "5":
            if not site:
                print("Спочатку створіть сайт!")
                continue

            keyword = input("Ключове слово: ")
            results = site.search_pages(keyword)

            if results:
                print("\nЗнайдені сторінки:")
                for page in results:
                    page.display()
            else:
                print("Нічого не знайдено.")

        elif choice == "0":
            print("Завершення програми...")
            break

        else:
            print("Невірний вибір!")


if __name__ == "__main__":
    main_menu()
