# Easy

# Several people are standing in a row and need to be divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. Return an array of two integers,
# where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

# Example

# For a = [50, 60, 60, 45, 70], the output should be
# alternatingSums(a) = [180, 105].

# Input/Output

# [execution time limit] 3 seconds (cs)

# [input] array.integer a

# Guaranteed constraints:
# 1 ≤ a.length ≤ 105,
# 45 ≤ a[i] ≤ 100.

# [output] array.integer


def alternatingSums(input):
    odd = True
    array1 = []
    array2 = []

    for num in input:
        if odd:
            array1.append(num)
        else:
            array2.append(num)
        odd = not odd
    output = [sum(array1), sum(array2)]
    return output


input = [50, 60, 60, 45, 70]
print(alternatingSums(input))


##########################
# Highest Rated Solution
##########################
# def alternatingSums(a):
#     return [sum(a[::2]),sum(a[1::2])]
