def lcs(string_a, string_b):
    cols = string_a
    rows = string_b
    
    matrix = [[0 for x in range(len(cols) + 1)] for x in range(len(rows) + 1)]

    for r in range(1, len(rows)+1):
        for c in range(1, len(cols)+1):
            if cols[c-1] == rows[r-1]:
                matrix[r][c] = matrix[r-1][c] + 1
            else:
                matrix[r][c] = max(matrix[r-1][c], matrix[r][c-1])
    return matrix[len(rows)][len(cols)]

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')