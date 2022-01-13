def find_outlier(integers):
    if len([x for x in integers if x % 2 == 0]) == 1:
        return [x for x in integers if x % 2 == 0][0]
    else:
        return [x for x in integers if x % 2 != 0][0]


print(find_outlier([2, 4, 6, 8, 10, 3]), 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)