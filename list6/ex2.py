import math
import numpy as np
def sieve_of_eratosthenes(p):
    x = np.ones(p+1)
    x[0] = 0
    x[1] = 0
    for n in range(2, int(p**(1/2))+1):
        if x[n] == 1:
            for j in range(2, int(p/n)+1):
                x[n*j] = 0
    return x

try:
    p = int(input("Enter p: "))
except:
    ValueError(f"Expected int, given {type(p)}")
res = sieve_of_eratosthenes(11)
for i in range(len(res)):
    print(f"is {i} prime: {int(res[i])}")
