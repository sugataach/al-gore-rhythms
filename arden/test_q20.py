'''
Given a binary tree of integers, print it in level order. The output will contain space between the numbers in the same level, and new line between different levels.

Approach:

Given a root, you want to walk through the tree using breadth first search.

How does BFS work?

Initialize a Queue and append the root
Initialize a current level counter and next level counter
While the Queue is not empty:
    - pop from Queue, decrement current level counter, print node value
    - check for Left & Right children and append them to Queue
    - increment next level counter

Time -> O(n), you will need to walk through the whole list

Space -> O((n+1)/2) -> O(n), the last level of a complete binary tree will contain approx half the nodes, which is still O(n)
'''
import pytest
import collections

class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    result = []
    if root is None:
        return result

    q = collections.deque([root])
    curr_count, next_count = 1, 0
    curr_str = ''

    while q:
        node = q.popleft()
        curr_count -= 1
        # print(node.val, end='')
        curr_str += str(node.val)
        if node.left:
            q.append(node.left)
            next_count += 1
        if node.right:
            q.append(node.right)
            next_count += 1
        if curr_count == 0:
            result.append(curr_str)
            result.append('\n')
            # print('\n', end='')
            curr_str = ''
            curr_count, next_count = next_count, curr_count
    return result

def test_level_order():
    # initialize a binary tree
    '''
            1
        2       3
      4       5   6
    '''
    tree = BSTNode(1, BSTNode(2, BSTNode(4)), BSTNode(3, BSTNode(5), BSTNode(6)))
    result = ['1','\n','23','\n','456','\n']
    assert(level_order(tree)) == result
