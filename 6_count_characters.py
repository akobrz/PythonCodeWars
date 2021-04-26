def count(string):
    ret = {v:string.count(v) for v in string}
    return ret


print(count('aba'))
print(count(''))