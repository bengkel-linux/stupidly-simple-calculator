#module tokenization
import re
#type of token:
# Number   (N) :
# Operator (O) : + - / * ^
# Paren    (P) :
def _token_type(thing):
    return {'0':1,
            '1':1,
            '2':1,
            '3':1,
            '4':1,
            '5':1,
            '6':1,
            '7':1,
            '8':1,
            '9':1,
            '+':2,
            '-':2,
            '/':2,
            '*':2,
            '^':2,
            '!':2,
            '(':3,
            ')':3,
    }.get(thing, 4)


def tokenize(strng):
    return filter(None, re.split("([+-/*\(\)])", strng.replace(" ", "")))

def to_postfix(tokens):
    res = []
    waiting = 0
    for i in tokens:
        if i.isdigit():
            res.append(i)
            if waiting != 0:
                res.append(waiting)
                waiting = 0
        else:
            waiting = i
    return res
