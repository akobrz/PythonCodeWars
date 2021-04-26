def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    counter, pos, dir = 0, h, -1

    while pos > window:
        counter += 1
        if dir < 0:
            pos *= bounce
            dir = 1
        else:
            dir = -1

    return counter


print(bouncing_ball(2, 0.5, 1), 1)
print(bouncing_ball(3, 0.66, 1.5), 3)
print(bouncing_ball(30, 0.66, 1.5), 15)
print(bouncing_ball(30, 0.75, 1.5), 21)