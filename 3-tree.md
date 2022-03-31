# Tree

**Introduction**

Trees is a widely used abstract data structure. Similar to a linked list, trees contain nodes, however, each node can contain pointers to one or many other elements. A natural way to use trees is then data has a hierarchical structure. Trees make searches extremely efficient when properly organized.


 - **Purpose**

The purpose of trees is to efficiently organize data in order to optimize operations, such as insertion, deletion, and searches. 

 - **Performance**
 
 
 - **Problems that can be Solved Using this Data Structure**

 Compression algorithms commonly uses a the concept of trees to compress information. Another great application for trees is to organize directories and subdirectories. Binary Search Trees are great for searches, making it possible to find elements in the tree in O(log n) time complexity.

 - **Common Errors**

 Many algorithms performed in a tree use the concept of recursion, what may be difficult to fully understand even though they may seem pretty simple. Traversing a tree, or visiting the nodes, may also be difficult because there are different ways to do it. There are two types of traversal, depth first search and breadth first search. Knowing when to use each is important to solve problems.


**Example**

```python

# Example of a node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        self._insert(self.root, val)
    
    def _insert(self, root: Node, val):
        if self.root is None:
            self.root = Node(val)
        else:
            # Check the left side
            if root.val > val:
                if root.left is None:
                    root.left = Node(val)
                else:
                    self._insert(root.left, val)
            #Check the right side
            else:
                if root.right is None:
                    root.right = Node(val)
                else:
                    self._insert(root.right, val)
    
    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, root: Node):
        if root is None:
            return
        
        self._traverse(root.left)
        print(root.val)
        self._traverse(root.right)

    def findValue(self, val):
        '''
            Implement the findValue function to return true if
            the value is inside the BST and false if not.
            Implemnt it in O(long n) time complexity.
        '''
        pass
        
```

**Problem to Solve**

Implement the findValue function to return true if the value is inside the BST and false if not. Implemnt the solution in O(long n) time complexity.

[Solution](binary_search_tree.py)