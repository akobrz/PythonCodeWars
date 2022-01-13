def min1_org(*args):
    res = args[0]
    for a in args:
        if a < res:
            res = a
    return res

def min1(*args, n=1):
    res = args[0]
    for a in args:
        if a < res:
            res = a
    ret = (res,)
    if n > 1:
        ret += (min1(*(x for x in args if x > res), n=n-1))
    return ret


print(min1_org(-1, 20, -10, 14, 15, -7, -11, -12, 19))
print(min1(-1, 20, -10, 14, 15, -7, -11, -12, 19))
print(min1(-12, 20, -10, 14, 15, -7, -11, -12, 19, n=4))

s = "Ala ma kota a kot ma ale"
print([x for x in s.split()])
g = (x for x in s.split())
print(type(g),*g)

def parzysta():
    n = 0
    while True:
        yield n
        n += 2

f = (parzysta())

print(next(parzysta()))
print(next(parzysta()))
print(next(parzysta()))
print(parzysta())
print(parzysta())
print(parzysta())
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))


l = [1, 2, 3, 4, 5, 6]

def sum_iter(l):
    if not l:
        return 0
    else:
        return l[0] + sum_iter(l[1:])

print(sum_iter(l))