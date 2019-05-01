def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]
    
    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))

import matplotlib.pyplot as plt
import statistics
import time

n_steps = 10
step_size = 200
array_sizes = list(range(step_size, n_steps*step_size, step_size))
big_array = list(range(n_steps*step_size))
sum_array_times = []
sum_array_index_times = []

for array_size in array_sizes:
    subset_array = big_array[:array_size]
    
    start_time = time.time()
    sum_array(subset_array)
    sum_array_times.append(time.time() - start_time)
    
    start_time = time.time()
    sum_array_index(subset_array, 0)
    sum_array_index_times.append(time.time() - start_time)
    
    
plt.scatter(x=array_sizes, y=sum_array_times, label='sum_array')
plt.scatter(x=array_sizes, y=sum_array_index_times, label='sum_array_index')
plt.ylim(
    top=max(sum_array_times + sum_array_index_times),
    bottom=min(sum_array_times + sum_array_index_times))
plt.legend()
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()


# If your recursive code is not easy to read, you had better to check straight forward code.
def sum_array_iter(array):
    result = 0
    
    for x in array:
        result += x
    
    return result

arr = [1, 2, 3, 4]
print(sum_array_iter(arr))