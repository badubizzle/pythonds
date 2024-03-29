# Python LinkedList



Linked list consist of nodes.
Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list
Each node has a pointer to the next node

Types of LinkedList

## Exercise
   1. Implement a class for a Node in a linked list
   2. Implement Singly Linked List class with the following method
      1. **add** - Add a new value to the end of the linked list
      2. **insert_at** - Takes a value and index and insert the value at the given index in the linked list. If index is greater than number of items in linked list, insert at the end of the linked list
      3. **index_of** - Takes a value and returns the zero-based index of the value if the value is in the linked list otherwise None
      4. **contains** - Using **index_of** method above, implement a method contains which takes in a value and return True if the value is in the linked list otherwise returns False
      5. **size** - Returns the total nodes in the linked list
      6. 


1. Write code to remove duplicates from an unsorted linked list
2. How would you solve question 1 above problem if a temporary buffer is not allowed?
3. Implement an algorithm to find the nth to last element of a singly linked list
4. Implement an algorithm to delete a node in the middle of a single linked list, given only access
to that node
EXAMPLE
Input: the node ‘c’ from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e

5. You have two numbers represented by a linked list, where each node contains a sin- gle digit The digits are stored in reverse order, such that the 1’s digit is at the head of the list Write a function that adds the two numbers and returns the sum as a linked list
EXAMPLE
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8