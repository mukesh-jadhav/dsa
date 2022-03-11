#problem
    # given a list of non-repeating numbers, find the pair of numbers that sum up to given target sum

#logic
    # bruit-force solution: iterate on each number and check for sum

# O(n^2) time , O(1) space
# def twoNumbersSum(array, targetSum):
#     for index, number in enumerate(array):
#         for next_number in array[index+1:]:
#             if number + next_number == targetSum:
#                 return [number, next_number]
#     return []

# logic:
    # use hashtable, store visited number in dict and check for it so that you won't have to use double for loop

# O(n) time, O(n) space
# def twoNumbersSum(array, targetSum):
#     hashTable = {}
#     for number in array:
#         potential_match = targetSum - number
#         if potential_match in hashTable.keys():
#             return [number, targetSum - number]
#         else:
#             hashTable[number] = True
#     return []


#logic:
    # sort array, use two pointers, start and end. while both pointers do not become equal,
    # check if the numbers they point to, sum up to targetSum

# O(nlog(n)) time, O(1) space
def twoNumbersSum(array, targetSum):
    array.sort()

    pointer_left = 0
    pointer_right = len(array)-1

    while pointer_left != pointer_right:
        currentSum = array[pointer_left] + array[pointer_right]
        if currentSum < targetSum:
            pointer_left += 1
        elif currentSum > targetSum:
            pointer_right -= 1
        else:
            return [array[pointer_left], array[pointer_right]]

    return []


if __name__ == "__main__":
    input_list = [-4, -1, 1, 3, 5, 6, 8, 11]
    target_sum = 13
    print(twoNumbersSum(input_list, target_sum))
