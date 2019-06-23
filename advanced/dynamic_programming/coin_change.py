def coin_change(coins, amount):

    current = amount
    queue = [amount]
    numbers={current: 0}
    while(len(queue)>0):
        current = queue.pop(0)
        for c in coins:
            cost = current - c
            if cost >=0:
                coin_num = numbers[current] + 1
                if not cost in numbers:
                    numbers[cost] = coin_num
                    queue.append(cost)
                else:
                    if coin_num < numbers[cost]:
                        numbers[cost] = coin_num

    return numbers[0] if 0 in numbers else -1

def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)