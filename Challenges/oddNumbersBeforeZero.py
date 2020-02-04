# https://app.codesignal.com/challenge/YZkenvHqAjS9fh7HM
# Given an array of integers, count the odd numbers before the first
# (i.e. leftmost) occurrence of zero.


def oddNumbersBeforeZero(sequence):
    oddFound = 0
    if 0 not in sequence:
        return 0

    for digit in sequence:
        if digit == 0:
            return oddFound
        if digit % 2 != 0:
            oddFound += 1
    return oddFound


print(oddNumbersBeforeZero([1, 2, 3, 0, 5]))
