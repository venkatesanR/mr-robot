from queue import Queue, LifoQueue

from datastructures.trees.binary_tree import BinaryNode


class BinaryTraversal:
    def __init__(self):
        pass

    def height(self, node):
        if not node:
            return 0
        left = 0
        right = 0
        left += self.height(node.left)
        right += self.height(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def in_order(self, node):
        if node is None:
            return
        print(node.data)
        self.in_order(node.left)
        self.in_order(node.right)

    def level_order(self, node, reverse=False):
        queue: Queue[BinaryNode] = Queue()
        queue._put(node)
        if reverse is True:
            stack = LifoQueue()
        while not queue.empty():
            current_node = queue.get_nowait()
            if reverse is True:
                stack._put(current_node.data)
            else:
                print(current_node.data)

            if current_node.left:
                queue._put(current_node.left)
            if current_node.right:
                queue._put(current_node.right)
        if reverse is True:
            while not stack.empty():
                print(stack.get_nowait())
