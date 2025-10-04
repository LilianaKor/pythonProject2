"""
Домашнее задание (Занятие 7)
1
Прямоугольник
Создайте класс Rectangle, который принимает ширину и высоту прямоугольника при создании и должен иметь соответствующие атрибуты width и height (целые числа).
Создайте метод area(), который возвращает площадь прямоугольника.
Создайте метод perimeter(), который возвращает периметр прямоугольника.
Пример:
rect = Rectangle(2, 4)
a = rect.area() # Вернул 8
p = rect.perimeter() # Вернул 12

2
Автомобиль
Создайте класс Car, который принимает марку автомобиля (make) в виде строки и максимально возможную скорость (max_speed)
 в виде целого числа при создании. Также при инициализации (в теле __init__) экземпляра Car должен быть автоматически
 создан атрибут speed, равный 0 (текущая скорость автомобиля).

Создайте метод display_speed(), который выводит в консоль текущую скорость автомобиля.
Создайте метод accelerate(), который увеличивает скорость автомобиля на 10, при этом скорость автомобиля не должна
превышать max_speed, если вызывается accelerate() при максимальной скорости, то скорость не должна увеличиваться.
Создайте метод brake(), который уменьшает скорость автомобиля на 10, при этом скорость автомобиля не может быть меньше 0.
Если вызывается метод brake() при скорости равной 0, то скорость не должна уменьшаться.
Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 3


Повторение прошлого материала. Ответьте на следующие вопросы:Что такое and, or и not? Приведите пример их использования.
Что такое цикл? Чем отличается for от while? Что такое функция? Зачем она нужна?

      LeetcodeFizzBuzz Task Description:

Write a program that prints the numbers from 1 to 100, but:
For numbers divisible by 3, print "Fizz" instead of the number.
For numbers divisible by 5, print "Buzz" instead of the number.
For numbers divisible by both 3 and 5, print "FizzBuzz".
For all other numbers, print the number itself.

FizzBuzzWoof rules:

If a number is divisible by 3, print "Fizz".
If divisible by 5, print "Buzz".
If divisible by 7, print "Woof".
If divisible by multiple numbers, concatenate the words (e.g., 15 → "FizzBuzz", 21 → "FizzWoof", 105 → "FizzBuzzWoof").
Otherwise, print the number itself.

"""

# def fizzbuzzwoof(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#             print("FizzBuzzWoof")
#         elif i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0 and i % 7 == 0:
#             print("FizzWoof")
#         elif i % 5 == 0 and i % 7 == 0:
#             print("BuzzWoof")
#         elif i % 5 == 0:
#             print("Buzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 7 == 0:
#             print("Woof")
#         else:
#             print(i)


# fizzbuzzwoof(35)


# def fizzbuzzwoof(i):
#     if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#         return "FizzBuzzWoof"
#     elif i % 3 == 0 and i % 5 == 0:
#         return "FizzBuzz"
#     elif i % 3 == 0 and i % 7 == 0:
#         return "FizzWoof"
#     elif i % 5 == 0 and i % 7 == 0:
#         return "BuzzWoof"
#     elif i % 5 == 0:
#         return "Buzz"
#     elif i % 3 == 0:
#         return "Fizz"
#     elif i % 7 == 0:
#         return "Woof"
#     else:
#         return i
#
#
# print(fizzbuzzwoof(17))


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def display_info(self):
#         print(f"Width: {self.width}")
#         print(f"Height: {self.height}")
#         print(f"Area: {self.area()}") # Вернул 8
#         print(f"Perimeter: {self.perimeter()}") # Вернул 12
#
#
# rect = Rectangle(2, 4)
# rect.display_info()

# Создайте класс Car, который принимает марку автомобиля (make) в виде строки и максимально возможную скорость (max_speed)
#  в виде целого числа при создании. Также при инициализации (в теле __init__) экземпляра Car должен быть автоматически
#  создан атрибут speed, равный 0 (текущая скорость автомобиля).
#
# Создайте метод display_speed(), который выводит в консоль текущую скорость автомобиля.
# Создайте метод accelerate(), который увеличивает скорость автомобиля на 10, при этом скорость автомобиля не должна
# превышать max_speed, если вызывается accelerate() при максимальной скорости, то скорость не должна увеличиваться.
# Создайте метод brake(), который уменьшает скорость автомобиля на 10, при этом скорость автомобиля не может быть меньше 0.
# Если вызывается метод brake() при скорости равной 0, то скорость не должна уменьшаться.
# Пример:
# my_toyota = Car("Toyota", 180)
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.display_speed() # вывел в консоль 3
class Car:
    def __init__(self, make,  max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        self.speed = min(self.max_speed, self.speed + 10)

    def brake(self):
        self.speed = max(0, self.speed - 10)


my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 3