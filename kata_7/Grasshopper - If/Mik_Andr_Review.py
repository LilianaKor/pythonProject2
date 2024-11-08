#START, STOP, STEP  – >> (-1, -1, -1)


def convert_mpg_to_kmpl(mpg):
    # Константы для конвертации
    gallons_to_liters = 4.54609188
    miles_to_kilometers = 1.609344

    # Конвертация mpg в kmpl
    kmpl = (mpg * miles_to_kilometers) / gallons_to_liters

    # Округление до двух знаков после запятой
    return round(kmpl, 2)


# Пример использования:
mpg_input = float(input("Введите мили на имперский галлон: "))
kmpl_output = convert_mpg_to_kmpl(mpg_input)
print(f"{mpg_input} MPG это {kmpl_output} KM/L")

from functools import reduce

ls = list(range(0, 101))
get_sum_of_even = lambda x: sum(num for num in x if num % 2 == 0)
# get_sum_of_even2 = reduce(lambda x, y: x + y, (num for num in ls if num % 2 == 0))
a = "bsj123cbsd2232jvcbajb223jasbcsjcjsdbcvdjbvdfjbvr3432ueuu3ufheufh"
d = {
    k: a.count(k) for k in a if k.isalpha()
}
# d2 = {}
#
for char in a:
    if d.get(char):  # get and d[char]
        d[char] += 1
    else:
        d[char] = 1
for k, v in d.items():
    if v == 10:
        print(k)
        break
print(d)
# x = lambda word: word in a
# print(x("asb"))


solution = lambda s: "".join(s[num] for num in range(len(s) - 1, -1, -1))
from functools import reduce

ls = list(range(0, 101))
get_sum_of_even = lambda x: sum(num for num in x if num % 2 == 0)
# get_sum_of_even2 = reduce(lambda x, y: x + y, (num for num in ls if num % 2 == 0))
a = "bsj123cbsd2232jvcbajb223jasbcsjcjsdbcvdjbvdfjbvr3432ueuu3ufheufh"
d = {
    k: a.count(k) for k in a if k.isalpha()
}
# d2 = {}
#
for char in a:
    if d.get(char):  # get and d[char]
        d[char] += 1
    else:
        d[char] = 1
for k, v in d.items():
    if v == 10:
        print(k)
        break
print(d)
# x = lambda word: word in a
# print(x("asb"))
