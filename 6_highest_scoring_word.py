def high(x):
    best = ""
    best_tot = 0
    for w in x.split():
        tot = 0
        for c in w:
            tot += ord(c) - ord("a") + 1
        if tot > best_tot:
            best_tot = tot
            best = w
    return best

print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')