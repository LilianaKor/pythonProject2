# Регистрация (часть 1)
#
# 1. Напишите функцию registration(), которая принимает 2 аргумента - username (строка) и password() (строка)
# 2. Функция должна проверить username, а именно: username является строкой.
#  Длина этой строки минимум 4 символа и максимум 15. username состоит только из букв.
# 3. Если username некорректный, то функция должна вызвать исключение ValueError.
# 4. Функция должна проверить password, а именно: password является строкой.
#  Длина этой строки минимум 8 символов и максимум 45.
#  password состоит только из букв и цифр.
# 5. Если password некорректный, то функция должна вызвать исключение ValueError.
# 6. Если “регистрация” прошла успешно, то функция должна вернуть True.
#
# Дополнительно: создайте свой тип исключения RegistrationError и используйте
# его вместо ValueError.



class RegistrationError(Exception):  # create custom - all exceptions must inherit from Exception
    pass


def registration(username, password):
    if not (isinstance(username, str) and 4 <= len(username) <= 15 and username.isalpha()):  # str validation
        raise RegistrationError('username incorrect')

    if not (isinstance(password, str) and 8 <= len(password) <= 45 and password.isalnum()): # str, int validation
        raise RegistrationError('password incorrect')

    return True


try:
    print(registration('user', '12345678'))
except RegistrationError as e:
    print(e)

try:
    print(registration('us', '123456789'))
except RegistrationError as e:
    print(e)

"""
Регистрация (часть 2) - Напишите программу, которая в бесконечном цикле запрашивает у
пользователя ввести логин и пароль и сохраняет их в соответствующие
переменные.
- Вызовите функцию registration из предыдущей задачи передав ей введенные логин и пароль пользователя.
- Если в registration были переданы некорректные данные, то ваша
программа должна перехватить вызванное функцией исключение
RegistrationError и написать в консоль “Ошибка регистрации!”, а затем снова попросить пользователя ввести данные.
- Если данные были введены корректно, то программа должна вывести “Успешно!” и выйти из бесконечного цикла."""

while True:
    username = input('Enter username: ')
    password = input('Enter password: ')
    try:
        if registration(username, password):
            print('Success!')
            break
    except RegistrationError:
        print('Error registration!') # until the correct data is entered

"""
Дорогой дневник...
- Создайте пустой текстовый файл journal.txt
- Программа должна в бесконечном цикле запрашивать пользователя
ввести строку, которая является одним из режимов: “прочитать”, “записать”, “выйти”.
- Если пользователь ввел “записать”:
 Программа просит пользователя ввести еще одну строку, которая будет записана в файл.
 Программа дозаписывает эту строку в файл journal.txt c новой строки.

- Если пользователь ввел “прочитать”:
 Программа выводит на экран все содержимое файла journal.txt.
- Если пользователь ввел “выйти”:
Программа пишет в консоль “Еще увидимся!”, выходит из бесконечного цикла и завершается.
- Если пользователь ввел что-то другое: Программа ничего не делает, просто возвращается к следующей
итерации бесконечного цикла."""
