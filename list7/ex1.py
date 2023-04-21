def multiply_polynomials(poly1, poly2):
    m = len(poly1)
    n = len(poly2)
    result = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            result[i + j] += poly1[i] * poly2[j]
    return result


def print_polynomial(poly):
    n = len(poly)
    for i in range(n):
        print(poly[i], end="")
        if i != 0:
            print(f"x^{i}", end="")
        if i != n - 1:
            print(" + ", end="")
        if i == n-1:
            print()


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

