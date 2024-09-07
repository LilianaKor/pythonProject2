def stringy(size):
    return ''.join('1' if i % 2 == 0 else '0' for i in range(size))

# Examples
print(stringy(6))   # Output: '101010'
print(stringy(4))   # Output: '1010'
print(stringy(12))  # Output: '101010101010'


# Explanation:
# We loop through the range from 0 to size-1.
# For even indices (i % 2 == 0), we add '1'.
# For odd indices, we add '0'.
# Finally, we join all the characters together into a single string.
# This will always start with a '1' and alternate between '1' and '0'.

def stringy(size):
    res = ""
    for x in range(0, size):
        res += "1" if x % 2 == 0 else "0"
    return res

stringy = lambda size: ('10' * size)[:size]


def stringy(size):
    string = ""
    for num in range(size):
        if num % 2 == 0:
            string += "1"
        else:
            string += "0"
    return string
