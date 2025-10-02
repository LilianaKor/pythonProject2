# Напишите функцию, которая будет возвращать все простые делители числа.

# def number(param):
#     list1 = []
#     F = True
#
#     for i in range(2, param + 1):
#         if param % i == 0:
#             for del1 in range(2, i):
#                 if i % del1 == 0:
#                     F = False
#             if F == True:
#                 list1.append(i)
#
#     print('Простые делители числа', param, 'составляют', list1)

# number(6)
#
# Напишите функцию, которая будет принимать число и возвращать True, если это число является
# числом фибоначчи иначе она должна вернуть False.

# Task 3. Fibonacci Sequence (loops, logic)
# Tasks: Print the first 10 numbers of the Fibonacci sequence. Expected output: 0 1 1 2 3 5 8 13 21 34


# a = 0
# b = 1
# my_list = [a, b]
# print(my_list)
#
# while len(my_list) < 10:
#     new_sum = a + b
#     my_list.append(new_sum)
#     a = b
#     b = new_sum
# print(my_list)

# def is_fibonacci(n):
#     first = 0
#     second = 1
#
#     if n == 0 or n == 1:
#         return True
#
#     for i in range(2, 100):
#         temp = first + second
#         if temp == n:
#             return True
#         elif temp > n:
#             return False
#         first = second
#         second = temp
#
#
# print(is_fibonacci(8))


def fibonacci(n):
    my_first = 0
    my_second = 1

    if n == 0 or n == 1:
        return True

    for i in range(2, 100):
        next_fib = my_first + my_second
        if next_fib == n:
            return True
        elif next_fib > n:
            return False
        my_first = my_second
        my_second = next_fib

    return False


print(fibonacci(3))

# Создайте функцию, которая будет проверять, правильно ли расставлены скобки. Пример:
# (()())True
# ())(False

# def brackets(s):
#     count = 0
#     for i in s:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0


# print(brackets("(()())"))

# Напишите функцию, которая будет проверять, является ли слово палиндромом.
# word = "12321"
# reversed_word = word[::-1]
# print(word == reversed_word)
