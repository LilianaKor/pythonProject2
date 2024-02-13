def filter_string(st):
    num = ''
    for i in st:
        if i.isdigit():
            num += i

    return int(num)

def filter_string(string):
    rez = ""
    for i in string:
        if i>='0' and i<='9':
            rez = rez + i
    return int(rez)

def filter_string(stR):
    out = ''
    for i in stR:
        if i.isdigit() == True:
            out += i
    return int(out)

filter_string = lambda string : int(''.join([i for i in string if i.isdigit()]))