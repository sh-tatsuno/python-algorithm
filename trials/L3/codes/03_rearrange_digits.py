def sort_block(arr_left, arr_right):
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
            right_index += 1
            if right_index >= len(arr_right):
                ret += arr_left[left_index:]
                break
    return ret
    

def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    center = len(arr) // 2
    arr_left = merge_sort(arr[:center])    
    arr_right = merge_sort(arr[center:])
    
    return sort_block(arr_left, arr_right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    merged = merge_sort(input_list)
    ret_1 = ""
    ret_2 = ""
    for i in range(len(merged)):
        if i % 2 == 0:
            ret_1 = ret_1 + str(merged[len(merged)-i-1])
        else:
            ret_2 = ret_2 + str(merged[len(merged)-i-1])
    ret_1 = 0 if len(ret_1)==0 else int(ret_1)
    ret_2 = 0 if len(ret_2)==0 else int(ret_2)
    return [ret_1, ret_2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0,1], [1, 0]])
test_function([[0,1,2], [21, 0]])