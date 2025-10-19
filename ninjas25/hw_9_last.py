"""
Регистрация (часть 1)

1. Напишите функцию registration(), которая принимает 2 аргумента -
username (строка) и password() (строка)
2. Функция должна проверить username, а именно:
a. username является строкой.
b. Длина этой строки минимум 4 символа и максимум 15.
c. username состоит только из букв.
3. Если username некорректный, то функция должна вызвать исключение
ValueError.
4. Функция должна проверить password, а именно:
a. password является строкой.
b. Длина этой строки минимум 8 символов и максимум 45.
c. password состоит только из букв и цифр.
5. Если password некорректный, то функция должна вызвать исключение
ValueError.
6. Если “регистрация” прошла успешно, то функция должна вернуть True.

Дополнительно: создайте свой тип исключения RegistrationError и используйте
его вместо ValueError.
"""


class RegistrationError(Exception):
    pass


def registration(username, password):
    if not (isinstance(username, str) and 4 <= len(username) <= 15 and username.isalpha()):
        raise RegistrationError('username incorrect')

    if not (isinstance(password, str) and 8 <= len(password) <= 45 and password.isalnum()):
        raise RegistrationError('password incorrect')
