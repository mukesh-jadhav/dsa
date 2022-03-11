# problem:
    # given a non-empty array of integers that are sorted in ascending order,
    # return new array with squares of all numbers in original array also in ascending order

#logic:
    # bruit-force solution: iterate on items, perform squares and insert into another list, sort that list.

# O(nlog(n)) time, O(n) space
# def sortedSquaredArray(array):
#     sortedSquares = [0 for _ in array]
#     for idx in range(len(array)):
#         value = array[idx]
#         sortedSquares[idx] = value * value
#
#     sortedSquares.sort()
#     return sortedSquares

#logic:
    # maintain start, end pointer, compare their absolutes, if start > right, increment start, put smaller's square in list
    # else increment end, put end's square in list

# O(n) time and O(n) space
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) -1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx]  = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    print(sortedSquaredArray(array))