import re


def validate_usr(username):
    print(username)
    pattern = r'[a-z0-9_]{4,16}'
    x = re.fullmatch(pattern, username)
    print(x)
    return bool(x)


def validate_usr1(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None


from re import fullmatch


def validate_usr2(username):
    return bool(fullmatch(r"[_0-9a-z]{4,16}", username))


import re
valid_username = re.compile(r"[a-z0-9_]{4,16}")


def validate_usr3(username):
    return bool(re.fullmatch(valid_username, username))

# DESCRIPTION:
# Write a simple regex to validate a username. Allowed characters are:
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).
