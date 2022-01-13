def to_alternating_case(string):
    ret = ""
    for c in string:
        if ord(c) < 97:
           ret += c.lower()
        else:
            ret += c.upper()
    return ret

print(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")