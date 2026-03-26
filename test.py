# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f"Ім’я: {self.name}, вік: {self.age}")


# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.


class Student:
    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age

    def print_info(self):
        print(f"Ім’я: {self.student_name}, вік: {self.student_age}")


students_list = []

for student_index in range(3):
    print(f"Введіть дані для студента №{student_index + 1}:")
    entered_name = input("Ім'я: ")
    entered_age = int(input("Вік: "))

    new_student = Student(entered_name, entered_age)
    students_list.append(new_student)

print("Інформація про студентів:")
for student in students_list:
    student.print_info()

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола
