# EASY

# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

#     For n = 1230, the output should be
#     isLucky(n) = true;
#     For n = 239017, the output should be
#     isLucky(n) = false.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A ticket number represented as a positive integer with an even number of digits.

#     Guaranteed constraints:
#     10 ≤ n < 106.

#     [output] boolean
#         true if n is a lucky ticket number, false otherwise.


def isLucky_OPTIMAL(n):
    s = str(n)
    pivot = len(s) // 2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))


def isLucky(n):
    inputNum = str(n)
    midpoint = (len(inputNum) // 2) - 1
    seg1, seg2 = 0, 0

    for idx, digit in enumerate(inputNum):
        if idx <= midpoint:
            seg1 = seg1 + int(digit)
        else:
            seg2 = seg2 + int(digit)
    return seg1 == seg2


print(isLucky(1230))
