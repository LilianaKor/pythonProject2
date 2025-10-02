# ---------------- Задача 1 ----------------

def sum_ignore_non_numbers(items):
    """
    Суммирует числовые значения (int, float) в переданной последовательности.

    :param items: Последовательность объектов (tuple, list).
    :return: Сумма числовых значений (int или float). Если их нет, то возвращает 0.
    """

    total = 0

    for i in items:
        if isinstance(i, (int, float)):
            total += i

    return total


# ---------------- Задача 2 ----------------

def is_triangle(a, b, c):
    """
    Проверяет возможность существования треугольника по трем сторонам.

    :param a: Первая сторона треугольника.
    :param b: Вторая сторона треугольника.
    :param c: Третья сторона треугольника.
    :return: True, если треугольник возможен. Иначе False.
    """

    return (a + b) > c and (a + c) > b and (b + c) > a


# ---------------- Задача 3 ----------------

def average(*args):
    """
    Возвращает среднее арифметическое переданных чисел.

    :param args: Произвольное количество чисел (int или float).
    :return: Среднее арифметическое переданных чисел. Возвращает 0, если не переданы.
    """

    if not args:
        return 0

    return sum(args) / len(args)


# ---------------- Задача 4 ----------------

def common_strings(list1, list2, ignore_case=True):
    """
    Возвращает список из строк, которые находятся в обоих списках, приводя строки к нижнему регистру.

    :param list1: Первый список строк.
    :param list2: Второй список строк.
    :param ignore_case: Если True, то регистр игнорируется. Иначе учитывается.
    :return: Список из строк (приведенные к нижнему регистру), которые находятся в обоих списках.
    """

    if ignore_case:
        list1 = [i.lower() for i in list1]
        list2 = [i.lower() for i in list2]

    return [i.lower() for i in list1 if i in list2]


# ---------------- Задача из повторения ----------------

text = input() # "Hello"
result = ""

for i in range(len(text)): # (0, 1, 2, 3, 4)
    if i % 2:
        result += text[i].lower()
    else:
        result += text[i].upper()

print(result)


# -----------------------------------------
