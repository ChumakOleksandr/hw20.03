from typing import Any

# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису


class Project:
    def __init__(self, project_name: str, total_budget: float):
        self.project_name = project_name
        self.total_budget = total_budget
        self.spent_money: float = 0.0
        self.is_completed = False
        self.total_duration_months: float = 0.0
        self.tasks_list: list[dict[str, Any]] = []

    def show_info(self):
        print(f"\nПроєкт: {self.project_name}")
        print(f"Кошторис: {self.total_budget} грн")
        print(f"Витрачено: {self.spent_money} грн")
        print(f"Статус: {'завершений' if self.is_completed else 'в процесі'}")
        print(f"Час виконання: {self.total_duration_months} міс")

        print("\nНеобхідні задачі:")
        if not self.tasks_list:
            print(" (немає задач)")
        else:
            for task in self.tasks_list:
                print(f" - {task['task_name']}")
                if task["subtasks"]:
                    print("    Під-задачі:")
                    for subtask in task["subtasks"]:
                        print(f"     • {subtask}")
        print()

    def add_task(self, task_name: str):
        task = {"task_name": task_name, "subtasks": [], "is_completed": False}
        self.tasks_list.append(task)
        print(f"Задачу '{task_name}' додано.")

    def split_task(self, task_name: str, subtasks_list: list[str]):
        for task in self.tasks_list:
            if task["task_name"] == task_name:
                task["subtasks"].extend(subtasks_list)
                subtasks_str = ", ".join(subtasks_list)
                print(f"Задачу '{task_name}' розбито на під-задачі: " f"{subtasks_str}")
                return

        print(f"Задачу '{task_name}' не знайдено!")

    def complete_task(self, task_name: str, months_spent: int, task_cost: float):
        if self.is_completed:
            print("Проєкт вже завершений!")
            return

        for task in self.tasks_list:
            if task["task_name"] == task_name:
                if task["is_completed"]:
                    print(f"Задача '{task_name}' вже виконана.")
                    return

                if self.spent_money + task_cost > self.total_budget:
                    available = self.total_budget - self.spent_money
                    print(
                        f"Недостатньо коштів! Потрібно {task_cost} грн, "
                        f"доступно {available} грн."
                    )
                    return

                task["is_completed"] = True
                self.spent_money += task_cost
                self.total_duration_months += months_spent

                print(
                    f"Задачу '{task_name}' виконано. "
                    f"Час: {months_spent} міс, витрати: {task_cost} грн."
                )

                if all(t["is_completed"] for t in self.tasks_list):
                    self.is_completed = True
                    print("Усі задачі виконані — проєкт завершено!")

                return

        print(f"Задачу '{task_name}' не знайдено!")

    def add_budget(self, added_amount: float):
        if added_amount <= 0:
            print("Сума повинна бути більшою за 0.")
            return

        self.total_budget += added_amount
        print(
            f"Кошторис поповнено на {added_amount} грн. "
            f"Новий бюджет: {self.total_budget} грн."
        )


project = Project("Створення веб‑порталу", 80000)

project.add_task("Розробка дизайну")
project.add_task("Верстка інтерфейсу")
project.add_task("Створення backend системи")

project.split_task("Розробка дизайну", ["UI макет", "UX структура", "Прототип"])
project.split_task("Створення backend системи", ["База даних", "API", "Авторизація"])

project.show_info()

project.complete_task("Розробка дизайну", months_spent=2, task_cost=20000)
project.complete_task("Верстка інтерфейсу", months_spent=1, task_cost=15000)

project.add_budget(10000)

project.complete_task("Створення backend системи", months_spent=3, task_cost=40000)

project.show_info()

# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
# Практичне завдання
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон


class Phone:
    def __init__(self, max_storage: int):
        self.max_storage = max_storage  # максимальна памʼять
        self.used_storage = 0  # зайнята памʼять
        self.is_turned_on = False  # стан телефону
        self.installed_apps: dict[str, int] = {}  # додатки

    def show_memory_info(self):
        free_space = self.max_storage - self.used_storage
        print(f"\nМаксимальна пам'ять: {self.max_storage} МБ")
        print(f"Використано: {self.used_storage} МБ")
        print(f"Вільно: {free_space} МБ")

        print("\nВстановлені додатки:")
        if not self.installed_apps:
            print(" (немає додатків)")
        else:
            for app_name, size in self.installed_apps.items():
                print(f" - {app_name}: {size} МБ")
        print()

    def install_app(self, app_name: str, app_size: int):
        if app_name in self.installed_apps:
            print(f"Додаток '{app_name}' вже встановлений.")
            return

        if self.used_storage + app_size > self.max_storage:
            free = self.max_storage - self.used_storage
            print(f"Недостатньо пам'яті! Потрібно {app_size} МБ, доступно {free} МБ.")
            return

        self.installed_apps[app_name] = app_size
        self.used_storage += app_size
        print(f"Додаток '{app_name}' встановлено ({app_size} МБ).")

    def delete_app(self, app_name: str):
        if app_name not in self.installed_apps:
            print(f"Додаток '{app_name}' не знайдено.")
            return

        removed_size = self.installed_apps.pop(app_name)
        self.used_storage -= removed_size
        print(f"Додаток '{app_name}' видалено. Звільнено {removed_size} МБ.")

    def update_app(self, app_name: str, new_size: int):
        if app_name not in self.installed_apps:
            print(f"Додаток '{app_name}' не встановлений.")
            return

        old_size = self.installed_apps[app_name]
        size_diff = new_size - old_size

        if size_diff > 0 and self.used_storage + size_diff > self.max_storage:
            print(f"Недостатньо пам'яті! Потрібно {size_diff} МБ додатково.")
            return

        self.installed_apps[app_name] = new_size
        self.used_storage += size_diff

        print(
            f"Додаток '{app_name}' оновлено. "
            f"Було: {old_size} МБ → Стало: {new_size} МБ."
        )
