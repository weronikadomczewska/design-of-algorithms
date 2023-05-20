from robot_generator import *

class RobotQueue:
    def __init__(self, maxsize):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.maxsize = maxsize

    def __repr__(self):
        return repr(print_list_of_robots_as_table(self.queue))

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        if self.head == self.tail:
            return len(self.queue) == self.maxsize
        tmp = (self.tail + 1) % self.maxsize
        return self.head == tmp

    def enqueue(self, robot):
        if self.is_full():
            raise OverflowError("Queue is already full")
        self.queue.append(robot)
        self.tail = (self.tail + 1) % len(self.queue)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        tmp = self.queue[self.head]
        self.head = (self.head + 1) % self.maxsize
        self.queue = self.queue[1:]
        return tmp

    def clear_queue(self):
        cleared_robots = self.queue[:]
        self.queue = []
        self.head = 0
        self.tail = 0
        return cleared_robots


if __name__ == "__main__":
    robot_queue = RobotQueue(10)
    print("Trying to dequeue robot from empty queue: ")
    try:
        first_robot = robot_queue.dequeue()
    except IndexError:
        print("The queue is empty, cannot remove a robot")

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
    print("Queue with one robot added: ")
    robot_queue.enqueue(new_robot)
    print(robot_queue)
    print("Queue with more robots added: ")
    robots_from_file = load_robots_from_file("robots.json")
    for robot in robots_from_file[:9]:
        robot_queue.enqueue(robot)
    print(robot_queue)
    print("First robot from the queue: ")
    print(robot_queue.dequeue())
    print("Queue with dequeued robot: ")
    print(robot_queue)
    print("Cleared queue: ")
    cleared_robots = print_list_of_robots_as_table(robot_queue.clear_queue())
    print(robot_queue)
    print("Removed robots: ")
    print(cleared_robots)


