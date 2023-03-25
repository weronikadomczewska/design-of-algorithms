import time
import random
import numpy as np
from ex1 import *
from ex2 import *
from ex3 import *


def time_max_elem(A, n):
    tic = time.time()
    find_max_value(A, n)
    toc = time.time()
    return round(toc - tic, 6)

def time_second_max_elem(A, n):
    tic = time.time()
    find_second_max_value(A, n)
    toc = time.time()
    return round(toc - tic, 6)

def time_mean(A, n):
    tic = time.time()
    calc_mean(A, n)
    toc = time.time()
    return round(toc - tic, 6)


def time_ex2(matrix1, matrix2, n):
    tic = time.time()
    multiply_square_matrices(matrix1, matrix2, n)
    toc = time.time()
    return round(toc - tic, 6)


def time_ex3(B):
    tic = time.time()
    is_summing_to_zero(B)
    toc = time.time()
    return round(toc - tic, 6)

def generate_random_list(n):
    A = np.zeros(n)
    for i in range(n):
        A[i] = random.randint(-10, 10)
    return A

def generate_random_square_matrix(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(-10, 10)
    return matrix


if __name__ == "__main__":
    n = int(input("Enter number of elements in array: "))
    A = generate_random_list(n)
    B = generate_random_list(n)
    matrix1 = generate_random_square_matrix(n)
    matrix2 = generate_random_square_matrix(n)

    time_max_elem(A, n)
    time_second_max_elem(A, n)
    time_second_max_elem(A, n)
    time_ex2(matrix1, matrix2, n)
    time_ex3(B)






