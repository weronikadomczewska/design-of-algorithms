from robot_generator import *

class RobotNode:
    def __init__(self, robot_type, price, range, camera):
        self.prev = None
        self.data = {"type": robot_type, "price": price, "range": range, "camera": camera}
        self.next = None

    def __repr__(self):
        return f"({self.data['type']}, {self.data['price']}, {self.data['range']}, {self.data['camera']})"

class RobotList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return f"[{', '.join(nodes)}]"

    def add_robot(self, robot):
        if not self.head:
            self.head = robot
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = robot
            robot.prev = current

    def remove_robot(self, robot):
        current = self.head
        while current:
            if current.data == robot:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current is self.head:
                    self.head = current.next
                break
            current = current.next
        del robot

    def search_robot(self, key):
        current = self.head
        while current:
            if current.data["type"] == key:
                return current
            current = current.next
        return None

    def sort_by_price(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_robot = current.next
            if sorted_head is None or current.data["price"] < sorted_head.data["price"]:
                current.prev = None
                current.next = sorted_head
                if sorted_head:
                    sorted_head.prev = current
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and current.data["price"] >= temp.next.data["price"]:
                    temp = temp.next
                current.prev = temp
                current.next = temp.next
                if temp.next:
                    temp.next.prev = current
                temp.next = current
            current = next_robot

        self.head = sorted_head


if __name__ == "__main__":
    robot_lst = RobotList()
    new_robot = RobotNode("agv", 1000, 50, 1)
    robot_lst.add_robot(new_robot)
    print("List with one robot added: ")
    print(robot_lst)
    robots_from_file = load_robots_from_file("robots.json")
    for robot in robots_from_file:
        new_robot = RobotNode(robot['type'], robot['price'], robot['range'], robot['camera'])
        robot_lst.add_robot(new_robot)

    print("List with more robots: ")
    print(robot_lst)
    robot_lst.remove_robot(new_robot)
    print("List with first robot removed: ")
    print(robot_lst)

