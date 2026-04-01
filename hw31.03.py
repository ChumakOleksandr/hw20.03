import random

# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального


class Car:
    def __init__(
        self, brand: str, mileage: float, fuel_level: float, fuel_consumption: float
    ):
        self.brand = brand
        self.mileage = mileage
        self.fuel_level = fuel_level
        self.fuel_consumption = fuel_consumption
        self.is_working = True

    def drive(self, distance: float):
        if not self.is_working:
            print("Автомобіль несправний і не може їхати!")
            return

        fuel_needed = distance * self.fuel_consumption
        if fuel_needed > self.fuel_level:
            print("Недостатньо пального, щоб проїхати таку відстань!")
            return

        self.fuel_level -= fuel_needed
        self.mileage += distance
        print(f"Автомобіль проїхав {distance} км.")

        if random.random() < 0.4:
            self.is_working = False
            print("Автомобіль зламався під час руху!")

    def repair(self):
        if self.is_working:
            print("Автомобіль уже справний.")
        else:
            self.is_working = True
            print("Автомобіль успішно відремонтовано.")

    def refuel(self, amount: float):
        if amount <= 0:
            print("Кількість пального має бути додатною!")
            return
        self.fuel_level += amount
        print(f"Додано {amount} л пального.")
