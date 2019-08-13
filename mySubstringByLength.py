# https://app.codesignal.com/challenge/MbQ2B83RMHNtRwxZL
# Implement an algorithm that can output a substring of the given string
# given a starting point and a length.


def mySubstringByLength(inputString, start, length):
    return inputString[start:start+length]

print(mySubstringByLength("abcde", 2, 3))
