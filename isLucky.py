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


def isLucky(n):
    n = str(n)
    if (len(n) % 2) != 0:
        return False

    mid = len(n)/2
    part1 = 0
    part2 = 0
    for idx, digit in enumerate(n):
        if idx < mid:
            part1 += int(digit)
        else:
            part2 += int(digit)
    if part1 == part2:
        return True
    else:
        return False


print(isLucky(123))
print(isLucky(1230))
print(isLucky(239017))
