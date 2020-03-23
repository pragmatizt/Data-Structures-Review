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
        pass

    def insert_before(self, data, x):
        pass

    def insert_at_position(self, data, k):
        pass

    def delete_node(self, x):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

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

