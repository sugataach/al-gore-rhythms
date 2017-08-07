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
        if self.tail is None:
            self.tail = self.head

    def deleteElement(self, el):
        '''
        One drawback of a LinkedList is the lack of random access. So it's expensive to delete a random element, because first you have to traverse the List and find it.

        Retrieve and remove the given element.
        Best = O(1)
        Average = Worst = O(n)
        '''
        if self.head.data == el:
            self.removeHead()

        if self.tail.data == el:
            self.removeTail()

        # comb through the LinkedList checking for el starting from the head
        parent = None
        curr = self.head

        while curre != None and curr.data != el:
            parent = curr
            curr = curr.next

        if curr != None:
            parent.next = curr.next # remove the element from the LinkedList

        # you could return curr if you want (I chose not to)

    def removeHead(self):
        ''' O(1) '''
        if self.head == self.tail:
            self.head = self.tail = None # only 1 element in LL?
        self.head = self.head.next

    def removeTail(self):
        ''' O(n) '''
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            pointer = self.head

            while pointer != self.tail:
                pointer = pointer.next

            pointer.next = None # remove the current tail from the LL
            self.tail = pointer
