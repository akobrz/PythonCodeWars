def validBraces(string):
    bra1 = {"(":")", "{":"}","[":"]"}
    bra2 = {")":"(", "}":"{", "]":"["}
    list= []
    for c in string:
        if c in "({[":
            list.append(c)
        elif c in ")}]" and bra2[c] not in list:
            return False
        elif c in ")}]" and bra1[list[len(list)-1]] == c:
            list.pop()
        else:
            return False
    if len(list) > 0:
        return False
    return True

print(validBraces("()"), True)
print(validBraces("[(])"), False)
print(validBraces(")(}{]["), False)