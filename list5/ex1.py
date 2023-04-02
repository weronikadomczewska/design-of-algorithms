import matplotlib.pyplot as plt
import numpy as np


def first_function_rec(n):
    if n == 0:
        return 1
    else:
        return 3**n + first_function_rec(n-1)


def first_function_analytically(n):
    acc = 0
    for i in range(1, n+1):
        acc += 3**i
    return acc + 1


def second_function_rec(n):
    if n == -1 or n == 0:
        return 0
    else:
        return n + second_function_rec(n-2)


def second_function_analytically(n):
    if n == -1 or n == 0:
        return 0
    elif n % 2 == 0:
        return 2 + (n/2) * ((n/2) - 1)
    else:
        return 1 + (n/2) * ((n/2) + 1)


def third_function_rec(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return third_function_rec(n-1) + third_function_rec(n-2)


def third_function_analytically(n):
    sqrt_5 = 5**(1/2)
    return (1/sqrt_5)*((1+sqrt_5)/2)**n - (1/sqrt_5)*((1-sqrt_5)/2)**n


def calc_error(func1, func2, n):
    res = []
    arg = 0
    for i in range(n):
        res.append(abs(func1(arg) - func2(arg)))
        arg += 1
    return res


n = int(input("Enter n: "))

print("First function: ")
print(f"Analytically: {first_function_analytically(n)}")
print(f"Recursively: {first_function_rec(n)}")
print()

print("Second function: ")
print(f"Analytically: {second_function_analytically(n)}")
print(f"Recursively: {second_function_rec(n)}")
print()

print("Third function: ")
print(f"Analytically: {third_function_analytically(n)}")
print(f"Recursively: {third_function_rec(n)}")

fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True)
ns = range(1, n+1)
errors_first_function = calc_error(first_function_analytically, first_function_rec, n)
errors_second_function = calc_error(second_function_analytically, second_function_rec, n)
errors_third_function = calc_error(third_function_analytically, third_function_rec, n)
ax[0].plot(ns, errors_first_function)
ax[0].set_title("First function")
ax[1].plot(ns, errors_second_function)
ax[1].set_title("Second function")
ax[2].plot(ns, errors_third_function)
ax[2].set_title("Third function")
plt.show()

