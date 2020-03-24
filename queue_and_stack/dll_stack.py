import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
Stacks are a last in, first out (LIFO) based data structure.
push: adds an element to the collection
pop: removes the most recently added element that was not yet removed.

https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
"""

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size


# Why is our DLL a good choice to store our elements?
"""
(1) The size of the arrays is fixed: So we must know the upper limit on the number 
of elements in advance. Also, generally, the allocated memory is equal to the upper
 limit irrespective of the usage, and in practical uses, the upper limit is rarely reached.

(2) Inserting a new element in an array of elements is expensive because a room has
 to be created for the new elements and to create room existing elements have to be shifted.
"""