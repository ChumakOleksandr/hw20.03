import random
import time

from settings import settings

while True:
    length = random.randint(settings.min_len, settings.max_len)
    line = settings.symbol * length
    print(line)
    time.sleep(settings.delay)
