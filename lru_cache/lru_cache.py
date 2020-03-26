# Imports
from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # Link to the list 
        self.order = DoublyLinkedList()
        # We have a limit above
        self.limit = limit
        # Counter
        self.size = 0
        # Create a dictionary 
        self.storage_dict = {}  

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Returns the value associated with the key or none
        ## A check is done to see if the key is in the storage dictionary
        if key in self.storage_dict:
            # Identify the value of the node based on the key from the dictionary
            
            node = self.storage_dict[key]
            
            # Move the node to the end of the linked list
            self.order.move_to_end(node)

            # print(node)
            # print(node.value)   
            # print(node.value[1])
            # print(node.value[0])

            # returns the node's value (which is same as key)
            return node.value[1]  
        else:
            # none if the key-value pair doesn't exist
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Storing
        ## A check is done to see if the key is in the storage dictionary
        if key in self.storage_dict:
            # Identify the value of the node based on the key from the dictionary
            node = self.storage_dict[key]

            # Set the node value to the key value pair
            node.value = (key, value)
            
            # Move the node to the end of the linked list
            return self.order.move_to_end(node)

        # If cache is at max capacity before entry is added
        if len (self.order) == self.limit:
            # Remove oldest entry in STORAGE to make room
            del self.storage_dict[self.order.head.value[0]]
            # After, we remove from tail on LINKED LIST
            self.order.remove_from_tail()

        # add to tail newest Value on LINKED LIST
        self.order.add_to_tail((key, value))
        # Make the STORAGE match with the LINKED LIST order
        self.storage_dict[key] = self.order.tail














# def set(self, key, value):
# 	if key in self.storage_dict:
# 		node = self.storage_dict[key]
# 		node.value = (key, value)
# 		self.storage.move_to_end(node)
# 		return

# 	if self.size == self.limit
# 		del self.storage_dict[self.storage.head.value[1]]  # this is wild.
# 		self.storage.remove_from_head()  
# 		self.size += 1

# 	self.storage.add_to_tail((key, value))    # opening it as a tuple
# 	self.storage_dict[key] = self.storage.tail
# 	self.size += 1
