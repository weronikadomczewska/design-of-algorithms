from robot_generator import *
import json

class Node:

    """
    1 - czerwone
    0 - czarne
    """
    def __init__(self, robot, key):
        self.robot = robot
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RBTree:
    def __init__(self, robot, key):
        self.NULL = Node(robot, key)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def is_red_black_tree(tree):
        def is_red_black_tree_helper(node):
            if node == tree.NULL:
                return True
            # Property 1: Red nodes must have black children
            if node.color == 1:
                if node.left.color == 1 or node.right.color == 1:
                    return False
            left_black_height = is_red_black_tree_helper(node.left)
            right_black_height = is_red_black_tree_helper(node.right)
            # Property 4: All simple paths from a node to its descendant leaves must contain the same number of black nodes
            if left_black_height != right_black_height:
                return False
            # Property 5: Every node is either red or black
            if node.color != 0 and node.color != 1:
                return False
            # Property 2: The root node must be black
            if node == tree.root and node.color != 0:
                return False
            return left_black_height + (1 if node.color == 0 else 0)
        return is_red_black_tree_helper(tree.root) is not False

    def insert(self, robot, key):
        node = Node(robot, key)
        node.parent = None
        # node.robot = robot
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.robot[key] < x.robot[key]:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.robot[key] < y.robot[key]:
            y.left = node
        else:
            y.right = node
        if node.parent is None:
            node.color = 0
            return
        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None :
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rotate_left(node.parent.parent)
            else:
                u = node.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rotate_right(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.lefr:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rotate_left(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rotate_right(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.rotate_left(x.parent)
                    x = self.root

            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rotate_right(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.rotate_left(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent is None :
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node_helper(self, node, value, key):
        z = self.NULL
        while node != self.NULL:
            if node.robot[key] == value:
                z = node
            if node.robot[key] <= value:
                node = node.right
            else:
                node = node.left
        if z == self.NULL:
            print("Value not present in Tree")
            return
        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant (z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.fix_delete(x)

    def delete_node(self, val, key):
        self.delete_node_helper(self.root, val, key)

    def print_tree(self, key):
        self.__print_call(self.root, "", True, key)

    def __print_call(self, node, indent, last, key):
        if node is None or not isinstance(node.robot, dict):
            return

        indent_increment = "    "
        s_color = "RED" if node.color == 1 else "BLACK"
        value = node.robot.get(key, "")

        if last:
            direction = "R----"
            indent += "     "
        else:
            direction = "L----"
            indent += "|    "

        print(indent + direction, value, "(" + s_color + ")")
        self.__print_call(node.left, indent, False, key)
        self.__print_call(node.right, indent, True, key)

    # def print_tree(self, key):
    #     self.__print_call(self.root, "", True, key)
    #
    # def __print_call(self, node, indent, last, key):
    #     if node is None:
    #         return
    #
    #     indent_increment = "    "
    #     s_color = "RED" if node.color == 1 else "BLACK"
    #     value = node.robot[key] if key in node.robot else ""
    #
    #     if last:
    #         direction = "R----"
    #         indent += "     "
    #     else:
    #         direction = "L----"
    #         indent += "|    "
    #
    #     print(indent + direction, value, "(" + s_color + ")")
    #     self.__print_call(node.left, indent, False, key)
    #     self.__print_call(node.right, indent, True, key)

    def save_rbtree_to_file(self, filename):
        def get_node_reference(node):
            if node is None:
                return None
            return id(node)

        def serialize_node(node):
            if node is None:
                return None
            return {
                'id': id(node),
                'robot': node.robot,
                'key': node.key,
                'parent': get_node_reference(node.parent),
                'left': get_node_reference(node.left),
                'right': get_node_reference(node.right),
                'color': node.color
            }

        tree_dict = {
            'root': get_node_reference(self.root),
            'NULL': id(self.NULL),
            'nodes': {}
        }

        # Traverse the tree to collect all node references
        def traverse_tree(node):
            if node is None:
                return
            tree_dict['nodes'][id(node)] = serialize_node(node)
            traverse_tree(node.left)
            traverse_tree(node.right)

        traverse_tree(self.root)

        serialized_tree = json.dumps(tree_dict)
        with open(filename, 'w') as file:
            file.write(serialized_tree)


    def load_rbtree_from_file(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        nodes = {}
        for node_id, node_data in data['nodes'].items():
            node = Node(node_data['robot'], node_data['key'])
            node.parent = nodes.get(int(node_data['parent'])) if node_data['parent'] is not None else None
            node.color = int(node_data['color'])
            nodes[int(node_id)] = node

        for node_id, node_data in data['nodes'].items():
            node = nodes[int(node_id)]
            node.left = nodes.get(int(node_data['left'])) if node_data['left'] is not None else None
            node.right = nodes.get(int(node_data['right'])) if node_data['right'] is not None else None

        root_id = int(data['root'])
        root = nodes[root_id]

        return RBTree(root, root.key)

    # def load_rbtree_from_file(filename):
    #
    #     def deserialize_node(node_data, node_map):
    #         if node_data is None:
    #             return None
    #
    #         node_id = node_data['id']
    #         robot_data = node_data['robot']
    #         key = node_data['key']
    #         color = node_data['color']
    #         left_id = node_data['left']
    #         right_id = node_data['right']
    #
    #         robot = {
    #             "type": robot_data['type'],
    #             "price": robot_data['price'],
    #             "range": robot_data['range'],
    #             "camera": robot_data['camera']
    #         }
    #         node = Node(robot, key)
    #         node.color = color
    #
    #         node.left = node_map.get(left_id)
    #         if node.left is not None:
    #             node.left.parent = node
    #
    #         node.right = node_map.get(right_id)
    #         if node.right is not None:
    #             node.right.parent = node
    #
    #         node_map[node_id] = node
    #
    #         return node
    #
    #     with open(filename, 'r') as file:
    #         serialized_tree = file.read()
    #
    #     tree_dict = json.loads(serialized_tree)
    #     root_id = tree_dict['root']
    #     null_id = tree_dict['NULL']
    #     nodes_data = tree_dict['nodes']
    #
    #     node_map = {}
    #     for node_id, node_data in nodes_data.items():
    #         node = deserialize_node(node_data, node_map)
    #         node_map[node_id] = node
    #
    #     root_node = node_map[root_id]
    #     NULL = node_map[null_id]
    #
    #     tree = RBTree(NULL.robot, NULL.key)
    #     tree.root = root_node
    #     tree.NULL = NULL
    #
    #     return tree


if __name__ == "__main__":
    robots = load_robots_from_file("robots.json")
    key = "price"
    bst = RBTree(robots[0], key)
    for i in range(1, len(robots)):
        bst.insert(robots[i], key)
    bst.print_tree(key)
    print("Is this tree R-B?: ", bst.is_red_black_tree())
    print("After deleting an element")
    bst.delete_node(9388, key)
    bst.print_tree(key)
    print("Tree from file: ")
    bst.save_rbtree_to_file('tree.json')
    loaded_bst = RBTree.load_rbtree_from_file('tree.json')
    loaded_bst.print_tree(key)
