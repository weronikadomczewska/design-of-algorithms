from ex1 import *


def find_robot_with_given_feature(required_feature, required_feature_name, list_of_robots):
    robots_with_matching_feature = []
    if required_feature is None:
        robots_with_matching_feature = list_of_robots[:]
    elif type(required_feature) == str or type(required_feature) == int:
        for robot in list_of_robots:
            if robot[required_feature_name] == required_feature:
                robots_with_matching_feature.append(robot)
    elif type(required_feature) == list:
        for robot in list_of_robots:
            if robot[required_feature_name] in required_feature:
                robots_with_matching_feature.append(robot)
    return robots_with_matching_feature


def find_robot_linear_search(list_of_robots, list_of_requirements):
    required_type = list_of_requirements[0]
    required_price = list_of_requirements[1]
    required_range = list_of_requirements[2]
    required_camera = list_of_requirements[3]

    robots_with_matching_type = find_robot_with_given_feature(required_type, "type", list_of_robots)
    robots_with_matching_price = find_robot_with_given_feature(required_price, "price", list_of_robots)
    robots_with_matching_range = find_robot_with_given_feature(required_range, "range", list_of_robots)
    robots_with_matching_camera = find_robot_with_given_feature(required_camera, "camera", list_of_robots)

    intersection = [d for d in robots_with_matching_type
                    if d in robots_with_matching_price and
                    d in robots_with_matching_range and
                    d in robots_with_matching_camera]
    return intersection


if __name__ == "__main__":
    n = int(input("Enter number of robots: "))
    random_robots = generate_list_of_robots(n)
    save_robots_to_file("robots.json", random_robots)
    robots_loaded_from_file = load_robots_from_file("robots.json")
    query = ["agv", None, [5, 6, 7, 8, 9, 10], 1]
    found_robot = find_robot_linear_search(robots_loaded_from_file, query)
    print_list_of_robots_as_table(found_robot)

