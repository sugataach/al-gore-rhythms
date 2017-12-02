'''
Given a binary tree, check whether it’s a binary search tree or not.

Approach A:
Iterate through the entire tree looking for contradictions
    - False if Left Child > Right Child

Approach B:
Iterate

'''
import pytest

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)

def is_bst(root, minValue=None, maxValue=None):
    if root is None:
        return True

    if not minValue <= root.value <= maxValue:
        return False

    return is_bst(root.left, minValue, root.value) and \
           is_bst(root.right, root.value, maxValue)

def test_is_bst():
    # build an illegal tree
    bst = Node(3, Node(2, Node(1), Node(4)), Node(5))
    assert(is_bst(bst, float('-infinity'), float('infinity'))) == False

    bst = Node(5, Node(3, Node(2), Node(5)), Node(7, None, Node(8)))
    assert(is_bst(bst, float('-infinity'), float('infinity'))) == True
