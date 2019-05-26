def count_inversions(arr):
    inverse_block = []
    _, inverse_block = merge_sort(arr, inverse_block)
    return len(inverse_block)

def sort_block(arr_left, arr_right, inverse_block):
    ret = []
    left_index=0
    right_index=0
    while(True):
        if arr_left[left_index] < arr_right[right_index]:
            ret.append(arr_left[left_index])
            left_index += 1
            if left_index >= len(arr_left):
                ret += arr_right[right_index:]
                break
        else:
            ret.append(arr_right[right_index])
            inverse_block.append([arr_left[left_index] , arr_right[right_index]])
            right_index += 1
            if right_index >= len(arr_right):
                ret += arr_left[left_index:]
                break
    return ret, inverse_block
    

def merge_sort(arr, inverse_block):
    if(len(arr)<=1):
        return arr, inverse_block
    center = len(arr) // 2
    arr_left = arr[:center]
    arr_left, inverse_block = merge_sort(arr_left, inverse_block)
    
    arr_right = arr[center:]
    arr_right, inverse_block = merge_sort(arr_right, inverse_block)
    
    return sort_block(arr_left, arr_right, inverse_block)

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)