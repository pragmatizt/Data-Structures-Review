# Ira's note: Why do we include the same thing twice (from yesterday's dir)?
# is it just because the .py file needs to be in its respective folder it's being imported in?

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:                   
            new_node.prev = self.tail   # Would love to understand what's happening here.
            self.tail.next = new_node   # go over during AH
            self.tail = new_node        # go over during AH

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):      # Ask to go over during AH
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        # TODO: Catch errors if list is empty or node is not in list
        # For now assumine node is in list
        self.length -= 1
        # if head and tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # if head
        elif node is self.head:
            self.head = self.head.next
            node.delete()

        # if tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            # if regular node
            node.delete()

    def get_max(self):
        # Loop through all nodes, looking for biggest value
        # TODO: Error checking
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while curent:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value