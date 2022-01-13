# Sortowanie bąbelkowe

l = [1, 2, 3, 6, 1, 3, 7, 1, 9, 0]

def sortowanie(l):
    s = len(l)
    while s > 1:
        for i in range(s - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
        s -= 1
    return l

print(sortowanie(l))