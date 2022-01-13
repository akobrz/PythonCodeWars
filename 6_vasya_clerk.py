def tickets(people):
    a, b = 0, 0
    for i in people:
        if i == 25: a += 1
        elif i == 50:
            b += 1
            if a > 0: a -= 1
            else: return "NO"
        elif i == 100 and a > 0 and b > 0:
            a -= 1
            b -= 1
        elif i == 100 and a > 2: a -= 3
        else: return "NO"
    return "YES"

print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))
print(tickets([25, 25, 50, 50, 50, 25, 50, 100, 50, 25]))
print(tickets([25, 25, 25, 25, 50, 100, 50]))
