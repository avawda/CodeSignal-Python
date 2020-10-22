# EASY

# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]


def addBorder(picture):
    topBottom = "*"*(len(picture[0])+2)

    output = [topBottom]
    for text in picture:
        output.append("*"+text+"*")

    output.append(topBottom)
    return output


input = ["abc",
         "ded"]

print(addBorder(input))
