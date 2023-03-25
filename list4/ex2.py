import numpy as np
from prettyprinter import pprint
def multiply_square_matrices(matrix1, matrix2, matrix_size):
    result = np.zeros((n, n))
    for row in range(n):
        numbers_sum = 0
        for column in range(n):
            for s in range(n):
                numbers_sum += matrix1[row][column] * matrix2[column][row]
            result[row][column] = numbers_sum

    return result


n = int(input("Enter size of an matrix: "))

matrix1 = np.zeros((n, n))
matrix2 = np.zeros((n, n))

print("Filling first matrix")
for i in range(n):
    for j in range(n):
        matrix1[i][j] = int(input(f"Enter number on position [{i}][{j}]: "))

print("Filling second matrix")
for i in range(n):
    for j in range(n):
        matrix2[i][j] = int(input(f"Enter number on position [{i}][{j}]: "))

print(f"Multiplication result: {multiply_square_matrices(matrix1, matrix2, n)}")



