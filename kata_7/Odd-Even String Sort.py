def sort_my_string(s):
    return s[::2] + ' ' + s[1::2]


def sort_my_string1(str):
    evenChar = str[::2]
    oddChar = str[1::2]

    return evenChar + ' ' + oddChar