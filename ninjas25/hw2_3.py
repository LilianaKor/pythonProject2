




# ---------------- Задача 1 ----------------   Посмотрите на следующие переменные:
# 1num = 100
# имя = “Алексей”
#  First_Number = 1
# “Мой текст” = text
# phone_number = “Hi!”
# Что с ними не так? Как бы вы их исправили?

num = 100
name = "Алексей"
first_number = 1
text = "Мой текст"
message = "Hi!"


# ---------------- Задача 2 ----------------

name = "Саша"

# Способ 1
print(f"Привет, меня зовут {name}.")

# Способ 2
message = "Привет, меня зовут" + " " + name + "."

print(message)


# ---------------- Задача 3 ----------------3
# Создать переменную name, значение которой определяется через ввод данных с клавиатуры.
# Создать переменную surname, значение которой определяется через ввод данных с клавиатуры.
# Вывести на экран строку "Привет, меня зовут <имя> <фамилия>.". Значение переменных name и surname должно быть
# отформатировано  к корректному виду. Например, если с клавиатуры вводятся строки "еЛеНА" и "поПОВА", то результат
# должен быть "Привет, меня зовут Елена Попова."

name = input()
surname = input()

print(f"Привет, меня зовут {name.title()} {surname.title()}.")


# ---------------- Задача 4 ----------------
a = input()
b = input()
result = int(a) + int(b)

print(result)


# print numbers coding challenge - easy level 2025

#as a column (0 - 9)
for number in range(10):
    print(number)

# as a column (1 - 10)
for number in range(1, 10 + 1):
    print(number)

#in a row, with coma
for number in range(1, 10 + 1):
    print(number, end=', ')

#in a row, separeted by coma, ends with full stop
limit = 12 #can be any number
for number in range(1, limit + 1):
    if number == limit:
        print(number, end='.')
    else:
        print(number, end=', ')