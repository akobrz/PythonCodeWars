def delete_nth(order,max_e):
    ret = []

    for c in order:
        if ret.count(c) < max_e:
            ret.append(c)

    return ret

print(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])