#from preloaded import NATO  # NATO['A'] == 'Alfa', etc

# The idea for this kata came from 9gag today:
#
#     Task
#     You
#     'll have to translate a string to Pilot'
#     s
#     alphabet(NATO
#     phonetic
#     alphabet).
#
#     Input:
#
#     If, you
#     can
#     read?
#
#     Output:
#
#     India
#     Foxtrot, Yankee
#     Oscar
#     Uniform
#     Charlie
#     Alfa
#     November
#     Romeo
#     Echo
#     Alfa
#     Delta ?
#
#     Note:
#
#     There is a
#     preloaded
#     dictionary
#     that
#     you
#     can
#     use, named
#     NATO.It
#     uses
#     uppercase
#     keys, e.g.NATO['A'] is "Alfa".See
#     comments in the
#     initial
#     code
#     to
#     see
#     how
#     to
#     access
#     it in your
#     language.
#     The
#     set
#     of
#     used
#     punctuation is,.!?.
#     Punctuation
#     should
#     be
#     kept in your
#     return string, but
#     spaces
#     should
#     not.
#     Xray
#     should
#     not have
#     a
#     dash
#     within.
#     Every
#     word and punctuation
#     mark
#     should
#     be
#     seperated
#     by
#     a
#     space
#     ' '.
#     There
#     should
#     be
#     no
#     trailing
#     whitespace

from preloaded import NATO  # NATO['A'] == 'Alfa', etc

def to_nato(words: str) -> str:
    lst = []
    for i in words:
        if i.upper() in NATO.keys():
            lst.append(NATO.ge(i_apper())
            else:
            if i != '':
                lst.append(i)

    return " ".join(lst)


from preloaded import NATO  # NATO['A'] == 'Alfa', etc


def to_nato(words: str) -> str:
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')


def to_nato(words):
    return " ".join(NATO.get(char, char) for char in words.upper() if not char.isspace())


def to_nato(w):
    return ' '.join(NATO[c.upper()] if c.isalpha() else c for c in w.replace(' ', ''))

to_nato=lambda words:' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')


to_nato = lambda w: ' '.join(NATO[c] if c in NATO else c for c in w.upper().replace(' ', ''))
