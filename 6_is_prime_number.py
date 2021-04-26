def is_prime(num):

    div =[]
    if num <2:
        return False

    for i in range(2,num+1):
        if num%i == 0 and i!=num:
            return False

    return True

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True

print(is_prime(0), False, "0  is not prime")
print(is_prime(1), False, "1  is not prime")
print(is_prime(2), True, "2  is prime")
print(is_prime(3), True, "3  is prime");
print(is_prime(4), False, "4  is not prime");
print(is_prime(5), True, "5  is prime");
print(is_prime(6), False, "6  is not prime");
print(is_prime(7), True, "7  is prime");
print(is_prime(8), False, "8  is not prime");
print(is_prime(9), False, "9 is not prime");
print(is_prime(2147483640), False, "2147483640 is not prime");
print(is_prime(2147483641), True, "2147483641 is prime");
print(is_prime(45), False, "45 is not prime");
print(is_prime(73), True, "73 is prime")
print(is_prime(75), False, "75 is not prime")
print(is_prime(5099), True, "5099 is prime");