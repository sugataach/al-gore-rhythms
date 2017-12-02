'''
Implement a Binary Search Tree, where the node values are integers.

Insert -> O(logN) (worst case -> O(n), since BST can degrade to a linked list)
Delete -> O(logN)
Search -> O(logN)
'''

class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, num):
        pass

    def delete(self, num):
        pass

    def search(self, num):
        pass

    def preorder(self):
        pass

    def preorder_iterative(self):
        pass

    def postorder(self):
        pass

    def postorder_iterative(self):
        pass

    def inorder(self):
        pass

    def inorder_iterative(self):
        pass

    def levelorder(self):
        pass

    def levelorder_iterative(self):
        pass
