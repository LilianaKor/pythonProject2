def solution(start, finish):
    return sum(divmod(finish - start, 3))


def solution1(start, finish):
    return (finish - start) // 3 + (finish - start) % 3


def solution3(s, f):
    return int(((f - s) / 3) + ((f - s) % 3))


def solution4(s, f):
    h = f - s
    x = h // 3
    y = h % 3
    return (y + x)

