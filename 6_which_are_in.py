def in_array(array1, array2):
    a = []

    for a1 in array1:
        for a2 in array2:
            if a2.count(a1) > 0:
                if not a1 in a:
                    a.append(a1)

    return sorted(a)


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1, a2), r)