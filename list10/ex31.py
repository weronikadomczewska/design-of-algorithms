from robot_generator import *

class RobotList:
    def __init__(self):
        self.robot_matrix = []

    def __repr__(self):
        output = ""
        for row in self.robot_matrix:
            output += repr(row[1]) + "\n"
        return output

    def add_robot(self, robot):
        prev_robot = None
        next_robot = None
        if self.robot_matrix:
            prev_robot = self.robot_matrix[-1][1]
            self.robot_matrix[-1][2] = robot
        self.robot_matrix.append([prev_robot, robot, next_robot])

    def remove_robot(self, robot):
        for i in range(len(self.robot_matrix)):
            if self.robot_matrix[i][1] == robot:
                prev_robot = self.robot_matrix[i][0]
                next_robot = self.robot_matrix[i][2]
                if prev_robot:
                    prev_robot[2] = next_robot
                if next_robot:
                    next_robot[0] = prev_robot
                self.robot_matrix.pop(i)
                break
        # Aktualizacja indeksów w macierzy robotów
        for i in range(len(self.robot_matrix)):
            if i > 0:
                self.robot_matrix[i][0] = self.robot_matrix[i - 1] if i - 1 >= 0 else None
            if i < len(self.robot_matrix):
                self.robot_matrix[i][2] = self.robot_matrix[i + 1] if i + 1 < len(self.robot_matrix) else None

    def search_robot(self, key):
        for row in self.robot_matrix:
            if row[1]["type"] == key:
                return row[1]
        return None

    def sort_by_price(self):
        self.robot_matrix.sort(key=lambda x: x[1]["price"])


robot_lst = RobotList()

new_robot = {
    "type": "agv",
    "price": 1000,
    "range": 50,
    "camera": 1
}
robot_lst.add_robot(new_robot)

# Dodawanie kolejnych robotów
robots_from_file = load_robots_from_file("robots.json")
for robot in robots_from_file:
    robot_lst.add_robot(robot)

print("List with more robots:")
print(robot_lst)

# Usuwanie robota
robot_to_remove = robot_lst.search_robot("agv")
if robot_to_remove:
    robot_lst.remove_robot(robot_to_remove)
    print("Matrix with robot removed:")
    print(robot_lst)
else:
    print("Robot not found in the matrix.")

# Sortowanie względem ceny
robot_lst.sort_by_price()
print("Matrix sorted by price:")
print(robot_lst)
