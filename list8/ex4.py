from ex1 import *


def hash_function(parameter_value, attempt, table_size):
    return (sum(ord(c) for c in str(parameter_value)) + attempt**2) % table_size


def robot_search(robot_list, parameter_name, parameter_value, alpha):
    table_size = int(len(robot_list) / alpha)
    hash_table = [None] * table_size
    for robot in robot_list:
        attempt = 0
        index = hash_function(robot[parameter_name], attempt, table_size)
        while hash_table[index] is not None:
            attempt += 1
            index = hash_function(robot[parameter_name], attempt, table_size)
        hash_table[index] = robot

    attempt = 0
    search_index = hash_function(parameter_value, attempt, table_size)

    start_index = search_index
    while hash_table[search_index] is not None:
        if hash_table[search_index][parameter_name] == parameter_value:
            return hash_table[search_index]
        attempt += 1
        search_index = hash_function(parameter_value, attempt, table_size)
        if search_index == start_index:
            break
    return []


if __name__ == "__main__":
    robots_loaded_from_file = load_robots_from_file("robots.json")
    alpha = float(input("Podaj docelowy współczynnik wypełnienia tablicy: "))
    found_robot = robot_search(robots_loaded_from_file, "price", 5471, alpha)
    print_list_of_robots_as_table(found_robot)
