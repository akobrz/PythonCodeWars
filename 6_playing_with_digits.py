def dig_pow(n, p):
    a = sum([pow(int(str(n)[i]),p+i) for i in range(len(str(n)))])
    if int(a/n) == a/n: return int(a/n)
    else: return -1


print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(695,2),2)
print(dig_pow(46288, 3), 51)