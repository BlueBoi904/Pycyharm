"""

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode):
    def valid(node: TreeNode, low=float('-inf'), high=float('inf')):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return (valid(node.right, node.val, high) and
                valid(node.left, low, node.val))

    return valid(root)
