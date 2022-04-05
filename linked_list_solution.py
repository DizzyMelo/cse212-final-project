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
        visited = set() # Initialize an empty set
        curr = self.head # Set the current node as the head

        while curr: # iteration condition
            if curr.val in visited: # Check if the current not val is in the set
                return True # If the condition is satisfied, there is a cycle. Return True
            visited.add(curr.val) # If not, add the current node val to the set
            curr = curr.next # Move the current node to the next element
        
        return False # If no cycle was found, return False

llist = LinkedList()

llist.insert_head(5)
llist.insert_head(6)
llist.insert_head(2)
llist.insert_head(9)
llist.insert_head(4)

print(llist.hasCycle())

llist.head.next.next.next = llist.head.next.next

print(llist.hasCycle())