from robot_generator import *


def counting_sort_by_range(list_of_robots):
    max_range = max(d["range"] for d in list_of_robots)
    cnt = [0] * (max_range + 1)

    for d in list_of_robots:
        cnt[d["range"]] += 1
    for i in range(1, max_range+1):
        cnt[i] += cnt[i-1]

    sorted_robots = [None] * len(list_of_robots)

    for d in reversed(list_of_robots):
        idx = cnt[d["range"]] - 1
        sorted_robots[idx] = d
        cnt[d["range"]] -= 1

    return sorted_robots


if __name__ == "__main__":
    robots_loaded_from_file = load_robots_from_file("robots.json")
    robots_sorted_by_range = counting_sort_by_range(robots_loaded_from_file)
    print_list_of_robots_as_table(robots_sorted_by_range)
