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
