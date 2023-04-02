import numpy as np
def find_max_elem_dividing(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        left_max = find_max_elem_dividing(lst[:mid])
        right_max = find_max_elem_dividing(lst[mid:])
        return max(left_max, right_max)


def find_second_max_elem_dividing(lst):
    max_elem = find_max_elem_dividing(lst)
    lst.remove(max_elem)
    return find_max_elem_dividing(lst)

def find_mean(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    return (len(lst) - 1)/len(lst) * find_mean(lst[1:]) + (1/len(lst)) * lst[0]


if __name__ == "__main__":
    lst = [5, 10, 3, 8, 4, 11, 15, 8, 5]
    print(f"Maximum value of a list {lst}: {find_max_elem_dividing(lst)}")
    print(f"Second maximum value of a list {lst}: {find_second_max_elem_dividing(lst)}")
    print(f"Mean of values of a list {lst}: {find_mean(lst)}")

