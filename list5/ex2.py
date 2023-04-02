import numpy as np
def find_max_elem_dividing(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        left_max = find_max_elem_dividing(lst[:mid])
        right_max = find_max_elem_dividing(lst[mid:])
        return max(left_max, right_max)


def find_second_max_elem_dividing(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return min(lst)
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        max_left = find_second_max_elem_dividing(left)
        max_right = find_second_max_elem_dividing(right)

        if max_left is None:
            return max_right
        elif max_right is None:
            return max_left
        else:
            if max_left > max_right:
                return find_second_max_elem_dividing([x for x in lst if x != max_left])
            else:
                return find_second_max_elem_dividing([x for x in lst if x != max_right])


def find_mean(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    return (len(lst) - 1)/len(lst) * find_mean(lst[1:]) + (1/len(lst)) * lst[0]


if __name__ == "__main__":
    lst = [5, 10, 3, 8, 4, 11, 15, 11, 18, 20, 5, 4, 3, 8, 15, 4, 18, 17, 4, 5, 6, 48, 45, 8]
    print(f"Maximum value of a list {lst}: {find_max_elem_dividing(lst)}")
    print(f"Second maximum value of a list {lst}: {find_second_max_elem_dividing(lst)}")
    print(f"Mean of values of a list {lst}: {find_mean(lst)}")

