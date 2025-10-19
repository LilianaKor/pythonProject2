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
    s = s.replace("…", ".")   ## заменим юникодное многоточие на точку
    return sum(map(float, re.findall(r'\d+(?:\.\d+)?', s)))


print(sumNumbersFromString("jshs7Jsh3shhs1.5hdhdje1…5dhdh"))
