from abc import ABC, abstractmethod

# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5


class Pet(ABC):
    def __init__(self, name, satiety=50, energy=50):
        self._name = name
        self._satiety = satiety
        self._energy = energy

    def sleep(self):
        self._energy = 100

    def eat(self, food_amount):
        self._satiety = min(100, self._satiety + food_amount)

    @abstractmethod
    def play(self, activity_level):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level):
        if self._satiety > 60:
            self._energy -= 2 * activity_level
            self._satiety -= activity_level

            if self._energy < 0:
                self._energy = 0
            if self._satiety < 0:
                self._satiety = 0

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self._energy > 30:
            if self._satiety > 40:
                self._energy -= 10
            else:
                self.eat(20)


class Dog(Pet):
    def play(self, activity_level):
        if self._satiety > 15:
            loss = activity_level // 2
            self._energy -= loss
            self._satiety -= loss

            if self._energy < 0:
                self._energy = 0
            if self._satiety < 0:
                self._satiety = 0

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self._satiety > 10:
            self._energy -= 5
            if self._energy < 0:
                self._energy = 0
