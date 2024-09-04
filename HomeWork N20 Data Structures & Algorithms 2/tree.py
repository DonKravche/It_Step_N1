
from ast import NodeVisitor


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def printParents(self):
        print("The Parents Of Each Node Are")
        self._printParents(self.root, None)

    def _printParents(self, node, parent):
        if node is not None:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "->", parent.key)

            self._printParents(node.left, node)
            self._printParents(node.right, node)

    def printChildren(self):
        print("The Children Of Each Node Are")
        self._printChildren(self.root)

    def _printChildren(self, node):
        if node is not None:
            print(node.key, "->", end='')
            if node.left is not None:
                print(node.left.key, ' ', end='')

            if node.right is not None:
                print(node.right.key, ' ', end='')

            print()
            self._printChildren(node.left)
            self._printChildren(node.right)

    def printLeadNode(self):
        print("The Leading Node Of Each Node Are: ")
        self._printLeafNodes(self.root)

    def _printLeafNodes(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.key, end=" ")

            self._printLeafNodes(node.left)
            self._printLeafNodes(node.right)

    def countEdges(self):
        edges = max(0, self._countNodes(self.root) - 1)
        print(f"The number of Edges in the tree is: {edges}")
        return edges

    def _countNodes(self, node):
        if node is None:
            return 0
        return 1 + self._countNodes(node.left) + self._countNodes(node.right)


binary_tree = BinaryTree()
binary_tree.insert(10)
binary_tree.insert(15)
binary_tree.insert(9)
binary_tree.insert(16)
binary_tree.insert(17)
binary_tree.insert(12)
# binary_tree.printParents()
binary_tree.printChildren()

binary_tree.printLeadNode()
binary_tree.countEdges()