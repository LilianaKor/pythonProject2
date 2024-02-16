def remove_vowels(strng):
    str = ""

    for i in strng:
        if i in "aeiou":
            continue
        else:
            str += i
    return str

def remove_vowels(stg):
    return "".join(c for c in stg if c not in "aeiou")

def remove_vowels( _s ):
    return _s.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

def remove_vowels(strng):
    str = ['a','i','u','e','o']
    for i in str:
        strng = strng.replace(i, "")
    return strng

def remove_vowels(s):
    res = ""
    for char in s:
        if char.lower() not in "aeiou":
            res += char
    return res

remove_vowels = lambda s: __import__("re").sub(r"[aeiou]", "", s)

def remove_vowels(s):
    return ''.join(i for i in s if i not in'aeiou')
