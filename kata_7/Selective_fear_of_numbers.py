# def am_I_afraid(day, num):
#     if day == "Monday":
#         return num == 12
#     elif day == "Tuesday":
#         return num > 95
#     elif day == "Wednesday":
#         return num == 34
#     elif day == "Thursday":
#         return num == 0
#     elif day == "Friday":
#         return num % 2 == 0
#     elif day == "Saturday":
#         return num == 56
#     elif day == "Sunday":
#         return abs(num) == 666
#
#     # If the day is not recognized, return False
#     return False
#
# # Test cases
# print(am_I_afraid("Monday", 12))  # Output: True
# print(am_I_afraid("Tuesday", 100))  # Output: True
# print(am_I_afraid("Wednesday", 34))  # Output: True
# print(am_I_afraid("Thursday", 0))  # Output: True
# print(am_I_afraid("Friday", 7))  # Output: False
# print(am_I_afraid("Saturday", 56))  # Output: True
# print(am_I_afraid("Sunday", -666))  # Output: True


# def am_I_afraid(day,num):
#     return {
#         'Monday':  num == 12,
#         'Tuesday': num > 95,
#         'Wednesday': num == 34,
#         'Thursday': num == 0,
#         'Friday': num % 2 == 0,
#         'Saturday': num ==  56,
#         'Sunday': num == 666 or num == -666,
#     }[day]

afraid = {
    'Monday': lambda x: x == 12,
    'Tuesday': lambda x: x > 95,
    'Wednesday': lambda x: x == 34,
    'Thursday': lambda x: x == 0,
    'Friday': lambda x: x % 2 == 0,
    'Saturday': lambda x: x == 56,
    'Sunday': lambda x: abs(x) == 666,
}

def am_I_afraid(day, num):
    return afraid[day](num)

