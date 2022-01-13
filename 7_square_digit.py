def square_digits(num):
    ret = ""
    for s in str(num):
        ret += str(int(s) * int(s))
    return ret

print(square_digits(9119))