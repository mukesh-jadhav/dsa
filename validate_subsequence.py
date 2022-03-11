# problem
    # given a two lists of non-repeating numbers, check if second list is contained in first list.
    # the numbers in the second list could be sequential or with some gap between them.
    # it's just that their order should be same.
    # e.g. [1, 6, -1 , 10] is a valid subsequence of [5, 1, 22, 25, 6, -1, 8, 10]

#logic:
    # don't check for whole sequence, check smaller sequence in bigger.
    # Also once one is found, check the next in rest of the sequence.

# O(N) time, O(1) space -> N = length of array
def isValidSubsequence(array, sequence):
    for element in sequence:
        if element in array:
            array = array[array.index(element)+1:]
        else:
            return False
    return True


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))
