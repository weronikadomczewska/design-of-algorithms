from robot_generator import *


def heap_sort_by_price(list_of_robots):
    n = len(list_of_robots)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(list_of_robots, n, i)
    for i in range(n-1, 0, -1):
        list_of_robots[i], list_of_robots[0] = list_of_robots[0], list_of_robots[i]
        max_heapify(list_of_robots, i, 0)
        print([d["price"] for d in list_of_robots])
    return list_of_robots


def max_heapify(list_of_robots, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and list_of_robots[left]["price"] > list_of_robots[largest]["price"]:
        largest = left
    if right < n and list_of_robots[right]["price"] > list_of_robots[largest]["price"]:
        largest = right
    if largest != i:
        list_of_robots[i], list_of_robots[largest] = list_of_robots[largest], list_of_robots[i]
        max_heapify(list_of_robots, n, largest)

if __name__ == "__main__":
    robots_loaded_from_file = load_robots_from_file("robots.json")
    robots_sorted_by_price = heap_sort_by_price(robots_loaded_from_file)
    print_list_of_robots_as_table(robots_sorted_by_price)
