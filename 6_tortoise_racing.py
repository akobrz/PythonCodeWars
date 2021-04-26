def race(v1, v2, g):
    if v1 >= v2: return None

    h = g/(v2-v1)
    m = (h - int(h)) * 60
    s = (m - int(m)) * 60

    if round(s,5) == 60:
        s = 0

    if round(m,5) == 60:
        m = 0

    return [int(round(h,5)), int(round(m,5)), int(round(s,5))]

print(race(720, 850, 70), [0, 32, 18])
print(race(80, 91, 37), [3, 21, 49])
print(race(80, 100, 40), [2, 0, 0])
print(race(100, 100, 40), [-1, -1, -1])
print(race(820,850,550), [18,20,0])
print(race(69,448,120),[0,18,59])
print(race(133,483,63),[0,10,48])