def filter_string(st):
    num = ""
    for i in st:
        if i.isdigit():
            num += i

    return int(num)

# def filter_string(string):
#     return int(''.join(filter(str.isdigit, string)))
#
#
# def filter_string(string):
#     rez = ""
#     for i in string:
#         if i >= '0' and i <= '9':
#             rez = rez + i
#     return int(rez)
#
# def filter_string(string):
#     return int("".join([num for num in string if num in "0123456789"]))
#
# def filter_string(string):
#     res=""
#     for i in string:
#         if i in "1234567890" :
#             res= res + i
#     return int(res)

# The number has been mixed up with the text. Your goal is to retrieve the number from the text, can you return
# the number back to its original state?
# Task ----  Your task is to return a number from a string.
# Details ---- You will be given a string of numbers and letters mixed up, you have to return all the numbers
# in that string in the order they occur.

