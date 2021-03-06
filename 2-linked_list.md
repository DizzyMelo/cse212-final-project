# Linked List

**Introduction**

A linked list is a data structure where each element in the list keeps pointers indicating who is the next and prevvious elements. Each element is usually encapsulated is a Node object. Usually there is a class that keeps track of the first (head) and last (tail) element of the list. 

 - **Purpose**
 
 Linked Lists are very useful when resizing the list is a problem. Linked lists have no problem to increase or shrink its size. Operations such as insertion and deletion are very efficient, and can be acomplished in constant time.
 - **Performance**

 |Command    |Description   | Python Code| Performance|
 |-----------|--------------|------------|------------|
 |insert_head(data) |Adds a new element to the stack   | append()   | O(1)       |
 |remove_head()      |Removes one element from the stack an returns its value   | pop()      | O(1)       |
 |size()     |Returns the number of elements in the list   | len()      | O(N)       |
 |empty()    |Checks if the list has at least one element   | empty()      | O(1)       |
 |getAt(index)    |Retrieves an element at certain position   | get()      | O(N)       |


 - **Problems that can be Solved Using this Data Structure**

 Linked lists can be used to implement queues and stacks efficiently. When it comes to memory allocation, linked lists is also a great choice, as it allocates memory dynamically and doesn't need more memory allocation before adding a new element. Lists and arrays need to allocate memory when they are created, even though the whole space is not going to be used, and that can be a problem when dealing with huge amounts of data.
 
 - **Common Errors**

Some common errors while working with a linked list is the idea of pointers. Keeping track of where each pointer is pointing to is not an easy task and may take a while until it becomes natural. Removing an element which is located in the middle of the list is another moment when people make mistakes by not disconnecting and connecting the pointers proplerly.

**Example**

```python
# Example of a Node class
class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_head(self, val):
        new_node = Node(val) # Instantiate a Node object
        if self.head is None: # Check if the list is empty, by checking if the head is None. If the list is empty, the node is added to the head and the tail
            self.head = new_node 
            self.tail = new_node
        else: # If the list is not empty, the node is also added to the head and pointers are updated.
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def remove_head(self):
        
        if self.head is None: # Check if there is an element to be removed. If not, a message is displayed.
            print('There is no element in the list.')
            return
        
        elif self.head == self.tail: # Check if there is only one element. If true, pointers are updated.
            self.head = None
            self.tail = None

        else:
            self.head.prev = None # Update pointers to disconnect Node
            self.head = self.head.next

    def getElementAt(self, index):
        curr = self.head # Initialize the curr Node as the head
        curr_index = 0 # Initialize counter to 0

        while curr and curr_index <= index: # Iteration condition
            if curr_index == index: # If index is found, return the Node
                return curr
            curr = curr.next # Move the pointer to the next element
            curr_index += 1 # increment the counter
        
        return None
    
    # The function below overrides the __iter__ function to make simpler to itererate through the list
    def __iter__(self):
        curr = self.head

        while curr: # Iteration condition
            yield curr.val # Yiels the current node val
            curr = curr.next # Move the node to the next element
    
    # Overrides the function that retrieves an object representation
    def __repr__(self) -> str:
        visited = [] # Initialize an empty list
        curr: Node = self.head # Set the current node as the head

        while curr: # Iteration condition
            visited.append(curr.val) # Add the current node val to the visited list
            curr = curr.next # Move the current node to the next element

        return str(visited)

    # Override the __len__ function to check the length of the list
    def __len__(self) -> int:
        count = 0 # Initialize the count as 0
        curr = self.head # Initialize the current node as the head

        while curr: # Iteration condition
            count += 1 # Increment the counter
            curr = curr.next # Move the current node to the next element
        return count # Returns the count

    # Check if the list is empty or not
    def empty(self):
        return True if self.head is None else False

    def hasCycle(self):
        '''
        This function should check if the linked list has a cyle. 
        A linked list has a cycle if there is a node that its next pointer 
        points to a previous node.
        '''
        pass

```
**Problem to Solve**

Implement a function called hasCicle that checks if the linked list hast a cycle in it.
A linked list has a cycle if there is a node that its next pointer points to a previous node.

[Solution](linked_list_solution.py)