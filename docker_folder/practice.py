import random
import time

while True:
    # кожні 2 секунди виводимо випадкове число
    time.sleep(2)
    print(random.randint(0, 100))

# створення образу
# docker build -t [назву образу] [шлях до Dockerfile]

# docker run [-d] --name [назва контейнера] [назва образу]
