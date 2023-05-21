from robot_generator import *

class RobotStack:
    def __init__(self, maxsize):
        self.stack = []
        self.top = -1
        self.maxsize = maxsize

    def __repr__(self):
        return repr(print_list_of_robots_as_table(self.stack))

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.maxsize - 1

    def add_robot(self, robot):
        if self.is_full():
            raise OverflowError("Stack is already full")
        self.stack.append(robot)
        self.top += 1

    def pop_robot(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped_robot = self.stack.pop()
        self.top -= 1
        return popped_robot

    def clear_stack(self):
        cleared_robots = self.stack[:]
        self.stack = []
        self.top = -1
        return cleared_robots


if __name__ == "__main__":
    robot_stack = RobotStack(10)
    print("Trying to remove robot from empty stack: ")
    try:
        last_robot = robot_stack.pop_robot()
    except IndexError:
        print("The stack is empty, cannot remove a robot")

    new_robot = {
        "type": "agv",
        "price": 1000,
        "range": 50,
        "camera": 1
    }
    # new_robot_type = ""
    # new_robot_price = -1
    # new_robot_range = -1
    # new_robot_camera = -1
    #
    # while new_robot_type not in ["agv", "afv", "asv", "auv"]:
    #     new_robot_type = input("Enter robot type: ")
    #
    # while new_robot_price not in range(0, 10001):
    #     new_robot_price = int(input("Enter robot price: "))
    #
    # while new_robot_range not in range(0, 101):
    #     new_robot_range = int(input("Enter robot range: "))
    #
    # while new_robot_camera not in [0, 1]:
    #     new_robot_camera = int(input("Enter robot camera: "))
    #
    # new_robot["type"] = new_robot_type
    # new_robot["price"] = new_robot_price
    # new_robot["range"] = new_robot_range
    # new_robot["camera"] = new_robot_camera
    #
    print("Stack with one robot added: ")
    robot_stack.add_robot(new_robot)
    print(robot_stack)
    print("Stack with more robots added: ")
    robots_from_file = load_robots_from_file("robots.json")
    for robot in robots_from_file[:9]:
        robot_stack.add_robot(robot)
    print(robot_stack)
    print("Last robot from the stack: ")
    print(robot_stack.pop_robot())
    print("Stack with removed robot: ")
    print(robot_stack)
    print("Cleared stack: ")
    cleared_robots = print_list_of_robots_as_table(robot_stack.clear_stack())
    print(robot_stack)
    print("Removed robots: ")
    print(cleared_robots)





