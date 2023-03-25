import numpy as np
import pandas


def multiply_square_matrices(matrix1, matrix2, matrix_size):
    """
    Złożoność obliczeniowa:
    1. Utworzenie pustej macierzy n x n na wynik: n^2
    2. Zainicjowanie trzech zmiennych: 3*1 = 3
    3. Pierwsza pętla while: n wykonań
    2. Druga pętla while: n*n wykonań
    3. Trzecia pętla while: n*n*n wykonań
    Złożoność obliczeniowa: O(n^3)
    """
    result = np.zeros((matrix_size, matrix_size))
    matrix1_row = 0
    matrix2_col = 0
    elem_idx = 0

    while matrix1_row < matrix_size:
        while matrix2_col < matrix_size:
            while elem_idx < matrix_size:
                result[matrix1_row][matrix2_col] += matrix1[matrix1_row][elem_idx]*matrix2[elem_idx][matrix2_col]
                elem_idx += 1
            matrix2_col += 1
            elem_idx = 0
        matrix1_row += 1
        matrix2_col = 0
    return result

if __name__ == "__main__":
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

    print(f"Multiplication result: \n {pandas.DataFrame(multiply_square_matrices(matrix1, matrix2, n))}")



