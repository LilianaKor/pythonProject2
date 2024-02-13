def paperwork(n, m):
    if (n<0 or m<0):
        return 0
    else:
        total = n*m
        return total

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

 def paperwork(n, m):
        if m < 0 or n < 0:
            return 0
        else:
            return n * m

def paperwork(n, m):
    return max(n, 0) * max(m, 0)

def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n*m


def paperwork(n, m):
    # Declaring the variable with a value makes it local instead of global
    ans = 0

    # Checks that n and m are > 0 before doing the math
    if n and m > 0:
        ans = n * m

    # Throws out any answers that are negative
    if ans <= 0:
        ans = 0

    # Returns the ans variable
    return ans