class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, key, value):
        if self.head == None:
            self.head = DoubleNode(key, value)
            self.tail = self.head
        else:
            self.tail.next = DoubleNode(key, value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.link = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        self.move_to_recent(key)
        return self.cache[key].value

    def size(self):
        return len(self.cache)

    def move_to_recent(self, key):
        if key not in self.cache:
            return

        # nodes
        current_node = self.cache[key]
        previous_node = current_node.previous
        next_node = current_node.next

        # remove current node in link
        if previous_node != None:
            previous_node.next = next_node 

        if next_node != None:
            next_node.previous = previous_node

        # add current node in tail of link
        self.link.append(current_node.key, current_node.value)
        self.cache[key] = self.link.tail

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.cache:
            # add new value
            self.link.append(key, value)
            self.cache[key] = self.link.tail

            # over capacity
            if self.size() > self.capacity:
                # remove oldest value
                head_node = self.link.head
                if head_node.next != None:
                    self.link.head = head_node.next
                del self.cache[head_node.key]

        # If the key exists, do nothing.
        return 

def assertion(case, v1, v2):
    assert v1 == v2, "actual: {0}, expected: {1}".format(v1, v2)
    if v1 == v2:
        print("test case: {0}\n actual: {1}, expected: {2}. passed the test\n\n".format(case, v1, v2))

our_cache = LRU_Cache(2)

our_cache.set(1, 11)
our_cache.set(2, 22)

assertion("get 1 is 11", our_cache.get(1), 11)
assertion("get 2 is 22", our_cache.get(2), 22)
assertion("no key pattern", our_cache.get(3), -1) # no key

our_cache.set(3, 33) # over capacity, remove 1
assertion("over capacity", our_cache.get(1), -1) # over capacity
assertion("set new value", our_cache.get(3), 33) # set new value
