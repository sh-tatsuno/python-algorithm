# without cashing

def staircase(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return staircase(n-1) + staircase(n-2) + staircase(n-3)

# using cashing

def staircase(n):
    
    def save_calculations(n):
        if n == 1:
            return [1]
        if n == 2:
            return [1,2]
        if n == 3:
            return [1,2,4]
        ret = save_calculations(n-1)
        ret.append(sum(save_calculations(n-1)[-3:]))
        return ret
    
    return save_calculations(n)[-1]

test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [3, 4]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)