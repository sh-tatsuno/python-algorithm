# use merge osrt
def sort_block(arr_left, arr_right):
    ret = []
    left_index=0
    right_index=0
    while(True):
        if ord(arr_left[left_index]) < ord(arr_right[right_index]):
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

def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    
    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    sorted_string = merge_sort(string)
    lower = None
    for ind in range(len(sorted_string)):
        if sorted_string[ind].islower():
            lower = ind
            break
    ret = ""
    upper = 0
    for char in string:
        if char.islower():
            ret += sorted_string[lower]
            lower += 1
        else:
            ret += sorted_string[upper]
            upper += 1
    
    return ret


# use built-in sort
def case_sort(string):
    upper_ch_index = 0
    lower_ch_index = 0
    
    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:       # ASCII value of a = 97 & ASCII value of z = 122
            lower_ch_index = index
            break
            
    output = list()
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)

def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]
    
    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")

test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)