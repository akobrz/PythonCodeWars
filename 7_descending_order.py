def descending_order(num):
    return int("".join(sorted(str(num))[::-1]))


print(descending_order(0))
print(descending_order(15))
print(descending_order(123456789))