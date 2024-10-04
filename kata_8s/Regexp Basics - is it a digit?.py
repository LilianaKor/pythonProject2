import re


def is_digit(n):
    # your code here
    pattern = r'\d'
    x = re.findall(pattern, n)

    return bool(re.fullmatch(pattern, n))


import re


def is_digit1(n):
    return bool(re.match("\d\Z", n))


is_digit = lambda n: len(n) == 1 and n in "0123456789"


def is_digit2(n):
    return n.isdigit() and int(n) < 10

# DESCRIPTION:
# Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object
# is a digit (0-9), false otherwise.
