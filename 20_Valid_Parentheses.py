s = "]"
def isValid(s):
    last = []
    for i in s:
        if i in '([{' :
            last.append(i)
        elif i in ')]}' and len(last) == 0:
            return False
        else:
            if len(last) != 0:
                if i == ')' and last[-1] == '(':
                    last.pop()
                elif i == '}' and last[-1] == '{':
                    last.pop()
                elif i == ']' and last[-1] == '[':
                    last.pop()
                else:
                    return False
    if len(last) == 0:
        return True
    return False

