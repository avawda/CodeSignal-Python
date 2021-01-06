# Easy

# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one.
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

# Example

# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3


def arrayChange(inputArray):
    total = 0
    for i in range(len(inputArray)-1):
        n1 = inputArray[i]
        n2 = inputArray[i+1]
        if n2 <= n1:
            total += abs(n2-n1)+1
            inputArray[i+1] = inputArray[i]+1
    return total


input = [1, 2, 3]
print(arrayChange(input))
