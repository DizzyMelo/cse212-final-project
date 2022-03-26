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
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def remove_head(self):
        
        if self.head is None:
            print('There is no element in the list.')
            return
        
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head.prev = None
            self.head = self.head.next

    def getElementAt(self, index):
        curr = self.head
        curr_index = 0

        while curr and curr_index <= index:
            if curr_index == index:
                return curr
            curr = curr.next
            curr_index += 1
        
        return None
    
    def __iter__(self):
        curr = self.head

        while curr:
            yield curr.val
            curr = curr.next
    
    def __repr__(self) -> str:
        visited = []
        curr: Node = self.head

        while curr:
            visited.append(curr.val)
            curr = curr.next

        return str(visited)

    def __len__(self) -> int:
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next
        return count

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

[Solution](linked_list.py)