from robot_generator import *

class RobotList:
    def __init__(self):
        self.robot_matrix = []

    def add_robot(self, robot):
        prev_robot_index = self.robot_matrix[-1][2] if self.robot_matrix else -1
        next_robot_index = -1
        self.robot_matrix.append([prev_robot_index, robot, next_robot_index])
        if prev_robot_index >= 0:
            self.robot_matrix[prev_robot_index][2] = len(self.robot_matrix) - 1

    def remove_robot(self, robot):
        robot_index = self.find_robot_index(robot)
        if robot_index >= 0:
            prev_robot_index = self.robot_matrix[robot_index][0]
            next_robot_index = self.robot_matrix[robot_index][2]

            if prev_robot_index >= 0:
                self.robot_matrix[prev_robot_index][2] = next_robot_index
            if next_robot_index >= 0:
                self.robot_matrix[next_robot_index][0] = prev_robot_index

            self.robot_matrix.pop(robot_index)

    def find_robot_index(self, robot):
        for i, entry in enumerate(self.robot_matrix):
            if entry[1] == robot:
                return i
        return -1

    def sort_by_price(self):
        self.robot_matrix.sort(key=lambda x: x[1]['price'])

    def display_robots(self):
        for entry in self.robot_matrix:
            print(entry[1])


if __name__ == "__main__":
    robot_lst = RobotList()
    new_robot = {"type": "agv", "price": 1000, "range": 50, "camera": 1}
    robot_lst.add_robot(new_robot)
    print("List with one robot added:")
    robot_lst.display_robots()

    robots_from_file = load_robots_from_file("robots.json")
    for robot in robots_from_file:
        robot_lst.add_robot(robot)
    print("Matrix with more robots:")
    robot_lst.display_robots()

    robot_to_remove = {"type": "agv", "price": 1000, "range": 50, "camera": 1}
    robot_lst.remove_robot(robot_to_remove)
    print("List with robot removed:")
    robot_lst.display_robots()

    robot_lst.sort_by_price()
    print("Matrix sorted by price:")
    robot_lst.display_robots()
