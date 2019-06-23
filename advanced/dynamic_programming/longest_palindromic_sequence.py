
def lps(input_string): 
    # store previous data
    matrix = [[0 for x in range(len(input_string))] for x in range(len(input_string))]
    max_p = 0
    for r in range(len(input_string)):
        for c in range(r):
            if r > 0:
                matrix[r][c] = matrix[r-1][c]
                # subproblem
                if (c - (matrix[r][c] + 1) >= 0) and (matrix[r][c] + 1 < r):
                    if input_string[c - (matrix[r][c] + 1)] == input_string[c + (matrix[r][c] + 1)]:
                        matrix[r][c] += 1 
            max_p = max_p if matrix[r][c] < max_p else matrix[r][c] 
    return max_p * 2 + 1

import pprint
pp = pprint.PrettyPrinter()

# complete LPS solution
def lps(input_string): 
    n = len(input_string) 

    # create a lookup table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 

    # strings of length 1 have LPS length = 1
    for i in range(n): 
        L[i][i] = 1 
    
    # consider all substrings
    for s_size in range(2, n+1): 
        for start_idx in range(n-s_size+1): 
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]: 
                # general match case
                L[start_idx][end_idx] = L[start_idx+1][end_idx-1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx-1], L[start_idx+1][end_idx]); 

    # debug line
    # pp.pprint(L)
    
    return L[0][n-1] # value in top right corner of matrix

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)

string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

