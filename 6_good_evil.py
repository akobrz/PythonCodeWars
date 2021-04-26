def goodVsEvil(good, evil):
    g = {0: 1, 1: 2, 2: 3, 3: 3, 4: 4, 5: 10}
    e = {0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 5, 6: 10}

    g_total = sum([ int(y) * x for (x, y) in zip(g, good.split(" "))])
    e_total = sum([ int(y) * x  for (x, y) in zip(e, evil.split(" "))])

    if g_total > e_total:
        return "Battle Result: Good triumphs over Evil"
    elif g_total < e_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))