# EASY

# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.string inputArray

# A non-empty array.

# Guaranteed constraints:
# 1 ≤ inputArray.length ≤ 10,
# 1 ≤ inputArray[i].length ≤ 10.

# [output] array.string

# Array of the longest strings, stored in the same order as in the inputArray.


def allLongestStrings(inputArray):
    maxLen = len(max(inputArray, key=len))
    answer = []
    for elm in inputArray:
        if len(elm) == maxLen:
            answer.append(elm)
    return answer


testData = ["enyky", "benyky", "yely", "varennyky"]

print(allLongestStrings(testData))