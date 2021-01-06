# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 50.

# [output] boolean

# true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.


def palindromeRearranging(inputString):
    if isPalindrome(inputString) or len(inputString) == 1:
        return True

    unique = ''.join(set(inputString))
    # Check if EVEN number of elements. If so, it must not have unique character
    if len(inputString) % 2 == 0:
        print("even")
        for char in unique:
            # Return false if we find odd number of characters within an even string
            if inputString.count(char) % 2 != 0:
                return False
        # Even set of characters in string with no odd sets, therefore palindromic
        return True
    else:
        print("odd")
        uniqueFound = False
        for char in unique:
            # Return false if we find more than a single odd number of characters within an even string
            if inputString.count(char) % 2 != 0:
                if uniqueFound:
                    return False
                else:
                    uniqueFound = True
        # Even set of characters in string with no odd sets, therefore palindromic
        return uniqueFound


def isPalindrome(checkString):
    return checkString == checkString[::-1]


input = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa"
print(palindromeRearranging(input))
