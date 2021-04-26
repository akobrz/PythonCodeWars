def find_uniq(arr):
    for c in set(arr):
        if arr.count(c) == 1:
            return c

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
print(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
print(find_uniq([ 3, 10, 3, 3, 3 ]), 10)