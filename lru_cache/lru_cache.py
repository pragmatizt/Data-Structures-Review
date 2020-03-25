# Imports

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # Link to the list (inspired by Assignment 1)
        self.order = DoublyLinkedList()
        # We have a limit above
        self.limit = limit
        # Counter
        self.size = 0
        # Create a dictionary 
        self.storage_dict = {}    # why self.storage_dict = {} vs. self.storage_dict = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Returns the value associated with the key or none
        if key in self.storage_dict:
            node = self.storage_dict[key] # If key is there, we want the given key to point to that node
            self.order.move_to_end(node)
            print(node)
            print(node.value)   # we never defined value, do we need to?
            print(node.value[1])
            print(node.value[0])
            return node.value[1]   # the [1] is the value; of the location of the pointer of the node
        else:
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
        if key in self.storage_dict:
            node = self.storage_dict[key]
            node.value = (key, value)
            return self.order.move_to_end(node)

        if len (self.order) == self.limit:
            del self.storage_dict[self.order.head.value[0]]
            self.order.remove_from_tail()

        self.order.add_to_tail((key, value))
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
