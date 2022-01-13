def solution(roman):
    d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1,"MC":900,"DC":400,"XC":90,"XL":40,"IX":9,"IV":4}
    ret = 0

    for i in range(0, len(roman)):
        a = roman[i:i+2]
        b = roman[i-1:i+1]
        c = roman[i]
        if not roman[i-1:i+1] in d.keys() and roman[i] in d.keys():
            ret += d.get(roman[i])
        elif roman[i:i+2] in d.keys():
            ret += d.get(roman[i:i + 2])

    return ret

# print(solution('XXI'), 21, 'XXI should == 21')
# print(solution('I'), 1, 'I should == 1')
print(solution('IV'), 4, 'IV should == 4')
# print(solution('MMVIII'), 2008, 'MMVIII should == 2008')
# print(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')