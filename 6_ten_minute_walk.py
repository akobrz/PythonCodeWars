def is_valid_walk(walk):
    x, y = 0, 0
    if len(walk) != 10: return False
    for d in walk:
        if d == "n": x += 1
        if d == "s": x -= 1
        if d == "w": y -= 1
        if d == "e": y += 1
    return x == 0 and y == 0

#some test cases for you...
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
print(is_valid_walk(['w']), 'should return False');
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');