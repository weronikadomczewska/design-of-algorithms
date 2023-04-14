from ex1 import find_prime_factors
import matplotlib.pyplot as plt
import timeit
def rnwd(a, b):
    a_factors = find_prime_factors(a)
    b_factors = find_prime_factors(b)
    common_factors = set(a_factors).intersection(set(b_factors))
    if len(common_factors) == 0:
        return 1
    gcd = 1
    for factor in common_factors:
        gcd *= factor
    return gcd

def enwd(a, b):
    if b == 0:
        return a
    if b > a:
        return enwd(b, a)
    return enwd(b, a % b)

def single_test_gcd(gcd_func, n, q):
    # stmt = f"{gcd_func(n, q)}"
    # setup = "from ex1 import find_prime_factors"
    # times = timeit.repeat(stmt=stmt, setup=setup, repeat=3, number=1)
    t = timeit.timeit(lambda: gcd_func(n, q), number=1000, setup="from ex1 import find_prime_factors")
    return t


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# print(f"GCD of {a} and {b} (rnwd): {rnwd(a, b)}")
# print(f"GCD of {a} and {b} (enwd): {enwd(a, b)}")

rnwd_test_res = []
enwd_test_res = []
n = 10
m = 100
for q in range(1, m+1):
    rnwd_test_res.append(single_test_gcd(rnwd, n, q))
    enwd_test_res.append(single_test_gcd(enwd, n, q))
xs = range(1, m+1)

fig, ax = plt.subplots()
ax.plot(xs, rnwd_test_res, color="orange")
ax.plot(xs, enwd_test_res)
ax.set_xlabel("q")
ax.set_ylabel("time")
plt.legend(["rnwd", "enwd"])
plt.show()

