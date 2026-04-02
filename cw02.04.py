from math import pi

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
        self._width = width
        self._height = height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def display_info(self):
        print(
            f"Прямокутник: ширина = {self._width}, висота = {self._height}, "
            f"периметр = {self.get_perimeter()}"
        )


class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    def get_perimeter(self):
        return 2 * pi * self._radius

    def display_info(self):
        print(
            f"Коло: радіус = {self._radius}, "
            f"довжина кола = {self.get_perimeter():.2f}"
        )


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self):
        return self._a + self._b + self._c

    def display_info(self):
        print(
            f"Трикутник: сторони = ({self._a}, {self._b}, {self._c}), "
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


# Завдання 2
# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька співробітників, добавте їх у список та для
# кожного викличте відповідні методи.


class Manager:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self):
        return self._base_salary

    def display_info(self):
        print(f"Менеджер {self._name}, зарплата: {self.get_salary()}")


class Developer:
    def __init__(self, name: str, base_salary: float, work_experience: float):
        self._name = name
        self._base_salary = base_salary
        self._work_experience = work_experience

    def get_salary(self):
        if self._work_experience > 4:
            return self._base_salary * 1.2
        return self._base_salary

    def display_info(self):
        print(
            f"Розробник {self._name}, стаж: {self._work_experience} років, "
            f"зарплата: {self.get_salary()}"
        )


class Inter:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self):
        return self._base_salary / 2

    def display_info(self):
        print(f"Інтерн {self._name}, зарплата: {self.get_salary()}")


def create_worker():
    worker_type = (
        input("Введіть тип працівника (manager, developer, inter): ").strip().lower()
    )

    if worker_type == "manager":
        name = input("Ім'я: ")
        base_salary = float(input("Базова зарплата: "))
        return Manager(name, base_salary)

    elif worker_type == "developer":
        name = input("Ім'я: ")
        base_salary = float(input("Базова зарплата: "))
        exp = float(input("Стаж у роках: "))
        return Developer(name, base_salary, exp)

    elif worker_type == "inter":
        name = input("Ім'я: ")
        base_salary = float(input("Базова зарплата: "))
        return Inter(name, base_salary)

    else:
        print("Невідомий тип працівника!")
        return None


workers = []

print("Створення працівників:")
for _ in range(3):
    worker = create_worker()
    if worker:
        workers.append(worker)

print("\nІнформація про всіх працівників:")
for worker in workers:
    worker.display_info()
# Завдання 3
# Створіть наступні класи:
#  Car – атрибути speed
#  Bicycle – атрибути speed
#  Boat – атрибути speed
# Методи:
#  move() – виводить повідомлення про рух
# o Car – їде по шосе зі швидкістю
# o Bicycle – їде по дорозі зі швидкістю
# o Boat – пливе по воді зі швидкістю
#  check_speed(speed) – перевіряє чи правильна швидкість,
# якщо ні то в init треба викикати ValueError з
# відповідним повідомленням
# o Car – від 20 до 200
# o Bicycle – від 10 до 30
# o Boat – від 0 до 50
# Напишіть функцію create_vehicle() яка запитує у
# користувача тип транспорту та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька транспортних засобів, добавте їх у список
# та для кожної викличте відповідні методи.


class Car:
    def __init__(self, speed: float):
        self._check_speed(speed)
        self._speed = speed

    def _check_speed(self, speed):
        if not (20 <= speed <= 200):
            raise ValueError("Швидкість автомобіля повинна бути від 20 до 200 км/год")

    def move(self):
        print(f"Автомобіль їде по шосе зі швидкістю {self._speed} км/год")


class Bicycle:
    def __init__(self, speed: float):
        self._check_speed(speed)
        self._speed = speed

    def _check_speed(self, speed):
        if not (10 <= speed <= 30):
            raise ValueError("Швидкість велосипеда повинна бути від 10 до 30 км/год")

    def move(self):
        print(f"Велосипед їде по дорозі зі швидкістю {self._speed} км/год")


class Boat:
    def __init__(self, speed: float):
        self._check_speed(speed)
        self._speed = speed

    def _check_speed(self, speed):
        if not (0 <= speed <= 50):
            raise ValueError("Швидкість човна повинна бути від 0 до 50 км/год")

    def move(self):
        print(f"Човен пливе по воді зі швидкістю {self._speed} км/год")


def create_vehicle():
    vehicle_type = (
        input("Введіть тип транспорту (car, bicycle, boat): ").strip().lower()
    )

    try:
        speed = float(input("Введіть швидкість: "))

        if vehicle_type == "car":
            return Car(speed)
        elif vehicle_type == "bicycle":
            return Bicycle(speed)
        elif vehicle_type == "boat":
            return Boat(speed)
        else:
            print("Невідомий тип транспорту!")
            return None

    except ValueError as e:
        print("Помилка:", e)
        return None


vehicles = []

print("Створення транспортних засобів:")
for _ in range(3):
    vehicle = create_vehicle()
    if vehicle:
        vehicles.append(vehicle)

print("\nІнформація про всі транспортні засоби:")
for vehicle in vehicles:
    vehicle.move()
