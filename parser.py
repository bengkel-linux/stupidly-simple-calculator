#module tokenization
import re

def apply(string, sarg = {}, darg = {}):
    return execute(to_postfix(tokenize(string)), sarg=sarg, darg=darg)

def execute(statement, sarg = {}, darg = {}):
    stack = []
    for elem in statement :
        if elem[0].isdigit() :
            stack.append(float(elem))
        elif elem in sarg :
            operand = stack.pop()
            stack.append(sarg[elem](operand))
        elif elem in darg :
            operandb = stack.pop()
            operanda = stack.pop()
            stack.append(darg[elem](operanda, operandb))
    if len(stack) == 1 :
        return stack.pop()
    else:
        return None


def tokenize(strng):
    return filter(None, re.split("([\+\-\/\*\!\(\)])", strng.replace(" ", "")))

def to_postfix(tokens):
    output = []
    operst = []
    for opt in tokens:
        if opt[0].isdigit():
            output.append(opt)
        elif opt == ")":
            while True:
                if len(operst) == 0 :
                    return []
                temp = operst.pop()
                if temp == "(" :
                    break;
                else:
                    output.append(temp)
        else:
            operst.append(opt)
    for something in operst :
        if something == "(" :
            return []
    while True :
        output.append(operst.pop())
        if len(operst) == 0:
            break;
    return output
