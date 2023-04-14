import math
def find_prime_factors(n):
    if n == 1:
        return []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return [i] + find_prime_factors(n // i)
    return [n]

n = 9
print(f"Prime factors of number {n}: {find_prime_factors(n)}")