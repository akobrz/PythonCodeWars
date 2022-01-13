
# 1
def litery_case_sensitive(napis):
    d = {}
    for s in napis:
        if s.isalpha():
            if s in d.keys():
                d[s] += 1
            else:
                d[s] = 1
    return d

def litery_case_not_sensitive(napis):
    d = {}
    for s in napis.lower():
        if s.isalpha():
            if s in d.keys():
                d[s] += 1
            else:
                d[s] = 1
    return d

print(litery_case_sensitive("Andrzej Kobrzycki"))
print(litery_case_not_sensitive("Andrzej Kobrzycki"))

# 2
def spr_trojkat(t):
    ret = []
    for p in t:
        p2 = sorted(p)[::-1]
        ret.append((p, p2[0] * p2[0] == p2[1] * p2[1] + p2[2] * p2[2]))
    return ret

print(spr_trojkat([(1, 2, 3), (10, 6, 8), (12, 13, 5), (5, 2, 1), (3, 3, 3), (3, 4, 5)]))

# 3
def palindrom(t):
    s = t.lower().replace(" ", "")
    return s == s[::-1]

print(palindrom("Kobyła ma mały bok"))
print(palindrom("Kobyła ma mały bko"))
print(palindrom("Kobyło ma mały bok"))