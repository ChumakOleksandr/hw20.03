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


# Завдання 2
# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana


class Paladin(Character):
    def __init__(
        self, name, max_hp, level, intelligence, strength, dexterity, mana, defense
    ):
        super().__init__(
            name, max_hp, level, intelligence, strength, dexterity, mana, defense
        )

    def attack(self, target):
        if self._mana >= 5:
            damage = 4 * self._strength
            self._mana -= 5
        else:
            damage = self._strength

        target.take_damage(damage)

    def shield(self):
        buff = 4 + self._level
        self._defense += buff

    def unshield(self):
        buff = 4 + self._level
        self._defense -= buff

    def heal_ally(self, ally):
        heal_amount = 5 + 2 * self._level + 0.5 * self._mana
        heal_amount = int(heal_amount)
        ally.heal(heal_amount)


# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить
# урону
#  heal_ally(ally) – лікує союзника на 3 + level +
# 3*intelligence


class Mage(Character):
    def __init__(
        self, name, max_hp, level, intelligence, strength, dexterity, mana, defense
    ):
        super().__init__(
            name, max_hp, level, intelligence, strength, dexterity, mana, defense
        )

    def attack(self, target):
        if self._mana >= 3:
            damage = 3 * self._intelligence + 4
            self._mana -= 3
            target.take_damage(damage)
        else:
            target.take_damage(0)

    def fireball(self, targets):
        if self._mana >= 5:
            damage = 2 * self._intelligence + 3
            self._mana -= 5
            for t in targets:
                t.take_damage(damage)
        else:
            return

    def heal_ally(self, ally):
        heal_amount = 3 + self._level + 3 * self._intelligence
        ally.heal(heal_amount)


# Завдання 4
# Створіть дочірній клас Warrior
# Методи:
#  attack() – наносить 4*strength+3 урону
#  power_strike(enemies) – проходить по списку ворогів:
# якщо їхній рівень менший за рівень персонажа, то
# знищує його повністю


class Warrior(Character):
    def __init__(
        self, name, max_hp, level, intelligence, strength, dexterity, mana, defense
    ):
        super().__init__(
            name, max_hp, level, intelligence, strength, dexterity, mana, defense
        )

    def attack(self, target):
        damage = 4 * self._strength + 3
        target.take_damage(damage)

    def power_strike(self, enemies):
        for enemy in enemies:
            if enemy._level < self._level:
                enemy.take_damage(enemy._hp)


# Завдання 5
# Створіть дочірній клас Rogue
# Методи:
#  attack() – наносить strength+level урону


class Rogue(Character):
    def __init__(
        self, name, max_hp, level, intelligence, strength, dexterity, mana, defense
    ):
        super().__init__(
            name, max_hp, level, intelligence, strength, dexterity, mana, defense
        )

    def attack(self, target):
        damage = self._strength + self._level
        target.take_damage(damage)
