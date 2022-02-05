def find_digit(num, nth):
    return -1 if not nth>0 else str(num)[-nth] if len(str(num))>nth else 0


print(find_digit(5673, 4), 5)
print(find_digit(129, 2), 2)
print(find_digit(-2825, 3), 8)
print(find_digit(0, 20), 0)
print(find_digit(65, 0), -1)
print(find_digit(24, -8), -1)