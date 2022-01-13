
def is_isogram(string):
    d = {}
    if string is not None:
        for s in string.lower():
            if s in d.keys():
                return False
            else:
                d[s] = 1
    return True

print(is_isogram("sdfsdfsfsfwe"))
print(is_isogram(""))
print(is_isogram("moOse"))
