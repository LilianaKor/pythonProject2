import math
import functools

#Round a off to three decimal places
# a = 10.04735
# result_1 = None
# result_1 = round(a,3)
# print(result_1)
#
# #Round up result_2 to greater value'
# result_2 = 5 /2 * 6 + 1.25 - 4
# print(result_2)
# result_2 = math.ceil(result_2)
# print(result_2)
#
# # Enter capital city of california state in lower case. Change the case to title case
# # #Save the result in result_co_capital variable'''
#
# result_ca_capital = 'sacramento'
# print(result_ca_capital.title())
# print(result_ca_capital.upper())
# print(result_ca_capital.lower())
# print(result_ca_capital.capitalize())
#
#
# #Enter the temperatute right now in Fahrenheit in the temperature_f variable in
# # a string (e.g. '75') and convert it to Celsius.
# #! Important you should save only number to result_temperature.
# #Formula (32F - 32) * 5/9 = 0C'''
#
# temperature_f = '75'
# #temperature_f = int(temperature_f)
# result_temperature =(int(temperature_f) - 32) * 5/9
# #print(round(result_temperature,2))
# print(math.floor(result_temperature))
#
# # Enter your first name and save it to first_name variable,
# #  then Enter last name and save it to last_name
# #  If first_name or last_name are shorter than 6 characters,
# #  save a full name (with space between) to result_3
# #  Else save first_name to result_3 as many times as length of last_name value'''
#
# first_name = input("input your first name:")
# last_name = input("input your last name:")
# result_3 = None
# if len(first_name) < 6 or len(last_name) < 6:
#     result_3 = f'{first_name} {last_name}'
# else:
#     result_3 = len(last_name) * first_name
# print(result_3)

#Enter a random string, which includes only digits.
#Write code which find a sum of digits in this string and save it
# into result_3 variable'''

string_number = input('Enter random digits: ')
result_4 = 0
#list_numbers = int(string_number)
#print(list_number)
#print(functools.reduce(lambda a, b: a+b, list_numbers))
# for digit in string_number:
#     result_4
# for char in string_number:
#     result_4 += int(char)
# print(result_4)


#distance = int(input('Enter distance traveled:'))


def taxi_fare(distance):
    total_fare = (distance * 1000 / 140) * 4
    return round(total_fare,2)

distance = int(input('Enter distance traveled:'))
print(taxi_fare(distance))

