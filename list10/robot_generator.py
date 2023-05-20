import random
import pandas as pd
import json


def generate_random_robot():
    types = ["agv", "afv", "asv", "auv"]
    prices = range(0, 10001)
    range_ = range(0, 101)
    camera = (0, 1)
    robot = {
        "type": random.choice(types),
        "price": random.choice(prices),
        "range": random.choice(range_),
        "camera": random.choice(camera)
    }
    return robot


def generate_list_of_robots(n):
    robots = []
    for i in range(n):
        robots.append(generate_random_robot())
    return robots


def print_list_of_robots_as_table(list_of_robots):
    data = {}
    cnt = 0
    columns = ["type", "price", "range", "camera"]
    if type(list_of_robots) == dict:
        data[f"robot0"] = list_of_robots
    else:
        for robot in list_of_robots:
            data[f"robot{cnt}"] = robot
            cnt += 1
    df = pd.DataFrame.from_dict(data, orient="index", columns=columns)
    return df


def save_robots_to_file(filename, list_of_robots):
    with open(filename, "w") as file:
        json.dump(list_of_robots, file)


def load_robots_from_file(filename):
    robots = []
    with open(filename, "r") as file:
        robots = json.load(file)
    return robots


if __name__ == "__main__":
    n = int(input("Enter number of robots: "))
    random_robots = generate_list_of_robots(n)
    save_robots_to_file("robots.json", random_robots)
    robots_loaded_from_file = load_robots_from_file("robots.json")
    print_list_of_robots_as_table(robots_loaded_from_file)




