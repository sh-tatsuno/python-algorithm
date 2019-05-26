def recursive_binary_search(arr, target, left=0, min_index=-1):  
        if len(arr) == 0:
            return min_index
        center = (len(arr) - 1) // 2
 
        if arr[center] > target:
            return recursive_binary_search(arr[:center], target, left, min_index)
        else:
            min_index = center + left
            return recursive_binary_search(arr[center+1:], target, left+center+1, min_index)

def recursive_get_target(arr, target, left=0):  
        if len(arr) == 0:
            return None
        center = (len(arr) - 1) // 2
     
        if arr[center] == target:
            return arr[center]
        elif arr[center] > target:
            return recursive_get_target(arr[:center], target, left)
        else:
            return recursive_get_target(arr[center+1:], target, left+center+1)
    

def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    Return the two numbers in the form of a sorted list
    """
    if len(arr) < 2:
        return [None, None]
    
    arr = sorted(arr)
    ind = recursive_binary_search(arr, target)
    if ind == -1:
        return [None, None]
    arr = arr[:ind+1]
    for i in range(len(arr)):
        ret = recursive_get_target(arr[i:], target-arr[i])
        if ret != None:
            return [arr[i], ret]
    return [None, None]


def pair_sum(arr, target):
    # sort the list
    arr.sort()
    
    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(arr) - 1

    # shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:       # sum < target ==> shift front pointer forward
            front_index += 1 
        else:
            back_index -= 1               # sum > target ==> shift back pointer backward

    return [None, None]

def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")

input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)