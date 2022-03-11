# problem: calculate sum of node depths of the whole tree

# logic: recursively -> the root node has zero depth. and its children has 0(current_depth) + 1

# O(V+E) time and O(V) space where V is vertices or nodes and E is no of edges connecting the nodes
from binarytree import bst


def nodeDepths(root, depth):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


if __name__ == "__main__":
    tree = bst()
    print(tree)
    print(nodeDepths(tree, 0))
