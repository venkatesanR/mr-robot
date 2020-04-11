from binary_tree import BinaryTree

from datastructures.trees.binary_tree_traversal import BinaryTraversal

if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    traversal = BinaryTraversal()
    traversal.level_order(tree.root, reverse=True)
    print('Height Of the Tree: ', traversal.height(tree.root))
