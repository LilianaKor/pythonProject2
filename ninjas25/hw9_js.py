"""
1: Fibonacci Sequence
Task: Given a non-negative integer n, return the nth Fibonacci number.
F0 = 0 and F1 = 1.
Example:
n = 6 → 8
function fib(n) {
}
2. Sum All Numbers in a Messy String
Task:
Given a string that mixes letters and numbers, extract all numbers and return their sum.
Numbers can be integers like 7 or decimals like 1.5. Sometimes “…” means a decimal point.
Example:
"jshs7Jsh3shhs1.5hdhdje1…5dhdh" → 13
function sumNumbersFromString(s) {
}
3. Recursion with Fibonacci
Task:
Write two versions:
	fibRecursive(n) → use recursion
	fibMemo(n) → same but with memoization
Example:
fibRecursive(5) → 5
fibMemo(30) → 832040
function fibRecursive(n) {
}
function fibMemo(n, memo = {}) {
}
4. Longest Subarray with No Repeating Numbers
Task:
Given an array, return the longest contiguous subarray with unique values.
Input:
[7, 6, 52, 372, 7, 6, 52627, 22, 348, 2, 6, 5, 7, 6]
Output:
[52, 372, 7, 6, 52627, 22, 348, 2]
function longestUniqueSubarray(arr) {
}
5. Factorial
Task:
Return factorial of n (product of all numbers from 1 to n).
Example:
5! → 120
function factorial(n) {
}
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1  # a = F_{k-1}, b = F_{k}
    for _ in range(2, n + 1):  # мы запускаем цикл n раз, но значение индекса неважно, поэтому используем _ как
        # мусорную переменную чтобы показать намерение переменная не используется
        a, b = b, a + b
    return b


print(fib(6))  # 8

import re


def sumNumbersFromString(s: str) -> float:
    s = s.replace("…", ".")  ## заменим юникодное многоточие на точку
    return sum(
        map(float, re.findall(r'\d+(?:\.\d+)?', s)))  # ищет: \d+ → цифры, (?:\.\d+)? → необязательную десятичную часть.


print(sumNumbersFromString("jshs7Jsh3shhs1.5hdhdje1…5dhdh"))  # 13 =7 + 3 + 1.5 + 1.5


# map(function, iterable) применяет функцию к каждому элементу последовательности (списка, строки, множества и т. д.)
# и возвращает итерируемый объект (map object).


# import re
#
#
# def sumNumbersFromString(s: str) -> float | int:
#     # заменяем все виды многоточия на точку
#     s = s.replace("…", ".").replace("...", ".")
#
#     # находим числа (целые и с десятичной частью)
#     numbers = re.findall(r"\d+(?:\.\d+)?", s)
#
#     total = sum(map(float, numbers))
#
#     # если сумма целая → вернуть int
#     return int(total) if total.is_integer() else total
#
#
# # Examples
# print(sumNumbersFromString("jshs7Jsh3shhs1.5hdhdje1…5dhdh"))  # 13
# print(sumNumbersFromString("abc10xyz20.5def"))  # 30.5
# print(sumNumbersFromString("aa3bb2...7cc"))  # 12


def fibRecursive(n: int) -> int:  # Эта функция считает число Фибоначчи с индексом n
    if n <= 1:
        return n
    return fibRecursive(n - 1) + fibRecursive(n - 2)


# пример
print(fibRecursive(5))  # 5

"""
ibRecursive(5)

Вызов: fibRecursive(5)
→ не базовый случай, поэтому:
= fibRecursive(4) + fibRecursive(3)

Раскроем fibRecursive(4)
= fibRecursive(3) + fibRecursive(2)

Раскроем fibRecursive(3)
= fibRecursive(2) + fibRecursive(1)

Подставим в уравнение:
fibRecursive(5)
= (fibRecursive(3) + fibRecursive(2)) + (fibRecursive(2) + fibRecursive(1))

Ещё дальше:

fibRecursive(2) = fibRecursive(1) + fibRecursive(0) = 1 + 0 = 1

fibRecursive(1) = 1

fibRecursive(0) = 0

Теперь всё складываем:

fibRecursive(2) = 1

fibRecursive(3) = fibRecursive(2) + fibRecursive(1) = 1 + 1 = 2

fibRecursive(4) = fibRecursive(3) + fibRecursive(2) = 2 + 1 = 3

fibRecursive(5) = fibRecursive(4) + fibRecursive(3) = 3 + 2 = 5"""


def longest_unique_subarray(arr):
    last_index = {}  # значение -> последний индекс
    start = 0  # начало текущего окна
    best_start, best_len = 0, 0

    for i, v in enumerate(arr):
        # если значение уже встречалось в текущем окне → двигаем start
        if v in last_index and last_index[v] >= start:
            start = last_index[v] + 1

        last_index[v] = i

        # проверяем длину текущего окна
        length = i - start + 1
        if length > best_len:
            best_len = length
            best_start = start

    return arr[best_start:best_start + best_len]


# пример
data = [7, 6, 52, 372, 7, 6, 52627, 22, 348, 2, 6, 5, 7, 6]
print(longest_unique_subarray(data))
#  [52, 372, 7, 6, 52627, 22, 348, 2]
"""
7 → уникален → окно [7].

6 → уникален → окно [7, 6].

52 → уникален → окно [7, 6, 52].

372 → уникален → окно [7, 6, 52, 372].

Снова 7 (уже есть!) → сдвигаем начало за старый 7.
Новое окно: [52, 372, 7].

Добавляем 6 → [52, 372, 7, 6].

Добавляем 52627 → [52, 372, 7, 6, 52627].

Добавляем 22 → [52, 372, 7, 6, 52627, 22].

Добавляем 348 → [52, 372, 7, 6, 52627, 22, 348].

Добавляем 2 → [52, 372, 7, 6, 52627, 22, 348, 2]. ✅ Длина 8.

Дальше идёт 6 (повтор) → окно сдвигается. Теперь оно [52627, 22, 348, 2, 6].

Потом 5 → [52627, 22, 348, 2, 6, 5].

Потом 7 → [52627, 22, 348, 2, 6, 5, 7].

Потом 6 снова → повтор, окно сокращается"""


# factorial(0) по определению = 1
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))  # 120

# recursive factorial
def recursive_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)


print(recursive_factorial(5))


# math.factorial
import math

print(math.factorial(5))  # 120
print(math.factorial(0))  # 1
print(math.factorial(10))  # 3628800
