#module tokenization
import re

def tokenize(strng):
    return filter(None, re.split("([+-/*!\(\)])", strng.replace(" ", "")))

def to_postfix(tokens):
    output = []
    operst = []
    for opt in tokens:
        if opt.isdigit():
            output.append(opt)
        elif opt == ")":
            while True:
                temp = operst.pop()
                if temp == "(" :
                    break;
                else:
                    output.append(temp)
        else:
            operst.append(opt)
    while True :
        output.append(operst.pop())
        if len(operst) == 0:
            break;
    return output
