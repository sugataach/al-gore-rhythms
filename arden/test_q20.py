'''
Given a binary tree of integers, print it in level order. The output will contain space between the numbers in the same level, and new line between different levels.

Approach:

Given a root, you want to walk through the tree using breadth first search

How does BFS work?


'''
import pytest
import collections

class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):


def test_level_order():
