# Завдання 1
# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи.


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def display_info(self):
        print(
            f"Прямокутник: ширина = {self.width}, висота = {self.height}, "
            f"периметр = {self.get_perimeter()}"
        )


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_perimeter(self):
        return 2 * 3.14159 * self.radius

    def display_info(self):
        print(
            f"Коло: радіус = {self.radius}, "
            f"довжина кола = {self.get_perimeter():.2f}"
        )


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def display_info(self):
        print(
            f"Трикутник: сторони = ({self.a}, {self.b}, {self.c}), "
            f"периметр = {self.get_perimeter()}"
        )


def create_figure():
    figure_type = (
        input("Введіть тип фігури (rectangle, circle, triangle): ").strip().lower()
    )

    if figure_type == "rectangle":
        width = float(input("Введіть ширину: "))
        height = float(input("Введіть висоту: "))
        return Rectangle(width, height)

    elif figure_type == "circle":
        radius = float(input("Введіть радіус: "))
        return Circle(radius)

    elif figure_type == "triangle":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        return Triangle(a, b, c)

    else:
        print("Невідомий тип фігури!")
        return None


figures = []

print("Створення фігур:")
for _ in range(3):
    fig = create_figure()
    if fig:
        figures.append(fig)

print("\nІнформація про всі фігури:")
for fig in figures:
    fig.display_info()
