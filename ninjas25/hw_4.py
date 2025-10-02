"""
Create a Python program that simulates a speeding ticker system. The program should take the driver
('s speed as input and number of offenses
If the driver is not overspeeding (i.e., over_speed <= 0),' print "You are driving within the speed Limit."

If the driver is speeding between 30 ( inclusive)and 50 '( inclusive) m/h above the limit: For the first offense,
 print "First time offender. You pay $100.”
For 'the second offense, print "Second time offender. You pay $150."
for the third offense, print "Third time 'offender. You pay $250.”

For the fourth or more offenses, print "Fourth time offender, License suspended."
 'If the driver is speeding less than 30 m/h above the limit, print "warning issued."
 If the driver is speeding more 'than 50 m/h above the limit, print "Over 50 m/h. above speed Limit. "
 License suspended." speed_limit= 90)
 """

# speed_limit = 90

# speed = int(input("Введите скорость водителя (миль/ч): "))
# offenses = int(input("Введите количество прошлых нарушений: "))
# over_speed = speed - speed_limit
#
# if over_speed <= 0:
#     print("You are driving within the speed Limit.SO Yoy are safe.")
# elif 30 <= over_speed <= 50:
#     if offenses == 1:
#         print("First time offender. You pay $100. Please be careful.")
#     elif offenses == 2:
#         print("Second time offender. You pay $150. What happens?")
#     elif offenses == 3:
#         print("Third time offender. You pay $250. Again, please be careful.")
#     else:
#         print("Fourth time offender, License suspended. Go to court.")
# elif over_speed < 30:
#     print("warning issued.")
# elif over_speed > 50:
#     print("Over 50 m/h. above speed Limit. License suspended."
#           "Speed-limit= 90")


# Task 1
# Продвинутый sum.
# Встроенная функция sum() в python вызывает ошибку, если один из элементов последовательности не является числом,
# например sum([1, 2, 'A']).
# Напишите функцию sum_ignore_non_numbers(), которая имеет один параметр items (список или кортеж).
# Функция должна вернуть сумму всех чисел (int, float) в переданной последовательности. При этом все нечисловые значения
# должны игнорироваться.
# Если чисел нет, то функция должна вернуть 0.
# Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3


# def sum_ignore_non_numbers(item):
#     total = 0
#     for i in item:
#         if isinstance(i, (int, float)):
#             total += i
#     return total
#
# print(sum_ignore_non_numbers(['Hi' 'Hey', None, 'GHFHFHF']))


# Task 2
# Треугольник.
# Треугольник возможен, если сумма любых двух его сторон больше длины третьей стороны.
# Напишите функцию is_triangle(), которая имеет 3 параметра - длины сторон треугольника.
# Функция должна возвращать True, если треугольник с переданными сторонами может существовать, и False в противном случае.
# Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True.

# Option 1
# def is_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
# print(is_triangle(3, 4, 5))


# Option 2
# def is_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a
# print(is_triangle(3, 4, 5))


# Task 3
# Среднее значение.
# Напишите функцию average(), которая принимает произвольное количество позиционных аргументов. (Можно передать любое число аргументов).
# Функция должна посчитать среднее арифметическое всех переданных чисел. (Представим, что в функцию передаются только числа).
# Если не передать ни одного аргумента, то функция должна вернуть 0.
# Такой вызова функции average(1, 2, 3, 4, 5, 6, 7, 8) должен вернуть 4.5

# Option 1
# def average(*args):
#     if not args:
#         return 0
#     result = sum(args) / len(args)
#     return result
# print(average(1, 2, 3, 4, 5, 6, 7, 8))
#
#
# # # Option 2
# def average(*args):
#
#     return sum(args) / len(args) if args else 0

# print(average(1, 2, 3, 4, 5, 6, 7, 8))


# Task 4
# Общие строки.
# Напишите функцию common_strings(), которая имеет 3 параметра: list1, list2 и iqnore_case=True (значение по умолчанию).
# Функция должна вернуть новых список из тех значений, которые встречаются в обоих списках. При этом, если ignore_case равен True,
# то функция должна игнорировать регистр и считать строки "string" и "STRING" одинаковыми.  В противном случае функция должна
# учитывать регистр символов и считать такие строки разными.
# Все строки в результирующем списке должны быть в нижнем регистре.
# Например, существуют 2 списка:
# fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
# fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
# То вызов функции common_strings(fruits_1, fruits_2) должен вернуть ['apple', 'cherry'].


# def common_strings(list1, list2, ignore_case = True):
#     total = []
#     for i in list1:
#         for j in list2:
#             if ignore_case and i.lower() == j.lower():
#                 total.append(j.lower())
#             if not ignore_case and i == j:
#                 total.append(j.lower())
#
#     return total
#
# print(common_strings(['banana', "APPLE", 'watermelon', 'cherry'], ['Mango', 'apple', 'orange', 'cherry']))


# Task 5
# КаКоЕ-тО вОлНеНиЕ.
# Создать переменную text, значение которой определяется через ввод данных с клавиатуры.
# Каждый символ под четным индексом должен быть переведен в верхний регистр, а каждый нечетный в нижний.
# Вывести полученную строку на экран.
# Если была введена строка "Чтобы продать что-нибудь ненужное, нужно сначала купить что-нибудь ненужное, а у нас денег нет.",
# то результат должен быть  "ЧтОбЫ ПрОдАтЬ ЧтО-НиБуДь нЕнУжНоЕ, нУжНо сНаЧаЛа кУпИтЬ ЧтО-НиБуДь нЕнУжНоЕ, а у нАс дЕнЕг нЕт."


text = input('Enter your text: ')
result = ''

for i in range(len(text)):
    if i % 2 == 0:

        result += text[i].upper()
    else:
        result += text[i]

print(result)
