from robot_generator import *
import ast

class Node:
    def __init__(self, robot, key):
        self.robot = robot
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.robot}"

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, robot, key):
        new_node = Node(robot, key)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(new_node, self.root, key)

    def _insert_node(self, new_node, current_node, key):
        if new_node.robot[key] < current_node.robot[key]:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_node(new_node, current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_node(new_node, current_node.right, key)

    def search(self, value, key):
        return self._search_helper(self.root, value, key)

    def _search_helper(self, node, value, key):
        if not node or node.robot[key] == value:
            return node if node else None
        elif value < node.robot[key]:
            return self._search_helper(node.left, value, key)
        else:
            return self._search_helper(node.right, value, key)

    def remove(self, value, key):
        self.root = self._remove_helper(self.root, value, key)

    def _remove_helper(self, node, value, key):
        if not node:
            return node
        if value < node.robot[key]:
            node.left = self._remove_helper(node.left, value, key)
        elif value > node.robot[key]:
            node.right = self._remove_helper(node.right, value, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._find_min_node(node.right)
            node.robot = temp.robot
            node.key = temp.key
            node.right = self._remove_helper(node.right, temp.robot[key], key)
        return node

    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def save_tree_to_file(self, filename):
        with open(filename, "w") as file:
            self.write_node_to_file(file, self.root)

    def write_node_to_file(self, file, node):
        if node is not None:
            file.write(str(node.robot) + '\n')
            if node.left:
                file.write('L,')
                self.write_node_to_file(file, node.left)
            if node.right:
                file.write('R,')
                self.write_node_to_file(file, node.right)
            file.write('U,' + '\n')

    def load_tree_from_file(self, filename, key):
        with open(filename, "r") as file:
            lines = file.readlines()
            data = ast.literal_eval(lines.pop(0).strip())
            self.root = Node(data, key)
            self._load_node_from_file(lines, self.root)

    def _load_node_from_file(self, lines, parent_node):
        if not lines:
            return
        line = lines.pop(0).strip()
        while line:
            parts = line.split(',', 1)
            direction = parts[0]
            if direction == 'L':
                if len(parts) > 1:
                    data = ast.literal_eval(parts[1])
                    node = Node(data, parent_node.key)
                    parent_node.left = node
                    self._load_node_from_file(lines, node)
            elif direction == 'R':
                if len(parts) > 1:
                    data = ast.literal_eval(parts[1])
                    node = Node(data, parent_node.key)
                    parent_node.right = node
                    self._load_node_from_file(lines, node)
            elif direction == 'U':
                break
            if not lines:
                break
            line = lines.pop(0).strip()

    def display(self, key):
        self._display_node(self.root, key)

    def _display_node(self, node, key, indent=" "):
        if node is not None:
            print(indent + str(node.robot[key]))
            if node.left or node.right:
                self._display_node(node.left, key, indent + '  |__')
                self._display_node(node.right, key, indent + '  |__')

    def preorder_traversal(self, node, key):
        if node is not None:
            print(node.robot[key])
            self.preorder_traversal(node.left, key)
            self.preorder_traversal(node.right, key)

    def inorder_traversal(self, node, key):
        if node is not None:
            self.inorder_traversal(node.left, key)
            print(node.robot[key])
            self.inorder_traversal(node.right, key)

    def postorder_traversal(self, node, key):
        if node is not None:
            self.postorder_traversal(node.left, key)
            self.postorder_traversal(node.right, key)
            print(node.robot[key])

    def rotate_left(self, node, key):
        if node is None or node.right is None:
            return
        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        if node.robot[key] == self.root.robot[key]:
            self.root = pivot
        else:
            parent = self._find_parent(node, key)
            if parent.left == node:
                parent.left = pivot
            else:
                parent.right = pivot

    def rotate_right(self, node, key):
        if node is None or node.left is None:
            return
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        if node.robot[key] == self.root.robot[key]:
            self.root = pivot
        else:
            parent = self._find_parent(node, key)
            if parent.left == node:
                parent.left = pivot
            else:
                parent.right = pivot

    def _find_parent(self, node, key):
        current = self.root
        parent = None
        while current is not None and current != node:
            parent = current
            if node.robot[key] < current.robot[key]:
                current = current.left
            else:
                current = current.right
        return parent

    # def rotate_left(self, node_value, key):
    #     self.root = self._rotate_left(self.root, node_value, key)
    #
    # def _rotate_left(self, node, node_value, key):
    #     if node is None or node.right is None:
    #         return None
    #     if node_value == node.robot[key]:
    #         if node.right is None:
    #             return node
    #         pivot = node.right
    #         node.right = pivot.left
    #         pivot.left = node
    #         return pivot
    #     elif node_value < node.robot[key]:
    #         node.left = self._rotate_left(node.left, node_value, key)
    #     else:
    #         node.right = self._rotate_left(node.right, node_value, key)
    #     return node

    # def rotate_right(self, node_value, key):
    #     self.root = self._rotate_right(self.root, node_value, key)

    # def _rotate_right(self, node, node_value, key):
    #     if node is None:
    #         return None
    #     if node_value == node.robot[key]:
    #         if node.left is None:
    #             return node
    #         pivot = node.left
    #         node.left = pivot.right
    #         pivot.right = node
    #         return pivot
    #     elif node_value < node.robot[key]:
    #         node.left = self._rotate_right(node.left, node_value, key)
    #     else:
    #         node.right = self._rotate_right(node.right, node_value, key)
    #     return node


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
    print("Trying to find robot with price 9388")
    price_to_find = 9388
    print(tree.search(price_to_find, key_parameter))
    print("Tree loaded from file: ")
    tree.save_tree_to_file("tree2.txt")
    tree_from_file = BinarySearchTree()
    tree_from_file.load_tree_from_file("tree2.txt", key_parameter)
    tree_from_file.display(key_parameter)

    print(f"Tree with removed value: {price_to_find}: ")
    tree_from_file.remove(price_to_find, key_parameter)
    tree_from_file.display(key_parameter)



