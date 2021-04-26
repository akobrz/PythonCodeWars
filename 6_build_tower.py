def tower_builder(n_floors):
    ret = []
    for i in range(1, n_floors + 1):
        ret.append(" "*(n_floors-i) + "*"*(2*i-1) + " "*(n_floors-i))
    return ret

print(tower_builder(1), ['*', ])
print(tower_builder(2), [' * ', '***'])
print(tower_builder(3), ['  *  ', ' *** ', '*****'])
print(tower_builder(4), ['   *   ', '  ***  ', ' ***** ', '*******'])

