def radix_sort(matrix):
    cols = len(matrix[0])
    for col in range(cols - 1, -1, -1):
        counting_sort(matrix, col)
    return matrix


def counting_sort(matrix, col):
    rows = len(matrix)
    cols = len(matrix[0])

    count = [0] * (max_value(matrix, col) + 1)

    for row in range(rows):
        value = matrix[row][col]
        count[value] += 1

    total = 0
    for i in range(len(count)):
        count[i], total = total, count[i] + total

    sorted_matrix = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        value = matrix[row][col]
        sorted_row = count[value]
        sorted_matrix[sorted_row] = matrix[row]
        count[value] += 1

    for row in range(rows):
        matrix[row] = sorted_matrix[row]


def max_value(matrix, col):
    max_val = matrix[0][col]
    for row in range(1, len(matrix)):
        if matrix[row][col] > max_val:
            max_val = matrix[row][col]
    return max_val


if __name__ == "__main__":
    matrix = [
        [4, 7, 2],
        [1, 5, 6],
        [3, 5, 2],
        [1, 2, 9]
    ]

    sorted_matrix = radix_sort(matrix)
    print("sorted matrix: ")
    for row in sorted_matrix:
        print(row)
