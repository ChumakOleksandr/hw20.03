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
        self._user = user
        self._text = text
        self._time = datetime.strptime(time_str, "%H:%M")

    def __str__(self):
        return f"[{self._time.strftime('%H:%M')}] {self._user}: {self._text}"

    def __len__(self):
        return len(self._text)

    def __gt__(self, other):
        return self._time < other.__time  # менший час = старіше повідомлення

    def get_time(self):
        return self._time


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

# Завдання 2
# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#  __len__(self) – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран


class Song:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __eq__(self, other):
        return (
            self._name.lower() == other._name.lower()
            and self._author.lower() == other._author.lower()
        )

    def __str__(self):
        return f"{self._name} — {self._author}"


class Playlist:
    def __init__(self):
        self._songs = []

    def __len__(self):
        return len(self._songs)

    def __contains__(self, item: Song):
        return item in self._songs

    def __iter__(self):
        return iter(self._songs)
