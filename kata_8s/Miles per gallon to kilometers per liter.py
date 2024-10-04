# Description:
# Sometimes, I want to quickly be able to convert miles per imperial gallon (mpg) into kilometers per liter (kpl).
#
# Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).
#Make sure to round off the result to two decimal points.
#Some useful associations relevant to this kata:
#1 Imperial Gallon = 4.54609188 litres
# 1 Mile = 1.609344 kilometres

def converter(mpg):
    miles_to_kilometres = 1.609344
    galon_to_litres = 4.54609188
    kpl = (mpg * miles_to_kilometres) / galon_to_litres
    kpl = round(kpl, 2)
    return kpl


def converter(mpg):
    # Constants for conversion
    miles_to_km = 1.609344
    gallon_to_liter = 4.54609188

    # Conversion from mpg to kpl
    kpl = (mpg * miles_to_km) / gallon_to_liter

    # Rounding to two decimal places
    return round(kpl, 2)


def converter1(mpg):
    # Constants for conversion
    miles_to_km = 1.609344
    gallon_to_liter = 4.54609188

    # Conversion from mpg to kpl
    kpl = (mpg * miles_to_km) / gallon_to_liter

    # Rounding to two decimal places
    return round(kpl, 2)


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


