import re


def validate_usr(username):
    print(username)
    pattern = r'[a-z0-9_]{4,16}'
    x = re.fullmatch(pattern, username)

    print(x)
    return bool(x)
