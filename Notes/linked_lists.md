## Notes from:
- BaseCS: LinkedLists (by "The Practical Dev"), https://www.youtube.com/watch?v=FuRMa8mHvLY

# Linked Lists
A data structure that is traversed linearly.
Linked lists can only be traversed sequentially.

Nonlinear examples: Tree, or a graph.  Nonlinear.  Order doesn't matter.
Arrays: Order matters.  They have indices.  An array is a linear data structure.

*Can be helpful to think of arrays when learning about linked lists.*

Biggest differentiator is how they use memory.  And how they allocate memory.
Dynamically typed languages like Ruby, or Javascript, or Python, you don't have to 
worry about how much memory your array is taking up.

But just because you're not worried about it, doesn't mean it's not happening.  Just abstracted away.

Linked Lists: Huge factor in what separates them from arrays.

What allows Linked lists to grow dynamically in size?

## Linked Lists Composed of:
**HEAD => NODE => LAST NODE => NULL**

A single node in a linked list has no idea how big or how small an entire linked list is.

As long as one node knows where the next piece of memory lies, we can traverse
through a linked list by going from one point of a linked list to the next.

===
Different types of linked lists:
**Singly-Linked List** - The nodes are traversing only in one way.

**Doubly-Linked List** - The nodes are two directional.  Can traverse down to the node 
that references null, but then can also go back up to the head node where we started from.

**Circular Linked List** - No null value.  We have a node that acts as a tail.  

Linked Lists at their core aren't complicated.  
What's complicated is knowing whether and when to use them.

We need to think about time and space complexity, which is often referred to as BIG O notation.

*"How much time does it take for me to do an action?"*
*"How much space am I using when I do that action?"*

If you can remember those two things, you can figure out the **BIG O** notation of what it is 
you're trying to do.

=======
## LINEAR TIME & CONSTANT TIME

**Linear Time / O(n):** As the input for function grows, the amount of space and time needed grows linearly.
By contrast, 

**Constant Time:** No matter how input grows in size, we need the same amount of time and space to do this action.

The actions we're concerned with are manipulating and handling parts of a linked list.  Which usually have to
do with constant time or linear time.

### INSERTING A NODE TO A LINKED LIST:
**Inserting node** at **beginning** of linked list: Time complexity of O(1) - constant time
**Inserting node** at **end** of linked list: Time complexity O(n) - linear time

### DELETING A NODE TO A LINKED LIST:
Same concept as insertion.  Deleting at beginning won't be a problem.
But for last?  If linked list has 3 million nodes, we would have to traverse 3m nodes.
So deleting at end would be inefficient.


=========================================
## ARRAYS 				            ||		LINKED LISTS
-----------------------------------:||:-------------------------------------:
[N] fast insertion and deletion     || [Y] fast insertion and deletion  <br>
[Y] fast search			            || [N] fast search                  <br>
[N] easy to grow or shrink	        || [Y] easy to grow or shrink       <br>
[Y] allocates a contiguous chunk    || [N] allocates a contiguous chunk	<br>
of memory			                || of memory                        <br>
[Y] Random access is allowed	    || [N] Random access is allowed     <br>
[Y] Easy binary search		        || [N] Easy binary search           <br>

*When are arrays helpful?*	             *When are linked lists helpful?*   <br>

|## ARRAYS    	                    | LINKED LISTS  	                |
|---	                            |---	                            |
|[N] fast insertion and deletion   	|[Y] fast insertion and deletion   	|
|[Y] fast search	   	            |[N] fast search    	            |
|[N] easy to grow or shrink   	    |[Y] easy to grow or shrink    	    |
|[Y] allocates a contiguous chunk   |[N] allocates a contiguous chunk   |
|of memory   	                    |of memory   	                    |
|[Y] Random access is allowed   	|[N] Random access is allowed   	|
|[Y] Easy binary search	   	        |[N] Easy binary search   	        |

If you ever find yourself having to do a lot of iteration or searching through dataset.
Or need to quickly find a random value. A linked list could be your worst enemy.

In those situations, an array has indexes, is a contiguous block of memory, 
and is handy for running algorithms like binary search.

If you need to add a whole lot of elements to a data set, and know you won't need 
to retrieve them later, in that case, a linked list makes sense.

