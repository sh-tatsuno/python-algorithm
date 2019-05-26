class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go    
    
    def size(self):
        return self.next_index
    
    def _doubly_cbt_capacity(self):
        new_cbt = [None for _ in range(self.size() *2)] 
        for i in range(len(self.cbt)):
            new_cbt[i] = self.cbt[i]
        self.cbt = new_cbt
    
    def _heapup(self, index):
        prev_index = (index - 1) // 2
        if prev_index < 0:
            return
        if self.cbt[prev_index] > self.cbt[index]:
            self.cbt[prev_index], self.cbt[index] = self.cbt[index], self.cbt[prev_index]
            self._heapup(prev_index)
        return
    
    def _heapdown(self, index):
        child_index = 2 * (index + 1)
        if child_index >= self.size():
            return
        
        if self.cbt[child_index] > self.cbt[child_index-1]:
            child_index -= 1
            
        if self.cbt[child_index] < self.cbt[index]:
            self.cbt[child_index], self.cbt[index] = self.cbt[index], self.cbt[child_index]
            self._heapdown(child_index)
        
        return
            
    def insert(self, data):
        # add last
        self.cbt[self.next_index] = data
        
        # exchange
        self._heapup(self.next_index)
        
        # step to next index
        self.next_index += 1
        
        if len(self.cbt) == self.next_index:
            self._doubly_cbt_capacity()
    
    def remove(self):
        if self.next_index == 0:
            return
        ret = self.cbt[0]
        self.cbt[0], self.cbt[self.size()-1] = self.cbt[self.size()-1], self.cbt[0]
        self.cbt[self.size()-1] = None
        self.next_index -= 1
        self._heapdown(0)
        return ret
    
    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]
        
    def is_empty(self):
        return self.size() == 0

def heapsort(arr):
    heap = Heap(len(arr))
    for i in arr:
        heap.insert(i)
    for i in range(len(arr)):
        val = heap.remove()
        arr[i] =val
    return 

def heapify(arr, n, i):
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subree
    
    # consider current index as largest
    largest_index = i 
    left_node = 2 * i + 1     
    right_node = 2 * i + 2     
  
    # compare with left child
    if left_node < n and arr[i] < arr[left_node]: 
        largest_index = left_node
  
    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]: 
        largest_index = right_node
  
    # if either of left / right child is the largest node
    if largest_index != i: 
        arr[i], arr[largest_index] = arr[largest_index], arr[i] 
    
        heapify(arr, n, largest_index) 
        
def heapsort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    """
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]

test_case = [arr, solution]

test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
