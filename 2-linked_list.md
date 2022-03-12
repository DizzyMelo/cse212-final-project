# Linked List

**Introduction**
A linked list is a data structure where each element in the list keeps pointers indicating who is the next and prevvious elements. Each element is usually encapsulated is a Node object. Usually there is a class that keeps track of the first (head) and last (tail) element of the list. 


**Example**

```python
# Example of a Node class
class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

# Example of a Linked List class
class LinkedList:
    head = None
    tail = None

    def insert(self, val):
        pass
    
    def remove(self, val):
        pass

    def getElementAt(self, index):
        pass


```
**Problem to Solve**