# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик


class Cart:
    def __init__(self, client):
        self.client = client
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Товар '{item}' додано до кошика.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Товар '{item}' видалено з кошика.")
        else:
            print(f"Товар '{item}' відсутній у кошику.")

    def show_cart(self):
        print(f"\nКошик клієнта: {self.client}")
        if not self.items:
            print("Кошик порожній.")
        else:
            print("Товари у кошику:")
            for item in self.items:
                print(f" - {item}")


cart = Cart("Олександр")

cart.add_item("Яблука")
cart.add_item("Молоко")
cart.add_item("Хліб")

cart.show_cart()

cart.remove_item("Молоко")
cart.show_cart()

# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.


class Phone:
    def __init__(self, number, battery_level):
        self.number = number
        self.battery_level = battery_level

    def decrease_battery(self, percent):
        if percent < 0:
            print("Не можна зменшити заряд на від’ємне значення.")
            return

        self.battery_level -= percent

        if self.battery_level < 0:
            self.battery_level = 0

        print(f"Заряд зменшено на {percent}%. Поточний рівень: {self.battery_level}%")

        if self.battery_level < 20:
            print("Увага! Заряд телефону нижче 20%!")

    def show_info(self):
        print(f"Номер телефону: {self.number}")
        print(f"Рівень заряду: {self.battery_level}%")


phone = Phone("+380501234567", 50)

phone.show_info()
phone.decrease_battery(25)
phone.decrease_battery(10)
phone.show_info()
