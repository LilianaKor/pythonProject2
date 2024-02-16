def spacey(array):
    result = []
    new_str=''
    for i in array:
        new_str += i
        result.append(new_str)
    return result

def spacey(array):
    return [''.join(array[:i+1]) for i in range(len(array))]

from itertools import accumulate
def spacey(array):
    return list(accumulate(array))

spacey= lambda a, x='': [x:=x+w for w in a]

from itertools import accumulate


def spacey(array):
    return list(map("".join, accumulate(array)))

def spacey(a):
    return [*map(lambda i:''.join(a[0:i+1]), range(len(a)))]


# Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array
# showing the space decreasing.  For example, running this function on the array ['i', 'have','no','space']
# would produce ['i','ihave','ihaveno','ihavenospace']
