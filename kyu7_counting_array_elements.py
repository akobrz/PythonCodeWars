

def count2(array):
    m = {}
    for i in array:
        m[i] = m.get(i, 0) + 1
    return m

def count(array):
    return {x:array.count(x) for x in array}

print(count(['a', 'a', 'b', 'b', 'b']))