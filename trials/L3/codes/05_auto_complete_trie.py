class TrieNode:
    def __init__(self):
        self.is_char = False
        self.children = {}
    
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        ret = []
        if suffix != '':
            child_node = self.children[suffix]
            if child_node.is_char:
                ret += [suffix]
            for key in child_node.children.keys():
                ret += [suffix + word for word in child_node.suffixes(key)]
        else:
            for key in self.children.keys():    
                ret += self.suffixes(key)

        return ret

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_char = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# # in Jupyter notebook
# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='')

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")

print('f:')
f('f')
print('---------')

print('trig:')
f('trig')
print('---------')

print('an:')
f('an')

## result
# f:
# un
# unction
# actory
# ---------
# trig:
# ger
# onometry
# ---------
# an:
# t
# thology
# tagonist
# tonym