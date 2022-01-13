t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0

def shift_table(t:[], n:int):
    for i in range(n):
        for j in range(len(t)-1):
            t[j], t[j+1] = t[j+1], t[j]
    return t

# print(shift_table(t, n))

t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
t2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
t3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
t4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
t5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
t6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def make_calc(t, s, ind, d):
    for i in range(0, s):
        t[ind + d*i], t[ind + d*(i + s)] = t[ind + d*(i + s)], t[ind + d*i]
    return d*s

def make_shift(t, s):
    s = s % len(t) if s > len(t) else s
    ib, ie, d = 0, len(t) - 1, 1
    while s > 0:
        if ie - ib + 1 >= 2 * s and d == 1:
            ib += make_calc(t, s, ib, d)
        elif ie - ib + 1 >= 2 * s and d == -1:
            ie += make_calc(t, s, ie, d)
        else:
            s = ie - ib + 1 - s
            d *= -1



def make_shift2(t, s):
    s = s % len(t) if s > len(t) else s
    ib, ie, d = 0, len(t) - 1, 1

    while s > 0:
        ieib = ie - ib + 1
        if ieib >= s + s:
            if d:
                ibs = ib + s
                for i in range(0, s):
                    t[i + ib], t[i + ibs] = t[i + ibs], t[i + ib]
                ib += s
            else:
                ies = ie - s
                for i in range(0, s):
                    t[ie - i], t[ies - i] = t[ies - i], t[ie - i]
                ie -= s
        else:
            s = ieib - s
            d = True if not d else False
    pass


make_shift2(t1, 2)
print(t1)
make_shift2(t2, 2)
print(t2)
make_shift2(t3, 2)
print(t3)
make_shift2(t4, 2)
print(t4)
make_shift2(t5, 2)
print(t5)
make_shift2(t6, 2)
print(t6)
