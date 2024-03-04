import re
def lowercase_count(strng):
    # Your code here
    pattern = r'[a-z]'
    x = re.findall(pattern, strng)
    return len(x)

def lowercase_count(strng):
    return sum(a.islower() for a in strng)

import re
def lowercase_count(string):
    return len(re.findall('[a-z]',string))

lowercase_count = lambda s: sum(e.islower() for e in s)

# Your task is simply to count the total number of lowercase letters in a string.
#
# Examples
# "abc" ===> 3
# "abcABC123" ===> 3
# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
# "" ===> 0;
# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
# "abcdefghijklmnopqrstuvwxyz" ===> 26

