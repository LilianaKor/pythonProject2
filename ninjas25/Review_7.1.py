"""
Class work
Создайте класс Book с атрибутами title, author, pages. Добавьте метод info(), который выводит строку “Книга: …, Автор:
 …, Страниц: …”
Создайте класс BancAccount с атрибутами owner, balance и методами deposit(amount) - пополнение счёта, withdraw(amount)
- снятие денег со счёта (не забудьте проверить, что баланс положительный), info() - выводит полную информацию об аккаунте.
Создайте класс Student с атрибутами name, grades (список с оценками). Создайте 2 метода: add_grade(grade) - добавить
 оценку, averege() - возвращает средний балл.
Создайте класс Calculator с атрибутом value (по умолчанию 0). Создайте методы add(x) - прибавить число, sub(x) -
вычесть число, mul(x) - умножить на число, div(x) - разделить на число (с проверкой на 0) и show() - выводит текущее значение.
Home work
Создайте класс Grocery с атрибутом items - список покупок и методами  add_item - добавить предмет, remove_item - удалить
предмет, show_items - вывести список покупок.
Создайте класс TrafficLight с атрибутом color ( изначально red) и методом switch(), который меняет цвета по кругу, а
акже методом show(), который выводит текущий цвет.
Создайте класс Lamp с атрибутом is_on (включена ли лампа) и методами turn_on() - включить лампу, turn_off() - выключить
 лампу, toggle() - переключить лампу (если была включена - выключить, если выключена - включить) и status() - вывести
 Лампа включена” или “Лампа выключена”
Дополнительные задачи
Создайте класс Thermometer должен хранить температуру в Цельсиях (как основную) и методы: set_temp_c(c) — установить
температуру в Цельсиях. set_temp_f(f) — установить температуру в Фаренгейтах (внутри пересчитывается в °C). get_temp_c()
— вернуть температуру в Цельсиях. get_temp_f() — вернуть температуру в Фаренгейтах. show() — вывести температуру в обеих
 шкалах. F = 95  C + 32, С =59 (F - 32)

"""


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def info(self):
#         print(f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}")
#
#
# book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
# book.info()


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Недостаточно средств")
#
#     def info(self):
#         print(f"Владелец: {self.owner}, Баланс: {self.balance}")
#
#
# account = BankAccount("John Doe", 1000)
# account.deposit(1500)
# account.withdraw(800)
# account.info()


# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def averege(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student = Student("Alice", [90, 95, 81, 99, 85])
# student.add_grade(95)
# print(student.averege())


# class Calculator:
#     def __init__(self, value=0):
#         self.value = value
#
#     def add(self, x):
#         self.value += x
#
#     def sub(self, x):
#         self.value -= x
#
#     def mul(self, x):
#         self.value *= x
#
#     def div(self, x):
#         if x == 0:
#             raise ValueError("Division by zero")
#         self.value /= x
#
#     def show(self):
#         print(self.value)
#
#
# calculator = Calculator()
# calculator.add(5)
# calculator.sub(2)
# calculator.mul(3)
# calculator.div(2)
# calculator.show()