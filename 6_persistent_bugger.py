def persistence(n,i=0):
    if ( n < 10 ):
        return i
    else:
        w = 1
        i += 1
        for c in str(n):
            w *= int(c)
        if w > 9:
            i = persistence(w, i)
    return i

print(persistence(39) == 3)
print(persistence(4) == 0)
print(persistence(25) == 2)
print(persistence(999) == 4)
