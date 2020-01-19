# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".


def commonCharacterCount(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    listmatch = []

    for i in s1:
        if i in s2:
            listmatch.append(1)
            s2.remove(i)

    return(sum(listmatch))


s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1, s2))
