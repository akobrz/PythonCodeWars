def balanced_num(number: int) -> int:
    '''
    :param number: number
    :return: int
    '''
    n = str(number)
    l = len(n)
    if n is not None:
        if len(n) % 2 == 0 and l > 2:
            return "Balanced" if sum([int(x) for x in n[0:(l//2 - 1)]]) == sum([int(x) for x in n[(l//2 + 1):]]) else "Not Balanced"
        elif len(n) % 2 == 1 and l > 1:
            return "Balanced" if sum([int(x) for x in n[0:(l//2)]]) == sum([int(x) for x in n[(l//2 + 1):]]) else "Not Balanced"
        return "Balanced"
    return "Not Balanced"

print(balanced_num(295591)  , "Not Balanced")
print(balanced_num(7)  , "Balanced")
print(balanced_num(17)  , "Balanced")
print(balanced_num(1230987) , "Not Balanced")
print(balanced_num(56239814), "Balanced")
print(balanced_num(959), "Balanced")



