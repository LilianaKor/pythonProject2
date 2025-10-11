

def paperwork(n, m):
    if (n < 0 or m < 0):
        return 0
    else:
        total = n * m
        return total


def paperwork1(n, m):
    return n * m if n > 0 and m > 0 else 0


def paperwork2(n, m):
    if m < 0 or n < 0:
        return 0
    else:
        return n * m


def paperwork3(n, m):
    return max(n, 0) * max(m, 0)


def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m
