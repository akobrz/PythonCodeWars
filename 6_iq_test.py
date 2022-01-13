def iq_test(numbers):
    a = [True if int(x) % 2 == 0 else False for x in (numbers.split(" "))]
    return a.index(True) + 1 if len(a) - sum(a) > 1 else a.index(False) +1


print(iq_test("2 4 7 8 10"), 3)
print(iq_test("1 2 2"), 1)