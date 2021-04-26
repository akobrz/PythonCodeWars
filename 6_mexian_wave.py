def wave2(people):
    a = []
    for l in range(0, len(people)):
        c = people[l:l+1]
        if c.isalpha():
            p = people[:l] + c.upper() + people[l+1:]
            a.append(p)
    return a

def wave(p):
    return [ (p[:l] + p[l:l+1].upper() + p[l+1:]) for l in range(0, len(p)) if p[l:l+1].isalpha()]


print(wave("andrzej kobrzycki"))