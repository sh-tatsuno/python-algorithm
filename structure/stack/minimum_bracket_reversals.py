def minimum_bracket_reversals_without_stack(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
        input_string(string): Strings to be used for bracket reversal calculation
    Returns:
        int: Number of breacket reversals needed
    """
    def to_int(blanket):
        if blanket == "{":
            return 1
        if blanket == "}":
            return -1
        return None
    
    length = len(input_string)
    if length % 2 != 0: 
        return -1
    
    ret = 0
    stack = 0
    for i in range(length):
        stack += to_int(input_string[i])
        if stack < 0:
            ret += 1
            stack += 2
        if stack > length - i:
            ret += 1
            stack -= 2
    return ret

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            top = stack.top()

            # if top is { and next is } then remove
            if top != bracket: 
                if top == '{':
                    stack.pop()
                    continue
            stack.push(bracket)

    # the rest are only unmatch blankets
    ls = list()
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        ls.append(first)
        ls.append(second)
        if first == '}' and second == '}':
            count += 1
        elif first == '{' and second == '}':
            count += 2
        elif first == '{' and second == '{':
            count += 1
    return count
