from abc import ABC, abstractmethod

# Завдання 1
# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я
#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense – стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp


class Character(ABC):
    def __init__(
        self, name, max_hp, level, intelligence, strength, dexterity, mana, defense
    ):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._level = level
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense

    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, damage):
        real_damage = damage - self._defense
        if real_damage < 0:
            real_damage = 0

        self._hp -= real_damage
        if self._hp < 0:
            self._hp = 0

        print(
            f"{self._name} отримує {real_damage} урону. HP: {self._hp}/{self._max_hp}"
        )

    def level_up(self):
        if self._level < 20:
            self._level += 1
            print(f"{self._name} підняв рівень! Тепер {self._level}.")
        else:
            print(f"{self._name} вже має максимальний рівень.")

    def increase_stat(self, stat):
        if stat == "intelligence":
            self._intelligence += 1
        elif stat == "strength":
            self._strength += 1
        elif stat == "dexterity":
            self._dexterity += 1
        elif stat == "mana":
            self._mana += 1
        elif stat == "defense":
            self._defense += 1
        else:
            print("Такого стату не існує.")
            return

        print(f"{self._name} збільшив стат '{stat}' на 1.")

    def rest(self):
        self._hp = self._max_hp
        print(f"{self._name} відпочив і повністю відновив HP.")

    def heal(self, heal_hp):
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp = self._max_hp

        print(f"{self._name} відновив {heal_hp} HP. Тепер: {self._hp}/{self._max_hp}")
