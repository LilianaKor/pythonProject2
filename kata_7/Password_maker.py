# One suggestion to build a satisfactory password is to start with a memorable phrase or sentence and make a password
# by extracting the first letter of each word.

# Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with the number 0):

# instead of including i or I put the number 1 in the password;
# instead of including o or O put the number 0 in the password;
# instead of including s or S put the number 5 in the password.
# Examples:
# "Give me liberty or give me death"  --> "Gml0gmd"
# "Keep Calm and Carry On"            --> "KCaC0"

SWAP = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}


def make_password(phrase):
    return ''.join(SWAP.get(a[0], a[0]) for a in phrase.split())


def make_password1(phrase):
    new = ""
    phrase = phrase.replace("i", "1").replace("I", "1")
    phrase = phrase.replace("o", "0").replace("O", "0")
    phrase = phrase.replace("s", "5").replace("S", "5")
    phrase = phrase.split(" ")
    for i in phrase:
        new += i[0]
    return new


def make_password2(ph):
    return (''.join([i[0] for i in ph.split(' ')]).replace('o', '0').replace('O', '0')
            .replace('s', '5').replace('S', '5').replace('i', '1').replace('I', '1'))


TABLE = str.maketrans('iIoOsS', '110055')


def make_password3(s):
    return ''.join(w[0] for w in s.split()).translate(TABLE)


def make_password4(phrase, mapping=dict(['i1', 'o0', 's5'])):
    return ''.join(mapping.get(c.lower(), c) for c, *rest in phrase.split())


def make_password5(phrase):
    phrase = phrase.split(" ")
    password = ""
    for word in phrase:
        password += word[0]
    password = password.replace("I", "1").replace("i", "1")
    password = password.replace("O", "0").replace("o", "0")
    password = password.replace("S", "5").replace("s", "5")
    return password


from re import sub


def make_password6(phrase):
    lst = phrase.split(" ")
    passw = ''
    for i in lst:
        passw += i[0]
    passw = sub('[iI]', '1', passw)
    passw = sub('[oO]', '0', passw)
    passw = sub('[sS]', '5', passw)
    return passw
