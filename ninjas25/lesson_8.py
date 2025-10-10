class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            print("Недостаточно средств")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance


# 2
class OverdraftAccount(BankAccount):
    def withdraw(self, amount):
        self._balance -= amount

# 3  Ответьте на следующие вопросы:
# 1. Зачем нужен метод copy() у списка?
# 2. Что такое словарь и чем он отличается от списка или кортежа?
# 3. Как создается строка документации у функции?
# users = [
# {'id': 345324, 'name': 'Alice', 'age': 25},
# {'id': 1232, 'name': 123, 'age': 30},
# {'id': 7854, 'name': 'Bob', 'age': 22},
# {'id': 33412, 'name': None, 'age': 35},
# {'id': 78845, 'name': 'Charlie', 'age': 28},
# {'id': 45325, 'name': 'Eve', 'age': 40},
# {'id': 745633, 'name': True, 'age': 19},
# {'id': 64364, 'name': 'Frank', 'age': 33}
# ]
# Есть список пользователей users, где каждый пользователь представленсловарем с ключами id, name, и age. Некоторые
# пользователи могут иметь некорректное значение для ключа name. Под некорректным значениемпонимается любой тип, который
# не является строкой.
# - Создайте список ids, в который будут включены идентификаторы (id) тех пользователей, у которых значение по ключу
# name некорректно.  - Выведите список на экран.
# Ответ должен быть: [1232, 33412, 745633]


users = [
{'id': 345324, 'name': 'Alice', 'age': 25},
{'id': 1232, 'name': 123, 'age': 30},
{'id': 7854, 'name': 'Bob', 'age': 22},
{'id': 33412, 'name': None, 'age': 35},
{'id': 78845, 'name': 'Charlie', 'age': 28},
{'id': 45325, 'name': 'Eve', 'age': 40},
{'id': 745633, 'name': True, 'age': 19},
{'id': 64364, 'name': 'Frank', 'age': 33}
]
ids = []

for user in users:
    if not isinstance(user['name'], str):
        ids.append(user['id'])

print(ids)
