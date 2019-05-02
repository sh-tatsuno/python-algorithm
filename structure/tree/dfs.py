# implementation of depth first search tree

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

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

# check Stack
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop())
print("\n")
print(stack)

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s

def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count +=1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
            
    if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order

# check pre-order traversal
pre_order_with_stack(tree, debug_mode=True)

def pre_order_tra(tree):

    visit_order=[]
    root = tree.get_root()

    def traverse(node):
        if node :
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())

    traverse(root)

# implement pre-oder with recursion
# get value -> left -> right
def pre_order(tree):
    current_node = tree.get_root()
    if current_node == None:
        return []
    ret = []
    ret.append(current_node.value)
    
    left_tree = Tree()
    left_tree.root = current_node.get_left_child()
    right_tree = Tree()
    right_tree.root = current_node.get_right_child()
    
    return ret + pre_order(left_tree) + pre_order(right_tree) 

pre_order(tree)

# define in_order traversal
# get left -> value -> right
def in_order(tree):
    current_node = tree.get_root()
    if current_node == None:
        return []
    ret = []
    ret.append(current_node.value)
    
    left_tree = Tree()
    left_tree.root = current_node.get_left_child()
    right_tree = Tree()
    right_tree.root = current_node.get_right_child()
    
    return in_order(left_tree) + ret +  in_order(right_tree) 

# check solution: should get: ['dates', 'banana', 'apple', 'cherry']
in_order(tree)

# define post_order traversal
# get left -> right -> value
def post_order(tree):
    current_node = tree.get_root()
    if current_node == None:
        return []
    ret = []
    ret.append(current_node.value)
    
    left_tree = Tree()
    left_tree.root = current_node.get_left_child()
    right_tree = Tree()
    right_tree.root = current_node.get_right_child()
    
    return post_order(left_tree)+  post_order(right_tree)  + ret 

# check solution: should get: ['dates', 'banana', 'cherry', 'apple']
post_order(tree)