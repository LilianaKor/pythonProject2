
class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount > 0:
            print("Недостаточно средств")
        else:
            self._balance -= amount

    def balance(self):
        return self._balance
