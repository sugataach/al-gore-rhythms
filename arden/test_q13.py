'''
Given a stream of unsorted integers, find the median element in sorted order at any given time.

So, we will be receiving a continuous stream of numbers in some random order and we don’t know the stream length in advance.

Write a function that finds the median of the already received numbers efficiently at any time. We will be asked to find the median multiple times. Just to recall, median is the middle element in an odd length sorted array, and in the even case it’s the average of the middle elements.

Approach:

2 heap solution -> max heap & min heap

2 properties to maintain:
    - size (max heap can only be 1 element more than min heap at any given time)
    - order (max heap root must be smaller than or equal to min heap root at any given time)

--- Insertion ---
If there are an even (N%2=0) # of elements in heap
    - Insert into the heap (percUp), increment element count
    - IF the max heap root > min heap root
        - If YES, swap the roots

If there are an odd (N%2=1) # of elements in heap
    - Insert into max heap (now there's even #), increment count
    - Pop the max heap root and insert it into the min heap

--- Median ---
If there's an even number of elements -> average of max heap root & min heap root
If there's an odd number of elements -> it's the max heap root

Example -> 1, 6, 4, 3, 5

-- Insert 1 --

Max             Min
(-1)            ()

-- Insert 6 --

Max             Min
(-6)            ()
(-1)

(-1)            (6)

-- Insert 4 --

Max             Min
(-4)            (6)
(-1)

-- Insert 3 --

Max             Min
(-4)            (6)
(-3)
(-1)

(-3)            (4)
(-1)            (6)

-- Insert 5 --

Max             Min
(-5)            (4)
(-3)            (6)
(-1)

(-4)            (5)
(-3)            (6)
(-1)

'''
import pytest
import heapq

class streamMedian:
    def __init__(self):
        self.min_heap, self.max_heap = [], []
        self.N = 0

    def insert(self, elem):
        if self.N%2 == 0:
            heapq.heappush(self.max_heap, -1*elem)
            self.N += 1

            if len(self.min_heap) == 0:
                return

            # if the root of the max_heap is > root of the min_heap
            if -1*self.max_heap[0] > self.min_heap[0]:
                # swap roots
                max_heap_root = -1*heapq.heappop(self.max_heap)
                min_heap_root = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -1*min_heap_root)
                heapq.heappush(self.min_heap, max_heap_root)

        else:
            # pop the max heap and insert into the min heap
            max_elem = -1*heapq.heappushpop(self.max_heap, -1*elem)
            heapq.heappush(self.min_heap, max_elem)
            self.N += 1

    def median(self):
        if self.N%2 == 0:
            max_heap_root = -1*self.max_heap[0]
            min_heap_root = self.min_heap[0]
            return (max_heap_root+min_heap_root)/2.0
        else:
            return -1*self.max_heap[0]

def test_stream_median():
    stream_listener = streamMedian()
    stream_listener.insert(1)
    stream_listener.insert(6)
    stream_listener.insert(4)
    stream_listener.insert(3)
    assert stream_listener.median() == 3.5

    stream_listener.insert(5)
    assert stream_listener.median() == 4
