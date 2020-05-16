from queue import Queue, LifoQueue


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if (self.root == None):
            self.root = BinaryNode(data)
        else:
            self.insert(self.root, data)

    def insert(self, node, data):
        queue = Queue()
        queue._put(node)
        while queue.empty() is not True:
            current_node = queue.get_nowait()
            if current_node.left:
                queue._put(current_node.left)
            else:
                current_node.set_left(BinaryNode(data))
                break

            if current_node.right:
                queue._put(current_node.right)
            else:
                current_node.set_right(BinaryNode(data))
                break
class Node:
    def __init__(self, data):
        self.data = data;

    def to_string(self):
        return 'Node [ ', self.data, ']'


class BinaryNode(Node):
    def __init__(self, data):
        super(BinaryNode, self).__init__(data)
        self.left = None
        self.right = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def to_string(self):
        return 'BinaryNode[ ' + str(self.data) + " --> { " + str(self.left.data) + " : " + str(self.right.data) + '} ]'
