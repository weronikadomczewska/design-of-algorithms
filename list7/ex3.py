from ex2 import fft
from ex1 import *
import numpy as np
import timeit


def multiply_polynomials_FFT(p, q):
    n = len(p) + len(q) - 1
    n_fft = 2 ** int(np.ceil(np.log2(n)))
    p_fft = np.pad(p, (0, n_fft - len(p)))
    q_fft = np.pad(q, (0, n_fft - len(q)))

    p_fft = fft(p_fft)
    q_fft = fft(q_fft)

    r_fft = p_fft * q_fft
    r = np.real(fft(r_fft.conj())) / n_fft
    r = np.trim_zeros(r, "b")
    return r


if __name__ == "__main__":
    poly1 = [5, 0, 10, 6]
    poly2 = [1, 2, 4]
    print("First polynomial: ")
    print_polynomial(poly1)
    print("Second polynomial: ")
    print_polynomial(poly2)
    print("Result of multiplication of first and second polynomial: ")
    res = multiply_polynomials(poly1, poly2)
    print_polynomial(res)

    poly1 = np.random.rand(1024)
    poly2 = np.random.rand(1024)
    r1 = multiply_polynomials(poly1, poly2)
    r2 = multiply_polynomials_FFT(poly1, poly2)

    t1 = timeit.timeit(lambda: multiply_polynomials(poly1, poly2), number=10)
    t2 = timeit.timeit(lambda: multiply_polynomials_FFT(poly1, poly2), number=10)

    print(f"Time of naive polynomial multiplication: {t1}")
    print(f"Time of FFT polynomial multiplication: {t2}")





