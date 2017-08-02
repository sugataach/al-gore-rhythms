"""
Implement a Singly Linked List, with all the trimmings.

Interesting facts:
- it is a data structure that allows access to a collection of data using pointers/references
- is very similar to an array but arrays are stored in a continguous block of memory
- nodes of a linked list can be stored anywhere (because of node references)
- insertion in a linked list (in the middle) is inexpensive (compared to an array) because all you need to do change the node references
- whereas inserting into an array requires shifting all subsequent elements and/or creating a new array
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, data):
        '''
        Add an element after current tail, so that it becomes the new tail.
        Best = Average = Worst = O(1)
        '''
        # if the Tail is None, then Head is None => addToHead
        if self.tail is None:
            addToHead(data)
        # otherwise make the current Tail point to a new Node
        self.tail.next = self.tail = Node(data)

    def addToHead(self, data):
        '''
        Add an element before the current head so that it becomes the new head.
        Best = Average = Worst = O(1)
        '''
        # make the Head equal to a new Node (which point to the currrent head)
        self.head = Node(data, self.head)
        # if the Tail is empty, make it equal to the Head
        is self.tail is None:
            self.tail = self.head

    def 
