def flip(d, a):
    a.sort()
    print(a)
    if d == "R":
        return a
    a.reverse()
    return a

def flip(d,  a):
    return sorted(a, reverse=d == 'L')

def flip(d, a):
    if d == 'L':
        return sorted(a, reverse=True)
    else:
        return sorted(a)

flip = lambda d, a: sorted(a, reverse = d == 'L')


