def solution2(n):
    d1 = {0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
    d2 = {0:"",1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    d3 = {0:"",1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
    d4 = {0:"",1: "M", 2: "MM", 3: "MMM"}
    val = list(str(n))
    ret = ""
    for i in range(len(val), 0, -1):
        num = int(val[len(val)-i])
        if i == 4:
            ret += d4[num]
        elif i == 3:
            ret += d3[num]
        elif i == 2:
            ret += d2[num]
        else:
            ret += d1[num]
    return ret

def solution(n):
    d1 = {0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
    d2 = {0:"",1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    d3 = {0:"",1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
    d4 = {0:"",1: "M", 2: "MM", 3: "MMM"}
    val = list(str(n))
    ret = ""
    for i in range(len(val), 0, -1):
        num = int(val[len(val)-i])
        if i == 4:
            ret += d4[num]
        elif i == 3:
            ret += d3[num]
        elif i == 2:
            ret += d2[num]
        else:
            ret += d1[num]
    return ret

print(solution(1),'I', "solution(1),'I'")
print(solution(4),'IV', "solution(4),'IV'")
print(solution(6),'VI', "solution(6),'VI'")
print(solution(14),'XIV', "solution(14),'XIV")
print(solution(21),'XXI', "solution(21),'XXI'")
print(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
print(solution(91),'XCI', "solution(91),'XCI'")
print(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
print(solution(1000), 'M', 'solution(1000), M')
print(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
print(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")