def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
        
    def recursive_binary_search_min(target, source, left=0, min_index=-1):  
        if len(source) == 0:
            return min_index
        center = (len(source)-1) // 2
        if source[center] == target:
            min_index = center + left          
            return recursive_binary_search_min(target, source[:center], left, min_index)
        elif source[center] < target:
            return recursive_binary_search_min(target, source[center+1:], left+center+1, min_index)
        else:
            return recursive_binary_search_min(target, source[:center], left, min_index)
        
    def recursive_binary_search_max(target, source, left=0, max_index=-1):  
        if len(source) == 0:
            return max_index
        center = (len(source)-1) // 2
        if source[center] == target:
            max_index = center + left          
            return recursive_binary_search_max(target, source[center+1:], left+center+1, max_index)
        elif source[center] < target:
            return recursive_binary_search_max(target, source[center+1:], left+center+1, max_index)
        else:
            return recursive_binary_search_max(target, source[:center], left, max_index)

    return [recursive_binary_search_min(number, arr), recursive_binary_search_max(number, arr)]
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)