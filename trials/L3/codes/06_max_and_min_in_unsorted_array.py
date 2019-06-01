def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    for i in range(len(ints)):
        if i == 0:
            min_int = ints[0]
            max_int = ints[0]
        if min_int > ints[i] : min_int = ints[i]
        if max_int < ints[i] : max_int = ints[i]
    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")