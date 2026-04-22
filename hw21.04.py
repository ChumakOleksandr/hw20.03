# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує


class Passenger:
    def __init__(self, name: str, destination: str):
        self.name = name
        self.destination = destination


# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали


class Transport:
    def __init__(self, speed: float):
        self.speed = speed  # км/год

    def move(self, destination: str, distance: float):
        time = distance / self.speed
        print(
            f"Рухаємося до {destination}. "
            f"Відстань: {distance} км, час у дорозі: {time:.2f} год"
        )


# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()


class Bus(Transport):
    def __init__(self, speed: float, capacity: int):
        super().__init__(speed)
        self.capacity = capacity
        self.passengers: list[Passenger] = []

    def board_passenger(self, passenger: Passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
        else:
            print("Автобус заповнений, немає місця для пасажира")

    def move(self, destination: str, distance: float):
        leaving_passengers = [
            passenger
            for passenger in self.passengers
            if passenger.destination == destination
        ]

        self.passengers = [
            passenger
            for passenger in self.passengers
            if passenger.destination != destination
        ]

        print(
            f"На зупинці {destination} вийшло пасажирів: " f"{len(leaving_passengers)}"
        )

        super().move(destination, distance)
