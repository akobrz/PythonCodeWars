def narcissistic(value):
    return value == sum([int(x)**len(str(value)) for x in str(value)])

def narcissistic2( value ):
    l, s = len(str(value)), 0
    for c in str(value):
        s += pow(int(c),l)
    return s==value

print(narcissistic(7), True, '7 is narcissistic');
print(narcissistic(371), True, '371 is narcissistic');
print(narcissistic(122), False, '122 is not narcissistic')
print(narcissistic(4887), False, '4887 is not narcissistic')