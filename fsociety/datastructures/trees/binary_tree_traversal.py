from queue import Queue, LifoQueue

from datastructures.trees.binary_tree import BinaryNode


class BinaryTraversal:
    def __init__(self):
        pass

    def deepest_by_level(self, node):
        queue: Queue[BinaryNode] = Queue()
        queue._put(node)
        current_node = None
        while not queue.empty():
            current_node = queue.get_nowait()
            if current_node.left:
                queue._put(current_node.left)
            if current_node.right:
                queue._put(current_node.right)
        return current_node.data

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
                print(current_node.data, end=" ")

            if current_node.left:
                queue._put(current_node.left)
            if current_node.right:
                queue._put(current_node.right)
        if reverse is True:
            while not stack.empty():
                print(stack.get_nowait(), end=" ")

    def is_identical(self, this_tree, that_tree):
        if that_tree is None and that_tree is None:
            return True
        if that_tree is None or this_tree is None:
            return False
        return that_tree.data == this_tree.data and self.is_identical(this_tree.left,
                                                                      that_tree.left) and self.is_identical(
            this_tree.right, that_tree.right)

    def diameter(self, node):
        if not node:
            return 0
        else:
            left_length = 0
            right_length = 0
            left_length += self.diameter(node.left)
            right_length += self.diameter(node.right)
            print(str(left_length), str(right_length))
            return max(left_length + 1, right_length + 1)
