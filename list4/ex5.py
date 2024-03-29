import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

from ex4 import *

fig, ax = plt.subplots(2, 3)
a1 = int(input("Enter lower boundary: "))
b1 = int(input("Enter upper boundary: "))
n_to_test = np.arange(a1, b1)

a2 = int(input("Enter lower boundary: "))
b2 = int(input("Enter upper boundary: "))
n_to_test_2 = np.arange(a2, b2)

a3 = int(input("Enter lower boundary: "))
b3 = int(input("Enter upper boundary: "))
n_to_test_3 = np.arange(a3, b3)

times1 = []
times11 = []
times12 = []
times2 = []
times3 = []

for test_n in n_to_test:
    A = generate_random_list(test_n)
    times1.append(time_max_elem(A, test_n))
    times11.append(time_second_max_elem(A, test_n))
    times12.append(time_mean(A, test_n))

for test_n in n_to_test_2:
    matrix1 = generate_random_square_matrix(test_n)
    matrix2 = generate_random_square_matrix(test_n)
    times2.append(time_ex2(matrix1, matrix2, test_n))


for test_n in n_to_test_3:
    B = generate_random_list(test_n)
    times3.append(time_ex3(B))

# scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
# scaled_times1 = scaler.fit_transform(np.array(times1).reshape(-1, 1))
# scaled_times2 = scaler.fit_transform(np.array(times2).reshape(-1, 1))
# scaled_times3 = scaler.fit_transform(np.array(times3).reshape(-1, 1))

ax[0, 0].plot(n_to_test, times1)
ax[0, 1].plot(n_to_test, times11)
ax[0, 2].plot(n_to_test, times12)

ax[1, 0].plot(n_to_test_2, times2)
ax[1, 1].plot(n_to_test_3, times3)
plt.show()

