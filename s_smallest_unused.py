def next_id(arr):
    if arr is not None:
        for n in range ( len(arr) + 1):
            if not n in arr:
                return n
    else:
        return 0


print(next_id([0,1,2,3,4,5,6,7,8,9,10]))
print(next_id([0,1,2,3,4,5,6,8,9,10]))
print(next_id([0,0,0,0,0,0]))