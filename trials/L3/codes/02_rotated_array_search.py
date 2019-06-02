def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def search_number(input_list, number, upper, lower):

        # check init
        if input_list[lower] == number:
            return lower
        if input_list[upper] == number:
            return upper

        # set current value
        current = (upper + lower) // 2
        if input_list[current] == number:
            return current

        # check if rotation between lower and current
        # normal order
        if input_list[lower] < input_list[upper]:
            if input_list[current] > number:
                upper = current
            else:
                lower = current
        else:
            # in reverse in upper area
            if input_list[current] > input_list[lower]:
                if (input_list[current] > number) and (number > input_list[lower]):
                    upper = current
                else:
                    lower = current
            # in reverse in lower area
            else:
                if (input_list[current] < number) and (number < input_list[upper]):
                    lower = current
                else:
                    upper = current

        if upper - lower <= 1:
            return -1

        return search_number(input_list, number, upper, lower)

    return search_number(input_list, number, len(input_list) - 1, 0)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass

test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass

test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass

test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass