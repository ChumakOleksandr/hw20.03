from abc import ABC

# Завдання 1
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off


class Robot(ABC):
    def __init__(self, name, battery_level=100):
        self._name = name
        self._battery_level = battery_level
        self._status = "off"

    def info(self):
        print(f"Robot: {self._name}")
        print(f"Battery: {self._battery_level}%")
        print(f"Status: {self._status}")

    def charge(self):
        self._battery_level = 100

    def turn_on(self):
        self._status = "on"

    def turn_off(self):
        self._status = "off"


# Завдання 2
# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за
# замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за
# замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy


class CleaningRobot(Robot):
    def __init__(
        self,
        name,
        battery_level=100,
        dust_capacity=0,
        water_capacity=100,
        cleaning_mode="dry",
    ):
        super().__init__(name, battery_level)
        self._dust_capacity = dust_capacity
        self._water_capacity = water_capacity
        self._cleaning_mode = cleaning_mode

    def info(self):
        super().info()
        print(f"Dust container: {self._dust_capacity}%")
        print(f"Water container: {self._water_capacity}%")
        print(f"Cleaning mode: {self._cleaning_mode}")

    def turn_on(self):
        if self._dust_capacity >= 100:
            print("Контейнер для пилу повний!")
            return
        if self._cleaning_mode == "wet" and self._water_capacity <= 0:
            print("Немає води для вологого прибирання!")
            return

        super().turn_on()

    def empty_dustbin(self):
        self._dust_capacity = 0

    def fill_water(self):
        self._water_capacity = 100

    def swap_mode(self):
        if self._cleaning_mode == "dry":
            self._cleaning_mode = "wet"
        else:
            self._cleaning_mode = "dry"

    def clean(self, energy, dust, water=None):
        if self._battery_level < energy:
            print("Недостатньо заряду!")
            return

        if self._cleaning_mode == "dry":
            if self._dust_capacity + dust > 100:
                print("Недостатньо місця в контейнері для пилу!")
                return
            self._dust_capacity += dust

        else:
            if water is None:
                print("Не вказано кількість води!")
                return
            if self._water_capacity < water:
                print("Недостатньо води!")
                return
            if self._dust_capacity + dust > 100:
                print("Недостатньо місця в контейнері для пилу!")
                return

            self._dust_capacity += dust
            self._water_capacity -= water

        self._battery_level -= energy
        if self._battery_level < 0:
            self._battery_level = 0
