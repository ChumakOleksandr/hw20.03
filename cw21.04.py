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
