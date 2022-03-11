# problem:
# find closest value in BST to a given target value

# logic:
# check absolute difference between currentClosest and currentNode.
# select left subtree or right subtree or node as current closest based on BST properties.
# i.e. values on right of node are always bigger than node and on the left are always smaller than node.

# Average: O(nlog(n)) time O(nlog(n)) space
# worst case O(n) time O(n) space
from binarytree import bst


#
#
# def findClosestValueInBst(tree, target_value):
#     return findClosestValueInBstHelper(tree, target_value, float("inf"))
#
#
# def findClosestValueInBstHelper(tree, target_value, closest_value):
#     if tree is None:
#         return closest_value
#
#     if abs(target_value - closest_value) > abs(target_value - tree.value):
#         closest_value = tree.value
#
#     if target_value < tree.value:
#         return findClosestValueInBstHelper(tree.left, target_value, closest_value)
#     elif target_value > tree.value:
#         return findClosestValueInBstHelper(tree.right, target_value, closest_value)
#     else:
#         return closest_value

# Average: O(nlog(n)) time, O(1) space
# Worst: O(nlog(n)) time, O(1) space
def findClosestValueInBst(bst_tree, target_value):
    return findClosestValueInBstHelper(bst_tree, target_value, float("inf"))


def findClosestValueInBstHelper(tree, target_value, closest_value):
    current_node = tree
    while current_node is not None:
        if abs(target_value - closest_value) > abs(target_value - current_node.value):
            closest_value = current_node.value

        if target_value < current_node.value:
            current_node = current_node.left
        elif target_value > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest_value


if __name__ == "__main__":
    tree = bst()
    print(tree)
    print(findClosestValueInBst(tree, 12))
