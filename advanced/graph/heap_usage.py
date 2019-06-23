import heapq

# initialize an empty list 
heap = list()

# insert 5 into heap
heapq.heappush(heap, 6)

# insert 6 into heap
heapq.heappush(heap, 6)

# insert 2 into heap
heapq.heappush(heap, 2)

# insert 1 into heap
heapq.heappush(heap, 1)

# insert 9 into heap
heapq.heappush(heap, 9)

print("After pushing, heap looks like: {}".format(heap))

# pop and return smallest element from the heap
smallest = heapq.heappop(heap)   

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))

heap = list()

heapq.heappush(heap, (0, 1))

heapq.heappush(heap, (-1, 5))

heapq.heappush(heap, (2, 0))

heapq.heappush(heap, (5, -1))

print("After pushing, now heap looks like: {}".format(heap))

# pop and return smallest element from the heap
smallest = heapq.heappop(heap)   

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))