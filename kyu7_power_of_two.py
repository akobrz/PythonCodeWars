import math
import numpy

def power_of_two3(x, n=0):
    if x == 0:
        return False
    if x == 1:
        return True
    while x != 2:
        y = numpy.divide(x, 2)
        if x % 2 == 1:
            return False
        else:
            x /= 2.0
    return True

def power_of_two(x):
    if x == 0:
        return False
    print(numpy.log2(x))
    return True if numpy.log2(x) == int(numpy.log2(x)) else False


# print(power_of_two(0), False)
# print(power_of_two(1), True)
# print(power_of_two(2), True)
# print(power_of_two(5), False)
# print(power_of_two(6), False)
# print(power_of_two(4096), True)
print(power_of_two(1180591620717411303426), False)