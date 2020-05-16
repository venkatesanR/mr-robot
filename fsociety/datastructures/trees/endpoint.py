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
    tree.add(9)
    tree.add(10)
    tree.add(11)
    tree.add(12)
    tree.add(14)
    tree.add(15)
    tree.add(15)
    tree.add(17)
    tree.add(18)

    traversal = BinaryTraversal()
    print("Print level by Reverse Ordering")
    traversal.level_order(tree.root, reverse=True)
    print("\nPrint level by Natural Ordering")
    traversal.level_order(tree.root)
    print('\nHeight Of the Tree: ', traversal.height(tree.root))
    print("Deepest Node: ", traversal.deepest_by_level(tree.root))
    print("Identical: ", traversal.is_identical(tree.root, tree.root))
    print("Diameter: ", traversal.diameter(tree.root))
