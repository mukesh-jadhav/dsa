# problem: accept a BST and return list of its branch sums ordered from leftmost branch sum to rightmost branchsum

# logic: recursively pass on branch_sum and keep adding it to result

# O(N) time and O(N)
from binarytree import bst


def branchSums(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums


def calculateBranchSum(node, currentSum, sums):
    if node is None:
        return

    currentSum += node.value
    if node.left is None and node.right is None:
        sums.append(currentSum)
        return

    calculateBranchSum(node.left, currentSum, sums)
    calculateBranchSum(node.right, currentSum, sums)


if __name__ == "__main__":
    tree = bst()
    print(tree)
    print(branchSums(tree))