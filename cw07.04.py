from datetime import datetime

# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть


class Message:
    def __init__(self, user: str, text: str, time_str: str):
        self.__user = user
        self.__text = text
        self.__time = datetime.strptime(time_str, "%H:%M")

    def __str__(self):
        return f"[{self.__time.strftime('%H:%M')}] {self.__user}: {self.__text}"

    def __len__(self):
        return len(self.__text)

    def __gt__(self, other):
        return self.__time < other.__time  # менший час = старіше повідомлення

    def get_time(self):
        return self.__time


messages = [
    Message("Олег", "Привіт!", "10:23"),
    Message("Ірина", "Як справи?", "09:15"),
    Message("Андрій", "Все добре!", "11:40"),
]

print("Початковий список повідомлень:")
for msg in messages:
    print(msg)

messages.sort()

print("\nВідсортований список повідомлень:")
for msg in messages:
    print(msg)

print("\nДовжина тексту першого повідомлення:", len(messages[0]))
