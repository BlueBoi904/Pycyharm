"""

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    res = []

    if root is None:
        return res

    def levels(node, level=0):
        if node is None:
            return
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        levels(node.left, level + 1)
        levels(node.right, level + 1)

    levels(root)
    return res
