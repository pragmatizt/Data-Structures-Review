import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
Queue'ing is a first in, first out (FIFO) based data structure.
Enqueue: adding to a queue of such items (in FIFO's case, tail)
Dequeue: deleting elements from a queue (in FIFO's case, head)
"""

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):   # add
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):          # delete
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size


# Why is our DLL a good choice to store our elements?
"""
(1) The size of the arrays is fixed: So we must know the upper limit on the number 
of elements in advance. Also, generally, the allocated memory is equal to the upper
 limit irrespective of the usage, and in practical uses, the upper limit is rarely reached.

(2) Inserting a new element in an array of elements is expensive because a room has
 to be created for the new elements and to create room existing elements have to be shifted.


ALSO, from lecture -- 
because the only elements you need to access are the front and end, so an array is 
unnecessarily complicated
"""
