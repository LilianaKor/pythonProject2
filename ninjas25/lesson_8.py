
class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
