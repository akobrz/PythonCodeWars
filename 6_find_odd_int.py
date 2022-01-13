def sort_array2(source_array):
    t = [i for i in source_array if i % 2 == 1 ]
    t.sort()
    indicator = 0
    for k, v in enumerate(source_array):
        if v % 2 == 1:
            source_array[k] = t[indicator]
            indicator += 1
    return source_array


def sort_array(source_array):
    odds = sorted([i for i in source_array if i%2 == 1], reverse=True)
    return [ ( i if i%2==0 else odds.pop() ) for i in source_array]

# Return a sorted array.

print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]), [])
print(sort_array([11, 1, 2, 8, 3, 4, 5]), [1, 3, 2, 8, 5, 4, 11])