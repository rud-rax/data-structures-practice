def isValid(s):
    stack = []

    pdict = {"(": ")", "{": "}", "[": "]"}

    # print(s[1] in pdict.keys())

    if s[0] not in pdict.keys():

        return False

    for e in s:
        if e in pdict.keys():
            stack.append(e)
        else:
            x = stack.pop()
            if pdict[x] != e:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(isValid("(]"))
# print(isValid("(]"))


def isValid2(s):
    mystack = []
    brackets = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in brackets:
            mystack.append(char)
        else:  # closing parentheses is encountered
            if len(mystack) == 0:
                return False
            opening = mystack[-1]  # top / peek
            if brackets[opening] == char:
                mystack.pop()
            else:
                return False

    return len(mystack) == 0


print(isValid2("(]"))
