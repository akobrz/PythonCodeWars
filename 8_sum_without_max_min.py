def sum_array(arr):
    if not arr == None:
        return 0
    elif len(arr) > 0:
        return sum(sorted(arr)[1:-1])
    else:
        return 0
