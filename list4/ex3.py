import time
def powerset(lst):
    """
    Złożoność czasowa: O(2^n)
    """
    if len(lst) == 0:
        return [[]]
    exclude_first = powerset(lst[1:])
    include_first = [[lst[0]] + x for x in exclude_first]
    return exclude_first + include_first

def is_summing_to_zero(lst):
    """
    Złożoność:
    n - ilość elementów w zbiorze A
    1. Wygenerowanie wszystkich podzbiorów: ~2^n operacji
    2. Przeglądanie wszystkich zbiorów 2^n operacji
    3. sumowanie elementów podzbioru: 2^n zbiorów, w każdym przeglądamy każdy element
    Oszacowanie: O(2^n)
    """
    all_subsets = powerset(lst)
    # print(f"All subsets of {lst}: {all_subsets}")
    for s in all_subsets:
        if len(s) == 0:
            continue
        elem_sum = 0
        for i in range(len(s)):
            elem_sum += s[i]
        if elem_sum == 0:
            return True
    return False


if __name__ == "__main__":
    n = int(input("Enter number of elements in a list: "))
    A = []
    for i in range(n):
        A.append(int(input("Enter number: ")))

    # tic = time.time()
    print(f"Is some subset summing to 0: ", is_summing_to_zero(A))
    # toc = time.time()
    # print(toc-tic)
