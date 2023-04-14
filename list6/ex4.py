import random
def fermat_primality_test(n, k):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):
            a = random.randint(2, n-2)
            if (a**(n-1)) % n != 1:
                return False
    return True

def miller_rabin_primality_test(n, k):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    for i in range(k):
        a = random.randint(2, n-2)
        d = n - 1
        while d % 2 == 0:
            d //= 2
        x = (a**d) % n
        if x == 1 or x == n-1:
            return True
        while d != n-1:
            x = (x**2) % n
            d *= 2
            if x == 1:
                return False
            elif x == n-1:
                return True
        return False



n = 11
k = 3
print(f"is number {n} prime: {fermat_primality_test(n, k)}")
print(f"is number {n} prime: {miller_rabin_primality_test(n, k)}")