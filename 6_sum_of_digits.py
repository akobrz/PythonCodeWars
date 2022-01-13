
def digital_root(n):
    a = sum(map(int, str(n)))
    print(a)

    return

def digital_root2(n):
    if ( n > 9 ):
        w = 0
        for c in str(n):
            w += int(c)
        if w > 9:
            w = digital_root(w)
        return w
    else:
        return n

print(digital_root(16) == 7)
print(digital_root(942) == 6)
print(digital_root(132189) == 6)
print(digital_root(493193) == 2)