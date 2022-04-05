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
            Try to implemnt it in O(long n) time
        '''

        def dfs(root: Node):
            if root is None: return False

            if root.val == val:
                return True
            if root.val > val:
                return dfs(root.left)
            else:
                return dfs(root.right)

        return dfs(self.root)
        
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

