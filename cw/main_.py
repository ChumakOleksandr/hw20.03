import datetime
import sys
import time

import pydantic

# Завдання 1
start_time = datetime.datetime.now()

while True:
    print("Python version:", sys.version)
    print("Message: hello")
    print("Pydantic version:", pydantic.__version__)
    print("Program started at:", start_time)
    print("-" * 40)

    time.sleep(2)
