# MEDIUM

# Given a sequence of integers as an array, determine whether it is possible to obtain a
# strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
# Sequence containing only one element is also considered to be strictly increasing.

# Example

#     For sequence = [1, 3, 2, 1], the output should be
#     almostIncreasingSequence(sequence) = false.

#     There is no one element in this array that can be removed in order to get a strictly increasing sequence.

#     For sequence = [1, 3, 2], the output should be
#     almostIncreasingSequence(sequence) = true.

#     You can remove 3 from the array to get the strictly increasing sequence [1, 2].
#     Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer sequence

#     Guaranteed constraints:
#     2 ≤ sequence.length ≤ 105,
#     -105 ≤ sequence[i] ≤ 105.

#     [output] boolean
#         Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.


def almostIncreasingSequence_OPTIMAL(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


def almostIncreasingSequence(sequence):
    lenSeq = len(sequence)
    lenUnique = len(set(sequence))

    # only 2 elements so removing 1 should return true
    if lenSeq == 2:
        return True

    # Sequence is already in order and no duplicates exist
    ordered = sequence.copy()
    ordered.sort()
    if (ordered == sequence) and (lenSeq == lenUnique):
        return True

    newSeq = []
    for idx, num in enumerate(sequence):
        newSeq = sequence[0:idx] + sequence[idx + 1:len(sequence)]
        ordered = newSeq.copy()
        ordered.sort()
        if (ordered == newSeq) and (len(ordered) == len(set(ordered))):
            return True
    return False


testData1 = [1, 1]
testData2 = [1, 1, 2, 3, 4, 4]
print(almostIncreasingSequence(testData1))
print(almostIncreasingSequence(testData2))
