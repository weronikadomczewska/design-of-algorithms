from ex1 import *


def sort_robots_by_feature(list_of_robots, feature_name):
    return sorted(list_of_robots, key=lambda x: x[feature_name])


def binary_search(list_of_robots, feature_name, required_feature_values):
    sorted_list_of_robots = sort_robots_by_feature(list_of_robots, feature_name)
    low = 0
    high = len(list_of_robots)-1

    for value in required_feature_values:
        while low <= high:
            mid = (high + low) // 2
            robot_feature = sorted_list_of_robots[mid][feature_name]
            if robot_feature == value:
                return sorted_list_of_robots[mid]
            if robot_feature < value:
                low = mid + 1
            elif robot_feature > value:
                high = mid - 1
    return []


if __name__ == "__main__":
    robots_loaded_from_file = load_robots_from_file("robots.json")
    feature_name = ""
    while feature_name not in ["type", "price", "range", "camera"]:
        feature_name = input("Enter feature name: (type, price, range or camera): ")

    found_robot = binary_search(robots_loaded_from_file, feature_name, [6705])
    print_list_of_robots_as_table(found_robot)



