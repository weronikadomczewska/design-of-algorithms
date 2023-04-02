def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2

        left_lst = lst[:mid]
        right_lst = lst[mid:]

        mergesort(left_lst)
        mergesort(right_lst)

        left_idx = 0
        right_idx = 0
        insert_idx = 0

        while left_idx < len(left_lst) and right_idx < len(right_lst):
            if left_lst[left_idx] <= right_lst[right_idx]:
                lst[insert_idx] = left_lst[left_idx]
                left_idx += 1
            else:
                lst[insert_idx] = right_lst[right_idx]
                right_idx += 1
            insert_idx += 1

        while left_idx < len(left_lst):
            lst[insert_idx] = left_lst[left_idx]
            left_idx += 1
            insert_idx += 1

        while right_idx < len(right_lst):
            lst[insert_idx] = right_lst[right_idx]
            right_idx += 1
            insert_idx += 1


if __name__== "__main__":
    lst = [5, 10, 3, 8, 4, 11, 15, 11, 18, 20, 5, 4, 3]
    print(f"list before sort: {lst}")
    mergesort(lst)
    print(f"list after sort: {lst}")
