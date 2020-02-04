# EASY

# Some people are standing in a row in a park. There are trees between them which cannot be moved.
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 1000,
#     -1 ≤ a[i] ≤ 1000.


def sortByHeight_OPTIMAL(a):

    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l


def sortByHeight(a):
    heights = []
    # Extract the heights of people and then sort
    for i in a:
        if i > 0:
            heights.append(i)
    heights.sort()

    # Go through the list and replace peoples heights with the ordered versions
    output = a.copy()
    pos = 0
    for idx, elm in enumerate(a):
        if elm > 0:
            output[idx] = heights[pos]
            pos += 1
    return output


testData = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(testData))
