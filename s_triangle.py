def triangle1(n):
    if n >= 3:
        print("*")
        print("*" * 2)
        for i in range(n-3):
            print("*" + " " * (i + 1) + "*")
        print("*" * n)

def triangle2(n):
    if n >= 2:
        print(" " * (n - 1) + "*" + " " * (n - 1))
        for i in range(1, n - 1):
            print(" " * (n - 1 - i) + "*" + " " * (2 * i - 1 ) + "*")
        print("*" * n + "*" * (n - 1))

n = 10

triangle1(n)
triangle2(n)