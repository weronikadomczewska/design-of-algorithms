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

    print("Preorder traversal: ")
    tree.preorder_traversal(tree.root, key_parameter)
    print("Inorder traversal: ")
    tree.inorder_traversal(tree.root, key_parameter)
    print("Postorder traversal: ")
    tree.postorder_traversal(tree.root, key_parameter)

