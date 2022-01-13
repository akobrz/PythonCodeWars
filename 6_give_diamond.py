def diamond(n):
    if n % 2 == 0 or n < 1: return None
    ret = ""
    for i in range(1,n+1,2):
        ret += " "*int((n-i)/2) + "*"*i + "\n"
    for i in range(n-2,0,-2):
        ret += " "*int((n-i)/2) + "*"*i + "\n"
    return ret

print(diamond(5))
print(diamond(9))

# expected =  " *\n"
# expected += "***\n"
# expected += " *\n"
# print(diamond(1), "*\n")
# print(diamond(2), None)
# print(diamond(3), expected)
# print(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
# print(diamond(0), None)
# print(diamond(-3), None)