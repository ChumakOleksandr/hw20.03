# 27. Кількість введень
# Просіть вводити числа до введення 0. Порахуйте і виведіть кількість введених чисел
# (без нуля).
# Підказка: Використайте лічильник count, збільшуйте після кожного введення.

# count = 0
#
# while True:
#     num = int(input("Введіть число (0 — завершити): "))
#
#     if num == 0:
#         break
#
#     count += 1
#
# print(f"Кількість введених чисел (без нуля):{count}")

# 37. Кратні числа
# За допомогою for порахуйте, скільки чисел від 1 до 100 кратні 7.
# Підказка: Умова кратності: n % 7 == 0. Використайте лічильник.

# count = 0
#
# for n in range(1, 101):
#     if n % 7 == 0:
#         count += 1
#
# print(f"Кількість чисел, кратних 7: {count}")

# 45. Усі пари чисел
# Виведіть усі можливі пари (i, j), де i та j — числа від 1 до 5.
# Підказка: Два вкладені цикли; виводьте кожну пару у форматі "(i, j)".

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"({i}, {j})")

# 54. Кількість пробілів
# Введіть рядок. Порахуйте і виведіть кількість пробілів у ньому.
# Підказка: Перевіряйте ch == " " або використайте text.count(" ").

# text = input("Введіть рядок: ")
#
# count = text.count(" ")
#
# print("Кількість пробілів:", count)

# 68. Видалення від'ємних
# Маючи список чисел, видаліть із нього всі від'ємні значення. Виведіть очищений
# список.
# Підказка: Створіть новий список: [x for x in lst if x >= 0],
# або видаляйте елементи через
# remove().

# lst = [-3, 5, -1, 8, 0, -7, 2]
#
# new_lst = [x for x in lst if x >= 0]
#
# print(f"Очищений список: {new_lst}")

# 7. Клас Rectangle — прямокутник
# Атрибути: ширина (float), висота (float).
# Метод area(): повертає площу: ширина * висота.
# Метод perimeter(): повертає периметр: 2 * (ширина + висота).
# Метод resize(w, h): змінює розміри. Обидва значення мають бути > 0.

# class Rectangle:
#     def __init__(self, width: float, height: float):
#         if width <= 0 or height <= 0:
#             raise ValueError("Ширина і висота мають бути додатніми числами.")
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def resize(self, w: float, h: float):
#         if w <= 0 or h <= 0:
#             raise ValueError("Нові розміри мають бути додатніми числами.")
#         self.width = w
#         self.height = h

# 19. Симулятор банкомату
# Клас Account: атрибути — власник (str), PIN (str), баланс (float).
# Клас ATM: список рахунків (dict або list).
# Метод find_account(owner): знаходить рахунок за ім'ям власника.
# Текстове меню: 1 — Створити рахунок
# (ввести ім'я, PIN, початковий баланс). 2 —
# Поповнити рахунок (ввести ім'я, PIN, суму). 3 — Зняти гроші
# (перевіряти PIN і наявність
# коштів). 4 — Показати баланс (після перевірки PIN). 0 — Вийти.


class Account:
    def __init__(self, owner: str, pin: str, balance: float):
        self._owner = owner
        self._pin = pin
        self._balance = balance

    def check_pin(self, pin):
        return self._pin == pin

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner


class ATM:
    def __init__(self):
        self._accounts = {}

    def find_account(self, owner):
        return self._accounts.get(owner)

    def create_account(self):
        owner = input("Ім'я: ")
        pin = input("PIN: ")
        balance = float(input("Початковий баланс: "))
        self._accounts[owner] = Account(owner, pin, balance)
        print("Рахунок створено!")

    def deposit(self):
        owner = input("Ім'я: ")
        pin = input("PIN: ")
        acc = self.find_account(owner)

        if acc and acc.check_pin(pin):
            amount = float(input("Сума поповнення: "))
            if acc.deposit(amount):
                print("Баланс поповнено!")
            else:
                print("Некоректна сума!")
        else:
            print("Невірні дані!")

    def withdraw(self):
        owner = input("Ім'я: ")
        pin = input("PIN: ")
        acc = self.find_account(owner)

        if acc and acc.check_pin(pin):
            amount = float(input("Сума зняття: "))
            if acc.withdraw(amount):
                print("Гроші знято!")
            else:
                print("Недостатньо коштів або некоректна сума!")
        else:
            print("Невірні дані!")

    def show_balance(self):
        owner = input("Ім'я: ")
        pin = input("PIN: ")
        acc = self.find_account(owner)

        if acc and acc.check_pin(pin):
            print("Баланс:", acc.get_balance())
        else:
            print("Невірні дані!")


atm = ATM()

while True:
    print("\n1 — Створити рахунок")
    print("2 — Поповнити рахунок")
    print("3 — Зняти гроші")
    print("4 — Показати баланс")
    print("0 — Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        atm.create_account()
    elif choice == "2":
        atm.deposit()
    elif choice == "3":
        atm.withdraw()
    elif choice == "4":
        atm.show_balance()
    elif choice == "0":
        print("До побачення!")
        break
    else:
        print("Невірний вибір!")
