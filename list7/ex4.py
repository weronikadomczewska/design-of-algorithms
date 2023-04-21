from ex1 import *
from ex3 import *
import matplotlib.pyplot as plt

def test_polynomial_multiplications(max_poly_degree):
    degrees = range(1, max_poly_degree+1)
    naive_times = []
    fft_times = []
    for degree in degrees:
        poly1 = np.random.rand(degree)
        poly2 = np.random.rand(degree)
        t1 = timeit.timeit(lambda: multiply_polynomials(poly1, poly2), number=10)
        t2 = timeit.timeit(lambda: multiply_polynomials_FFT(poly1, poly2), number=10)
        naive_times.append(t1)
        fft_times.append(t2)
    return naive_times, fft_times


max_poly_degree = 512
degrees = range(1, max_poly_degree+1)
naive_times, fft_times = test_polynomial_multiplications(max_poly_degree)
fig, ax = plt.subplots()
ax.plot(degrees, naive_times, color="orange")
ax.plot(degrees, fft_times)
ax.set_xlabel("degree")
ax.set_ylabel("time")
plt.legend(["naive", "fft"])
plt.show()
