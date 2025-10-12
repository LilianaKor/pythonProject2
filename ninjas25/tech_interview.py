# 1. To reversea a string

# string = "offer"


# def reverse(string):
#     return ''.join(reversed(string))
#
#
# print(reverse(string))


# def reverse_string(s: str) -> str:
#     result = ''
#     for char in s:
#         result = char + result
#     return result
#
#
# print(reverse_string(string))


# 2. To check if a string is a palindrome
# string = "civic"
# def is_palindrome(s):
#     return s == s[::-1]
#
# print(is_palindrome(string))


# 3.  Count vowels in a string   Task: Count how many vowels (a, e, i, o, u) are in a string.
# def count_vowels(s):
#     return sum(c in 'aeiou' for c in s.lower())
#
# print(count_vowels("Hello"))

# def count_vowels(s):
#     return sum(1 for char in s.lower() if char in 'aeiou')
#
# print(count_vowels("apricot"))


# 4. Подсчёт повторяющихся символов в строке

# def count_duplicates(s):
#     return len(s) - len(set(s))
#
# print(count_duplicates("Hello"))

from collections import Counter


# def count_chars(s):
#     return Counter(s)
#
# print(count_chars("Hello"))

# 5. убрать дубликаты, объединить массивы и отсортировать их в порядке возрастания:
# arr1 = [2, 5, 1, 6, 6, 8]
# arr2 = [5, 6, 3, 4, 6, 1]
#
# merged_sorted = sorted(set(arr1 + arr2))
# print(merged_sorted)

# or – Решение без set():
# arr1 = [2, 22, 9, 5, 1, 6, 6, 8]
# arr2 = [5, 6, 22, 3, 4, 1, 2, 1, 3, 6, 1]
# # Шаг 1: Объединяем массивы
# merged = arr1 + arr2
# # Шаг 2: Убираем дубликаты вручную
# unique = []
# for num in merged:
#     if num not in unique:
#         unique.append(num)
# # Шаг 3: Сортируем (используем встроенный sorted или ручную сортировку)
# sorted_unique = sorted(unique)
# print(sorted_unique)

# 6.  Write a short program that prints each number from 1 to 100 on a new line.
#  For each multiple of 3, print "Fizz" instead of the number.
#  For each multiple of 5, print "Buzz" instead of the number.
#  For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number. Напишите короткую программу,
# которая выводит каждое число от 1 до 100 на новой строке.
#  Для каждого числа, кратного 3, выведите «Fizz» вместо числа.
#  Для каждого числа, кратного 5, выведите «Buzz» вместо числа.
#     Для чисел, кратных как 3, так и 5, выведите «FizzBuzz» вместо числа.

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")  # Multiple of both 3 and 5
#
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# 7. Find the maximum number in a list

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_num = max(my_list)
# print(max_num)

#  or without using max()
def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


# 8. Generate Fibonacci sequence    Task: Print the first n numbers of the Fibonacci sequence.
