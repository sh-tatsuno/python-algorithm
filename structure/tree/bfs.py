# implementation of breadth first search tree

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")
print(q)

# BFS algorithm
def bfs(tree):
    visit_order = list()
    q = Queue()

    # start at the root node and add it to the queue
    node = tree.get_root()
    q.enq(node)
    
    while len(q) != 0:
        node = q.deq()
        visit_order.append(node)
        
        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())
            
    return visit_order

# check solution: should be: apple, banana, cherry, dates
bfs(tree)

def _bfs(tree):
    visit_order = list()
    q = Queue()
    
    # start at the root node and add it to the queue
    node = tree.get_root()
    visit_order.append(node)
    q.enq(node)
    
    while len(q) != 0:
        node = q.deq()
        if node.has_left_child():
            visit_order.append(node.get_left_child())
            q.enq(node.get_left_child())
        else:
            visit_order.append(Node("<empty>"))
        if node.has_right_child():
            visit_order.append(node.get_right_child())
            q.enq(node.get_right_child())
        else:
            visit_order.append(Node("<empty>"))
            
    return visit_order

# implement print function

class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    """
    define the print function
    """
    def __repr__(self):
        tree = Tree()
        tree.root = self.get_root()
        tree_list = _bfs(tree)
        n = 0
        s = ""
        length = len(tree_list)
        while (2**(n-1) < length):
            output = [str(item.value) for item in tree_list[:2**n]]
            s += "|".join(output) + "\n"
            tree_list = tree_list[2**n:]
            n += 1
        return s

# check solution
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
print(tree)

# result should be below
# apple
# banana|cherry
# dates|<empty>|<empty>|<empty>
# <empty>|<empty>