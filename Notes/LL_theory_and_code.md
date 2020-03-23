## Notes from:
Overview by By Deepali Srivastava - https://www.youtube.com/watch?v=AvGNrp4Al0A

*First X minutes do a great visual on how nodes interact within a Linked List.*

The first node contains the first list items.  And reference to the second node.  That node contains the second list item, and reference to the third node, and so on.

While maintaining a linked list, we maintain a reference to only the first node of the linked list.

We call that reference **"start"**.

**Linked Lists:**
- Dynamic data structure made up of nodes
- Data in a linked list is not stored in cotiguous memory locations
- Insertion and deletion of elements is easier
- Can be used to implement abstract data types like list, stack, queue
- **Disadvantage:** efficient random access is not possible.
- **Disadvantage:** Implementation requires extra memory

## Linked List types
- Single Linked Lists
- Double Linked Lists
- Circular Linked Lists
- Linked Lists with Header Node
- Sorted Linked Lists

### Single Linked List
(this starts 5:30 of video)

Node of a single linked list:  INFO | LINK

The start of a link list is referenced as **Start**. We have to use the link value from each node to the next node.

You would basically follow each link of the node.  

In Python, we have a spacial reference value called **None**.  None denotes no next node.  Which means end of the list.

*see single_linked_list.py for python code sample*

## Finding references in a Linked List
*(this portion of video starts at 19:30)*

- Finding reference to last node
- Finding reference to second last note
- Finding reference to a node with particular info
- Finding reference to predecessor of a node with a particular info
- Finding reference to a node at a particular position

**Finding reference to last node**
~~~~
p = self.start 
while p.link is not None:  
    p = p.link
~~~~

**Finding reference to second to last node**
~~~~
p = self.start
while p.link.link is not None:
    p = p.link
~~~~

**Finding reference to a node with paritcular info**
Say we want to find a node with a value of x.
~~~~
x = 30

p = self.start
while p.link is not None:
    if p.link.info == x:
        break
    p = p.link
~~~~

**Finding reference to a node at a particular position**
Say we want to find a node at the *nth* node of the list.

~~~~
k = 3  # being position

p = self.start
i = 1
while i<k and p is not None:
    p = p.link
    i+=1
~~~~

**Insertion in a Single Linked list**
- Insertion in the beginning
- Insertion in an empty list
- Insertion at the end
- Insertion in between the list nodes

`temp = Node(data)`

This is how you would add a new node:
Create a new node called `temp`. 
`temp.link = self.start`
`self.start = temp`

*The above code is the correct node, because if you did it in reverse then the node would just continuously link to itself*

**Insertion in an empty list**
`self.start = temp`

**Insertion at the end**
`p = self.start`
`while p.link is not None:`
    `p = p.link`
`p.link = temp`

**Insertion in between the nodes**
`temp.link = p.link`
`p.link = temp`

*remember, order matters*

**Insertion after a node**
`p = self.start`
`while p is not None:`
`  if p.info == x:`
`    break`
`  p = p.link`

Insert a new node by writing these two insertions:
`temp.link = p.link`
`p.link = temp`

**Insertion before a node**
`p = self.start`
`while p.link is not None:`
`  if p.link.info == x:` # what is info in this case?
`    break`
`  p = p.link`

*and then, just to keep drilling the idea in, this is how we would insert that new node:*
`temp.link = p.link`
`p.link = temp`

**Insertion at a given position**
Suppose:
k = insert a new node at kth position in the list
4 (representing the 4th index)

So it means we'll be inserting a node between index 3 and index 4.  For that, we'd need a reference to the 3rd node for starters.

We would need to reference a k - 1 of the list.

`p = self.start`
`i = 1`
`while i<k-1 and p is not None:`
  `p = p.link`
  `i+=1`

After finding that location, we create a temp node.
And again, doing this for repetitions:
`temp.link = p.link`
`p.link = temp`


## Deletion in a Single Linked List
- Deletion of first node
- Deletion of the only node
- Deletion in between the list
- Deletion at the end

**Deletion fo the first node**
After deletion, the second node will become the first node of the list.

`self.start = self.start.link`

**Deletion of the only node**
`self.start = None`

**Deletion in between the list nodes**
We'll need a reference for this one.

`p.link = p.link.link`  

**Deletion at the end of the list**
`p.link = None`
