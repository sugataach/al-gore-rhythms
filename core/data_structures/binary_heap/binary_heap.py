"""
Implement a (min-heap) binary heap (without decrease key)

Properties:
- is a balanced binary tree -> left & right subtrees are roughly the same size (differ at most by 1 level)
- we keep the tree balanced by enforcing the complete tree property:
    - every level except for possibly the last has 2 children
    - all nodes are as far left as possible

- represented as a list
- n = index of node
- parent = n // 2, left_child = 2n, right_child = 2n + 1
- heap order property: for any node n, the parent is smaller or equal to n
"""

class BinaryHeap(object):
    def __init__(self):
        self.data = [0] # 0 is the 1st element b/c of operations involving integer division
        self.size = 0

    def insert(self, n):
        '''
        Add to the bottom of the heap and percolate up.
        O(1)
        '''
        self.data.append(n)
        self.size += 1
        self.percUp(self.size)

    def percUp(self, idx):
        '''
        Integer divide the size, then compare to parent and
        swap if the parent is bigger than the element.
        '''
        i = idx // 2
        while i > 0:
            if self.data[i] > self.data[idx]:
                self.data[i], self.data[idx] = self.data[idx], self.data[i]
            idx = idx // 2 # go up the new position of the inserted element

    def removeMin(self, elem):
        '''
        Remove the min element.
        Replace with last element.
        Percolate down.
        O(n)
        '''
        top = self.data[1]
        self.data[1] = self.data[self.size] # replace with last elem
        self.size -= 1
        self.data.pop() # remove duplicate last element
        self.percDown(1) # start moving the element down so that you can re-balance the tree
        return top

    def percDown(self, idx):
        '''
        Check the node's children, and get the minChild.
        If the node > minChild -> swap
        Update idx, to be the new position.
        Keep going until you reach the bottom of the heap.
        '''
        while (idx * 2) <= self.size: # check if there is actually a left tree
            minChild = self.getMinChild(idx)
            if self.data[idx] > self.data[minChild]: # check if the current node is greater than the minChild, if so swap
                self.data[idx], self.data[minChild] = self.data[minChild], self.data[idx]
            idx = minChild

    def getMinChild(self, idx):
        '''
        If R_index > Size of Array -> return L_index  (i.e. there is no right lol)
        If data[L] < data[R] -> return L_index
        Else return R_index
        '''
        if idx*2+1 > self.size: # check if there is a right subtree
            return idx * 2
        else:
            if self.data[idx*2] < self.data[idx*2+1]:
                return idx * 2
            else:
                return idx * 2 + 1

    def convertList(self, arr):
        '''
        Takes a list and converts it to a min-heap.
        O(n)
        '''
        i = len(arr) // 2 # starts with the middle of the list a.k.a. 1 level above the leaf nodes -> no children since it's a complete binary tree
        self.size = len(arr)
        self.data = [0] + arr
        while i > 0:
            self.percDown(i)
            i -= 1
