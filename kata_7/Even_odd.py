def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test the function
print(even_or_odd(5))  # Output: Odd
print(even_or_odd(10))  # Output: Even


def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'


def even_or_odd(number):
    return ["Even", "Odd"][number % 2]


even_or_odd = lambda number: "Odd" if number % 2 else "Even"
