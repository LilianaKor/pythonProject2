# 1. To reversea a string

string = "offer"


# def reverse(string):
#     return ''.join(reversed(string))
#
#
# print(reverse(string))


def reverse_string(s: str) -> str:
    result = ''
    for char in s:
        result = char + result
    return result


print(reverse_string(string))


# 2. To check if a string is a palindrome

def is_palindrome(s):
    return s == s[::-1]
