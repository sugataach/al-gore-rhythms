'''
Given a linkedlist of integers and an integer value, delete every node of the linkedlist containing that value.

Approach A:

iterate through linkedlist, keeping a pointer to the current and prev nodes
when curr.val == integer, prev.next = curr.next, curr = prev.next
'''
import pytest

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, node_value=None):
        if node_value == None:
            self.head = self.tail = None
        else:
            self.head = Node(node_value)
            self.tail = self.head

    def add(self, value):
        self.tail.next = self.tail = Node(value)

    def remove(self, remove_value):
        curr_node = self.head
        prev_pointer = None
        while curr_node:
            if curr_node.value == remove_value:
                if prev_pointer == None:
                    self.head = curr_node.next
                    prev_pointer = curr_node
                else:
                    prev_pointer.next = curr_node.next
                    curr_node = curr_node.next
            else:
                prev_pointer = curr_node
                curr_node = curr_node.next

    def get_list(self):
        if self.head == None:
            return []
        result = []
        curr_node = self.head
        while curr_node:
            result.append(curr_node.value)
            curr_node = curr_node.next
        return result

def test_remove_node():
    # standard case
    linked_list = LinkedList(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.remove(3)
    assert linked_list.get_list() == [1,2,4]

    # delete from head
    linked_list = LinkedList(1)
    linked_list.add(2)
    linked_list.remove(1)
    assert linked_list.get_list() == [2]

    # delete from tail
    linked_list = LinkedList(1)
    linked_list.add(2)
    linked_list.remove(2)
    assert linked_list.get_list() == [1]

    # one node case
    linked_list = LinkedList(1)
    linked_list.remove(1)
    assert linked_list.get_list() == []

    # empty case
    linked_list = LinkedList()
    assert linked_list.get_list() == []

    # empty remove case
    linked_list = LinkedList()
    linked_list.remove(4)
    assert linked_list.get_list() == []

    # missing case
    linked_list = LinkedList(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(3)
    linked_list.remove(4)
    assert linked_list.get_list() == [1,2,3,3]
