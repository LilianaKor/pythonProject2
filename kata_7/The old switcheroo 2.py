def encode(string):
    str_ = ''
    for i in string.lower():
        if i.isalpha():
            str_ += str(ord(i) - 96)
        else:
            str_ += i

    return str_

def encode(string):
    return "".join(str(ord(ch) - 64) if ch.isalpha() else ch for ch in string.upper())

def encode(string):
    return ''.join(str(ord(c.upper())-64) if c.isalpha() else c for c in string)

def encode(string):
  return ''.join(str(ord(c)-96) if c.isalpha() else c for c in string.lower())

from string import ascii_lowercase as letters


def encode(string):
    return ''.join(str(letters.find(char)+1) if char in letters else char for char in string.lower())

import re

# def encode(string):
#     return re.sub('[a-z]', lambda x: str(ord(x.group()) - 96), string.lower())
#
# that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
#
# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'

