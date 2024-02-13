def position(alphabet):
    alphabet = alphabet.lower()
    alphabet_position = ord(alphabet) - ord('a') + 1
    return f"Position of alphabet: {alphabet_position}"

print(position("a"))  # Output: Position of alphabet: 1
print(position("z"))  # Output: Position of alphabet: 26
print(position("e"))  # Output: Position of alphabet: 5


def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)

def position(alphabet):
    return "Position of alphabet: %s" % ("abcdefghijklmnopqrstuvwxyz".find(alphabet) + 1)

position = lambda i:"Position of alphabet: %i"%(ord(i)-96)

