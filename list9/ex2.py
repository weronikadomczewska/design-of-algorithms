from robot_generator import *

def quick_sort_by_price(list_of_robots):
    if len(list_of_robots) <= 1:
        return list_of_robots

    pivot = list_of_robots[len(list_of_robots) // 2]["price"]
    less = []
    equal = []
    greater = []

    for d in list_of_robots:
        if d["price"] < pivot:
            less.append(d)
        elif d["price"] == pivot:
            equal.append(d)
        else:
            greater.append(d)
    sorted_robots = quick_sort_by_price(less) + equal + quick_sort_by_price(greater)
    print([d["price"] for d in sorted_robots])  # Display the list of prices in each recursive call
    return sorted_robots


if __name__ == "__main__":
    robots_loaded_from_file = load_robots_from_file("robots.json")
    robots_sorted_by_price = quick_sort_by_price(robots_loaded_from_file)
    print_list_of_robots_as_table(robots_sorted_by_price)