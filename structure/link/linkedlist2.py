class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        current_node = Node(value)
        current_node.next = self.head
        self.head = current_node
    
    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        current_node = self.head
        while(current_node.next!=None):
            current_node = current_node.next
        current_node.next = Node(value)
    
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next                
            return

        current_node = self.head
        while(current_node!=None):
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
                
    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            raise ValueError("Value not found in the list.")

        current_node = self.head
        value = current_node.value
        self.head = current_node.next
        return value
        
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        if pos==0:
            self.prepend(value)
            return

        current_node = self.head
        for _ in range(pos-1):
            current_node = current_node.next
            if current_node.next == None:
                current_node.next = Node(value)
                return
        tmp_node = current_node.next
        current_node.next = Node(value)
        current_node.next.next = tmp_node
        
        pass
    
    def size(self):
        """ Return the size or length of the linked list. """
        size=0
        current_node = self.head
        while(current_node != None):
            size += 1
            current_node = current_node.next
        
        return size
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

print(linked_list.to_list())
# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"