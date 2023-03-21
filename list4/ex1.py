import numpy as np

"""
Złożoność obliczeniowa:
długość listy: n
Przypadek pesymistyczny: największy element na liście jest ostatni
1. Przypisanie current_max -> 1
2. Pętla -> n obiegów, w każdym obiegu jedno porównanie -> n porównań
Czas wykonania: n + 1
Złożoność: O(n)
"""

def find_max_value(lst, number_of_elems):
    current_max = lst[0]
    for i in range(number_of_elems):
        if lst[i] > current_max:
            current_max = lst[i]

    return current_max

"""

1. Wybranie wartości większej z lst[0], lst[1] -> 1
2. Wybranie wartości mniejszej z lst[0], lst[1] -> 1
3. Pętla: n-2 obrotów, w każdym obrocie 5 porównań + 1 przypisanie -> 6 operacji w każdym obrocie, razem 6(n-2) operacji
Czas wykonania: 1 + 1 + 6(n-2) = 2 + 6n - 12 = 6n - 10
Złożoność obliczeniowa: O(n) 
"""
def find_second_max_value(lst, number_of_elems):

    if lst[0] > lst[1]:
        first_max = lst[0]
    else:
        first_max = lst[1]
    if lst[0] < lst[1]:
        second_max = lst[0]
    else:
        second_max = lst[1]

    for i in range(2, number_of_elems):
        if lst[i] > first_max:
            second_max = first_max
            first_max = lst[i]
        elif lst[i] > second_max and first_max != lst[i]:
            second_max = lst[i]
        elif first_max == second_max and second_max != lst[i]:
            second_max = lst[i]
    return second_max

"""
Złożoność obliczeniowa: 
1. Przypisanie sum = 0 -> 1
2. Pętla wykonująca n obiegów i w każdym jedna operacja dodawania -> n
3. Obliczenie wartości średniej -> 1

Czas wykonania: n + 2
Złożoność obliczeniowa: O(n)

"""


def calc_mean(lst, number_of_elems):
    sum = 0
    for i in range(number_of_elems):
        sum += lst[i]

    return sum / number_of_elems


n = int(input("Enter number of elements in a list: "))
lst = np.zeros(n)
for i in range(n):
    lst[i] = (int(input("Enter a number: ")))


print("Finding maximum value in a list")
print(f"Maximum value of a list {list(lst)} is: {find_max_value(lst, n)}")
print("The time complexity of this algorithm is O(n)")

print("Finding second maximum value in a list")
print(f"Second maximum value of a list {list(lst)}: {find_second_max_value(lst, n)}")

print("Finding mean of elements in a list:")
print(f"Mean value of a list {list(lst)}: {calc_mean(lst, n)}")
