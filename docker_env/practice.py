import time

from settings import settings

while True:
    print(f"app_name = {settings.app_name}")
    print(f"filename = {settings.filename}")
    print(f"login = {settings.login}")
    print(f"password = {settings.password}")
    print("-" * 30)

    time.sleep(2)
