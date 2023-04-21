def multiply_polynomials(poly1, poly2, m, n):
    result = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            result[i + j] += poly1[i] * poly2[j]
    return result, len(result)


def print_polynomial(poly, n):
    for i in range(n):
        print(poly[i], end="")
        if i != 0:
            print(f"x^{i}", end="")
        if i != n - 1:
            print(" + ", end="")
        if i == n-1:
            print()


#################################################
poly1 = [5, 0, 10, 6]
poly2 = [1, 2, 4]
print("First polynomial: ")
print_polynomial(poly1, 4)
print("Second polynomial: ")
print_polynomial(poly2, 3)
print("Result of multiplication of first and second polynomial: ")
res, res_len = multiply_polynomials(poly1, poly2, 4, 3)
print_polynomial(res, res_len)

