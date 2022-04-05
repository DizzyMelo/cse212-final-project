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
                if root.left is None: # If the root.left is none, add the node to the left node
                    root.left = Node(val)
                else:
                    self._insert(root.left, val) # Make recursive call on the left side
            #Check the right side
            else:
                if root.right is None:
                    root.right = Node(val)# If the root.right is none, add the node to the roght node
                else:
                    self._insert(root.right, val) # Make recursive call on the roght side
    
    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, root: Node):
        if root is None:
            return
        
        self._traverse(root.left) # Make recursive call on the left side
        print(root.val) # Print the current node val
        self._traverse(root.right) # Make recursive call on the right side

    def findValue(self, val):
        '''
            Implement the findValue function to return true if
            the value is inside the BST and false if not.
            Try to implemnt it in O(long n) time
        '''

        def helper(root: Node):
            if root is None: return False

            if root.val == val:
                return True
            if root.val > val:
                return helper(root.left)
            else:
                return helper(root.right)

        return helper(self.root)
        
bst = BST()

bst.insert(8)
bst.insert(3)
bst.insert(5)
bst.insert(10)
bst.insert(9)
bst.traverse()
print(bst.findValue(9))
print(bst.findValue(90))
print(bst.findValue(5))

