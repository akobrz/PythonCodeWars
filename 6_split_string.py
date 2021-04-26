def solution2(s):
    a = []
    for i in range(0,len(s),2):
        if len(s[i:i+2]) == 2:
            a.append(s[i:i+2])
        else:
            a.append(s[i:i+1]+"_")
    return a

def solution(s):
    return [s[x:x+2] if len(s[x:x+2]) == 2 else s[x:x+1]+"_" for x in range(0,len(s),2)]


print(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
print(solution("asdfads"), ['as', 'df', 'ad', 's_'])
print(solution(""), [])
print(solution("x"), ["x_"])