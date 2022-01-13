def find_nb(m):
    iterator, ret = 0, 0
    while ret < m:
        iterator += 1
        ret += iterator**3

    return iterator if ret == m else -1

print(find_nb(4183059834009), 2022)
print(find_nb(24723578342962), -1)
print(find_nb(135440716410000), 4824)
print(find_nb(40539911473216), 3568)
print(find_nb(26825883955641), 3218)