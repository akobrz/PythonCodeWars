def multiplication_table(size):
    ret = [[0]*size for i in range(size)]
    for i in range(size):
        ret[0][i] = i + 1
        ret[i][0] = i + 1

    if size > 1:
        for i in range(1,size):
            for j in range(1, size):
                ret[i][j] = ret[i][0] * ret[0][j]

    return ret


print(multiplication_table(2), [[1,2],[2,4]])
print(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])