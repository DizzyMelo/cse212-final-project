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
        visited = set()
        curr = self.head

        while curr:
            if curr.val in visited:
                return True
            visited.add(curr.val)
            curr = curr.next
        
        return False

llist = LinkedList()

llist.insert_head(5)
llist.insert_head(6)
llist.insert_head(2)
llist.insert_head(9)
llist.insert_head(4)

print(llist.hasCycle())

llist.head.next.next.next = llist.head.next.next

print(llist.hasCycle())