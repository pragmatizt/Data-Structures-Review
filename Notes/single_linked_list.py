class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

"""You can see that the list class itself does not contain
any node objects, it contains only reference to the first node
of the list."""
class SingleLinkedList:
    def __init__(self):  # Init method
        self.start = None

    def display_list(self): # Displays elements of list
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is :  ")
            p = self.start
            while p is not None:
                print(p.info , " ", end='')
                p = p.link
            print()

    def count_nodes(self):  # count # of nodes in list
        p = self.start 
        n = 0
        while p is not None:
            n+=1
            p = p.link
        print("Number of nodes in the list = " ,n)

    def search(self,x):   # search for value in list
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x , " is at position ", position)
                return True
            position+=1
            p = p.link
        else:
            print(x, " not found in list")
            return False

    def insert_in_beginning(self, data):  # insert new node in beginning of list
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.linke
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        # If list is empty
        if self.start is None:
            print("List is empty")
            return

        # x is in first node, new node is to be inserted before first node
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        # Find reference to predecessor of node containing x
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
                p = p.link

        if p.link is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        
        p = self.start
        i = 1
        while i<k-1 and p is not None: # find a reference to k-1 node
            p = p.link
            i+=1

        if p is None:
            print("You can insert only upto position", i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        
        if self.start is None:
            print("List is empty")
            return
        
        # Deletion of first node
        if self.start.info == x:
            self.start = self.start.link
            return

        # Deletion in between or at the end
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print("Element ", x ,"not in list")
        else:
            p.link = p.link.link

    def delete_first_node(self):
        
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        
        if self.start is None:
            return

        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self,listStart):
        pass

    def _divide_list(self, p):      # end of single linkedlist class
        pass

##################################################

list = SingleLinkedList()  # Let's create a SingleLinkedList instance object
list.create_list()

while True:
    print("1. Display list")
    print("2. Count the numbber of nodes")
    print("3. Search for an element")
    print("4. Insert in empty list")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

