from ex2 import BinarySearchTree
from robot_generator import *

if __name__ == "__main__":
    robots = load_robots_from_file("robots.json")
    tree = BinarySearchTree()
    # key_parameter = input("enter key parameter: ")
    # while key_parameter not in ["price", "type", "range", "camera"]:
    #     key_parameter = input("enter key parameter again: ")
    key_parameter = "price"
    for robot in robots:
        tree.insert(robot, key_parameter)
    print("Tree with robots: ")
    tree.display(key_parameter)

print("Left rotated tree on node 9388:")
left_rotated_tree = BinarySearchTree()
for robot in robots:
    left_rotated_tree.insert(robot, key_parameter)
#
left_rotated_tree.rotate_left(9388, key_parameter)
left_rotated_tree.display(key_parameter)

print("Right rotated tree on node 5882:")
right_rotated_tree = BinarySearchTree()
for robot in robots:
    right_rotated_tree.insert(robot, key_parameter)

right_rotated_tree.rotate_right(5882, key_parameter)
right_rotated_tree.display(key_parameter)
