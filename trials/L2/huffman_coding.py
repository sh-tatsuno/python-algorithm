import sys
import math

class Node(object):
        
    def __init__(self, index = None, value = None):
        self.index = index
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value

    def get_index(self):
        return self.index
        
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
        return f"Node({self.get_index()}, {self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_index()}, {self.get_value()})"
    
    
class HuffmanTree():
    def __init__(self, node=None):
        self.root = node

    def get_root_value(self):
        return self.root.value
        
    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node

    def get_binary(self):
        def binary(dic, node):    
            if node == None:
                return
            if node.has_left_child():
                left = node.get_left_child()
                left.value = "0" + node.value
                binary(dic, left)
            if node.has_right_child():
                right = node.get_right_child()
                right.value = "1" + node.value
                binary(dic, right)
            if node.index != None:
                dic[node.index] = int(node.value)
            return

        dic = {}
        self.root.value = ""
        binary(dic, self.get_root())
        max_len = max(dic.values())
        for k, v in dic.items():
            dic[k] = str(v).zfill(int(math.log(max_len)))

        return dic

    def merge(self, new_tree):
        if self.root == None:
            self.set_root(new_tree.get_root())
            return
            
        new_root = new_tree.get_root()
        current_root = self.get_root() 

        node = Node(value = current_root.get_value() + new_root.get_value())
        self.set_root(node)

        if current_root.get_value() < new_root.get_value():
            self.root.set_left_child(current_root)
            self.root.set_right_child(new_root)
        else:
            self.root.set_right_child(current_root)
            self.root.set_left_child(new_root)
        return 

class HeapTree():
    def __init__(self, huff_tree=None):
        self.root = self.get_new_node(huff_tree)

    def get_root(self):
        return self.root

    def set_root(self, huff_tree):
        self.root = self.get_new_node(huff_tree)

    def get_new_node(self, huff_tree):
        if huff_tree ==None:
            return None
        return Node(index = huff_tree, value = huff_tree.get_root_value())

    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert(self, new_tree):
        if self.root == None:
            self.set_root(new_tree)
            return
        new_node = self.get_new_node(new_tree)
        current_node = self.get_root() 
        while(True):
            branch = self.compare(current_node, new_node)
            
            if branch <= 0:
                if current_node.has_left_child() != True:
                    current_node.set_left_child(new_node)
                    return
                current_node = current_node.get_left_child()
                
            else:
                if current_node.has_right_child() != True:
                    current_node.set_right_child(new_node)
                    return
                current_node = current_node.get_right_child()
        return

    def pop(self):
        if self.root == None:
            return None
        prev_node = None
        current_node = self.get_root()
        while(True):
            if current_node.has_left_child():
                prev_node = current_node
                current_node = current_node.get_left_child()
            else:
                if prev_node == None:
                    if current_node.has_right_child():
                        self.root = current_node.get_right_child()
                    else:
                        self.root = None
                else:
                    if current_node.has_right_child():
                        prev_node.set_left_child(current_node.get_right_child())
                    else:
                        prev_node.set_left_child(None)
                return current_node


class PriorityQueue(object):
    def __init__(self):
        self.queue_tree = HeapTree()
    def push(self, huff_tree):
        self.queue_tree.insert(huff_tree)
        return
    def pop(self):
        return self.queue_tree.pop()


def huffman_encoding(data):
    # aggregate chars
    # Take a string and determine the relevant frequencies of the characters.
    char_dict = {}
    if len(data) < 1:
        return data, char_dict

    for char in data:
        char_dict[char] = 1 if char not in char_dict else char_dict[char] + 1

    queue = PriorityQueue()
    size = len(char_dict)
    for c in char_dict:
        node = Node(index=c, value=char_dict[c])
        tree = HuffmanTree(node)
        queue.push(tree)

    for _ in range(size-1):
        min_1 = queue.pop()
        min_2 = queue.pop()

        new_tree = min_1.index
        
        new_tree.merge(min_2.index)
        queue.push(new_tree)
        
    huff_tree = queue.pop().index

    dic = huff_tree.get_binary()
    ret = ""
    for char in data:
        ret += dic[char]
    return ret, dic



def huffman_decoding(data, dic):
    ret = ""
    dic_swap = {}
    if len(dic) > 0:
        for k, v in dic.items():
            dic_swap[v] = k
        length = len(v)
        N = len(data) // length
        for i in range(N):
            ret += dic_swap[data[length*i:length*(i+1)]]
    return ret


def run_test(case, text):
    print(case, "\n")

    # encode
    encoded_data, dic = huffman_encoding(text)
    v1 = sys.getsizeof(text)
    if len(encoded_data) > 0:
        v2 = sys.getsizeof(int(encoded_data,base=2))
    else:
        v2 = sys.getsizeof(encoded_data)
    assert v1 >= v2, "memory should reduced. before: {0}, after: {1}".format(v1, v2)
    print("memory reduced. before: {0}, after: {1}".format(v1, v2))
    
    # decode
    decoded_data = huffman_decoding(encoded_data, dic)
    assert text == decoded_data, "text should be equal. actual: {0}, expected: {1}".format(decoded_data, text)
    print("out put is equal to input, passes the test.\n\n")

if __name__ == "__main__":

    text1 = "The bird is the word"
    run_test("normal case", text1)

    text2 = ""
    run_test("empty case", text2)

    text3 = "'こんにちは！' means 'hello!'"
    run_test("include multi bytes", text3)