def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

# Examples
print(basic_op('+', 4, 7))  # Output: 11
print(basic_op('-', 15, 18))  # Output: -3
print(basic_op('*', 5, 5))  # Output: 25
print(basic_op('/', 49, 7))  # Output: 7.0

def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2
    else:
        return "Invalid operation"


def basic_op(operator, value1, value2):
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '*':
            return value1 * value2
        case '/':
            return value1 / value2


def basic_op(operator, value1, value2):
    op = {
        '+': (value1 + value2),
        '-': (value1 - value2),
        '*': (value1 * value2),
        '/': (value1 / value2),
    }

    return op[operator]

