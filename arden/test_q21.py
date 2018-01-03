'''
Given a binary tree of integers, print it in reverse level order, starting from the bottom level to the root. The output will contain space between the numbers in the same level, and new line between different levels.

Approach:

Given a root, you want to walk through the tree using breadth first search.

But keep a stack to store the elements as you walk thorugh the tree. Use the stack to print the elements in reverse order after you've finished BFS.

How does BFS work?

Initialize a Queue and append the root
Initialize a current level counter and next level counter
While the Queue is not empty:
    - pop from Queue, decrement current level counter, print node value
    - check for Right, then Left*(note that you need to store the right first) children and append them to Queue
    - increment next level counter

Iterate through stack and print the elems

Time -> O(n) + O(n) -> 2*O(n) -> O(n), you will need to walk through the whole tree and then the whole stack

Space -> O((n+1)/2) + O(n) -> O(n), the last level of a complete binary tree will contain approx half the nodes, plus all the nodes from the binary tree in the stack, which is just a constant times O(n)
'''
import pytest
import collections

class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverse_level_order(root):
    result = []
    if root is None:
        return result

    q = collections.deque([root])
    s = [] # stack will hold our elements to be printed
    curr_count, next_count = 1, 0

    while q:
        node = q.popleft()
        curr_count -= 1
        s.append(str(node.val))
        if node.right:
            q.append(node.right)
            next_count += 1
        if node.left:
            q.append(node.left)
            next_count += 1
        if curr_count == 0:
            s.append('\n')
            curr_count, next_count = next_count, curr_count
    return s

def test_reverse_level_order():
    # initialize a binary tree
    '''
            1
        2       3
      4       5   6
    '''
    tree = BSTNode(1, BSTNode(2, BSTNode(4)), BSTNode(3, BSTNode(5), BSTNode(6)))
    result = ['1','\n','3','2','\n','6','5','4','\n']
    assert(reverse_level_order(tree)) == result
