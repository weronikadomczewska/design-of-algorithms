from robot_generator import *


def make_heap(lst):
    n = len(lst)
    for i in range((n//2) - 1, -1, -1):
        max_heap(lst, n, i)

def max_heap(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[left]["price"] > lst[right]["price"]:
        largest = left
    if right < n and lst[right]["price"] > lst[largest]["price"]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heap(lst, n, largest)
def heap_sort_by_price(list_of_robots):
    pass