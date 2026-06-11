from typing import cast

import redis


class AuthService:
    def __init__(self) -> None:
        self.redis_client = redis.Redis(
            host="127.0.0.1", port=6379, db=0, decode_responses=True
        )

        if not self.redis_client.hexists("users", "admin"):
            self.redis_client.hset("users", "admin", "1234")

    def login(self, username: str, password: str) -> bool:
        stored_password = cast(str | None, self.redis_client.hget("users", username))

        if stored_password is None:
            return False

        return stored_password == password


class RedisRepository:
    def __init__(self, host: str = "localhost", port: int = 6379) -> None:
        self.redis_client = redis.Redis(
            host=host, port=port, db=0, decode_responses=True
        )

    def save_exhibit(self, exhibit_data: dict) -> None:
        exhibit_id = exhibit_data["id"]

        self.redis_client.hset(f"exhibit:{exhibit_id}", mapping=exhibit_data)
        self.redis_client.sadd("exhibit_ids", exhibit_id)

    def get_exhibit(self, exhibit_id: str) -> dict | None:
        exhibit_data = self.redis_client.hgetall(f"exhibit:{exhibit_id}")
        return exhibit_data if exhibit_data else None

    def delete_exhibit(self, exhibit_id: str) -> None:
        self.redis_client.delete(f"exhibit:{exhibit_id}")
        self.redis_client.srem("exhibit_ids", exhibit_id)

    def get_all_exhibits(self) -> list[dict]:
        all_exhibits = []
        for exhibit_id in self.redis_client.smembers("exhibit_ids"):
            exhibit_data = self.redis_client.hgetall(f"exhibit:{exhibit_id}")
            all_exhibits.append(exhibit_data)
        return all_exhibits

    def find_exhibits_by_type(self, exhibit_type: str) -> list[dict]:
        filtered_exhibits = []
        for exhibit_id in self.redis_client.smembers("exhibit_ids"):
            exhibit_data = self.redis_client.hgetall(f"exhibit:{exhibit_id}")
            if exhibit_data.get("type") == exhibit_type:
                filtered_exhibits.append(exhibit_data)
        return filtered_exhibits


class MuseumService:
    def __init__(self, repository: RedisRepository) -> None:
        self.repository = repository

    def add_exhibit(self) -> None:
        exhibit_id = input("ID: ")
        title = input("Назва: ")
        description = input("Опис: ")
        exhibit_type = input("Тип (book/letter/...): ")

        exhibit_data = {
            "id": exhibit_id,
            "title": title,
            "description": description,
            "type": exhibit_type,
        }

        self.repository.save_exhibit(exhibit_data)
        print("Експонат додано")

    def delete_exhibit(self) -> None:
        exhibit_id = input("ID: ")
        self.repository.delete_exhibit(exhibit_id)
        print("Видалено")

    def edit_exhibit(self) -> None:
        exhibit_id = input("ID: ")
        field_name = input("Поле (title/description/type): ")
        new_value = input("Нове значення: ")

        self.repository.redis_client.hset(
            f"exhibit:{exhibit_id}", field_name, new_value
        )
        print("Оновлено")

    def view_exhibit(self) -> None:
        exhibit_id = input("ID: ")
        exhibit_data = self.repository.get_exhibit(exhibit_id)

        if exhibit_data:
            print("\nЕкспонат:")
            for key, value in exhibit_data.items():
                print(f"{key}: {value}")
        else:
            print("Не знайдено")

    def view_all_exhibits(self) -> None:
        all_exhibits = self.repository.get_all_exhibits()

        print("\nВсі експонати:")
        for exhibit in all_exhibits:
            print("----------------")
            for key, value in exhibit.items():
                print(f"{key}: {value}")

    def filter_exhibits(self) -> None:
        exhibit_type = input("Тип: ")
        filtered_exhibits = self.repository.find_exhibits_by_type(exhibit_type)

        print("\nРезультат:")
        for exhibit in filtered_exhibits:
            print("----------------")
            for key, value in exhibit.items():
                print(f"{key}: {value}")


def main_menu() -> None:
    auth_service = AuthService()

    username = input("Логін: ")
    password = input("Пароль: ")

    if not auth_service.login(username, password):
        print("Помилка авторизації")
        return

    redis_repo = RedisRepository()
    museum_service = MuseumService(redis_repo)

    while True:
        print("\nМеню:")
        print("1. Додати експонат")
        print("2. Видалити експонат")
        print("3. Редагувати експонат")
        print("4. Переглянути експонат")
        print("5. Всі експонати")
        print("8. Фільтр по типу")
        print("0. Вихід")

        user_choice = input("Вибір: ")

        if user_choice == "1":
            museum_service.add_exhibit()
        elif user_choice == "2":
            museum_service.delete_exhibit()
        elif user_choice == "3":
            museum_service.edit_exhibit()
        elif user_choice == "4":
            museum_service.view_exhibit()
        elif user_choice == "5":
            museum_service.view_all_exhibits()
        elif user_choice == "8":
            museum_service.filter_exhibits()
        elif user_choice == "0":
            print("Вихід")
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main_menu()
