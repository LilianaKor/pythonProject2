def get_count(sentence):
    sum = 0
    str = 'aeiou'
    for c in str:
        sum += sentence.count(c)
    return sum

def getCount(s):
    return sum(c in 'aeiou' for c in s)

def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))

def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])

# DESCRIPTION:
# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.
#
