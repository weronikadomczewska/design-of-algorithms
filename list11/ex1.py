class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data, parent_data=None, is_left_child=True):
        if self.root is None:
            self.root = Node(data)
        else:
            parent_node = self._find_node(self.root, parent_data)
            if parent_node:
                if is_left_child and parent_node.left is None:
                    parent_node.left = Node(data)
                elif not is_left_child and parent_node.right is None:
                    parent_node.right = Node(data)
                else:
                    print("Cannot insert the node to the given parent")
            else:
                print("Cannot find parent node")

    def _find_node(self, current_node, data):
        if current_node is None:
            return None
        if current_node.data == data:
            return current_node
        left_result = self._find_node(current_node.left, data)
        if left_result:
            return left_result
        right_result = self._find_node(current_node.right, data)
        return right_result

    def remove_node(self, data):
        if self.root is None:
            print("Tree is empty.")
            return
        self.root = self._remove_node_recursive(self.root, data)

    def _remove_node_recursive(self, current, data):
        if current is None:
            return None
        if current.data == data:
            return None
        current.left = self._remove_node_recursive(current.left, data)
        current.right = self._remove_node_recursive(current.right, data)

        if current.left is not None and current.left.data == data:
            current.left = None

        if current.right is not None and current.right.data == data:
            current.right = None

        return current

    def display_tree(self):
        self._display_node(self.root)

    def _display_node(self, node, indent=" "):
        if node is not None:
            print(indent + str(node.data))
            self._display_node(node.left, indent + '  |__')
            self._display_node(node.right, indent + '  |__')

    def save_tree_to_file(self, filename):
        with open(filename, "w") as file:
            self.write_node_to_file(file, self.root)

    def write_node_to_file(self, file, node):
        if node is not None:
            file.write(str(node.data) + '\n')
            if node.left:
                file.write('L,' + str(node.left.data) + '\n')
                self.write_node_to_file(file, node.left)
            if node.right:
                file.write('R,' + str(node.right.data) + '\n')
                self.write_node_to_file(file, node.right)
            file.write('U,' + '\n')

    def load_tree_from_file(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            data = lines.pop(0).strip()
            self.root = Node(int(data))
            self._load_node_from_file(lines, self.root)

    def _load_node_from_file(self, lines, parent_node):
        if not lines:
            return
        line = lines.pop(0).strip()
        while line != 'U,':
            parts = line.split(',')
            direction = parts.pop(0)
            if direction == 'L':
                if parts:
                    data = parts.pop(0)
                    node = Node(int(data))
                    parent_node.left = node
                    self._load_node_from_file(lines, node)
            elif direction == 'R':
                if parts:
                    data = parts.pop(0)
                    node = Node(int(data))
                    parent_node.right = node
                    self._load_node_from_file(lines, node)
                    if parts:
                        data = parts.pop(0)
                        node = Node(int(data))
                        parent_node.right.right = node
                        self._load_node_from_file(lines, node)
            if not lines:
                break
            line = lines.pop(0).strip()


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add_node(1)
    tree.add_node(2, 1)
    tree.add_node(3, 1, False)
    tree.add_node(4, 2)
    tree.add_node(5, 2, False)
    tree.add_node(6, 3)
    tree.add_node(7, 3, False)
    tree.add_node(8, 4)
    tree.add_node(9, 4, False)
    print("Original tree: ")
    tree.display_tree()

    tree.save_tree_to_file("tree.txt")
    tree_from_file = BinaryTree()
    tree_from_file.load_tree_from_file("tree.txt")
    print("Tree from file: ")
    tree_from_file.display_tree()

    print("Tree with deleted node: ")
    tree_from_file.remove_node(4)
    tree_from_file.display_tree()
