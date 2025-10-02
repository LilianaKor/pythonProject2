def sum_ignore_non_numbers(items):
    total = 0

    for i in items:
        if isinstance(i, (int, float)):
            total += i

    return total


def is_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a


def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)


def common_strings(list1, list2, ignore_case=True):
    if ignore_case:
        list1 = [i.lower() for i in list1]
        list2 = [i.lower() for i in list2]

    return [i.lower() for i in list1 if i in list2]
