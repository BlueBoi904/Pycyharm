"""

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.


(i.e., from left to right, then right to left for the next level and alternate between).


"""

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    if root is None:
        return []

    results = []

    def dfs(node, level):
        if level >= len(results):
            results.append(deque([node.val]))
        else:
            if level % 2 == 0:
                results[level].append(node.val)
            else:
                results[level].appendleft(node.val)

        for next_node in [node.left, node.right]:
            if next_node is not None:
                dfs(next_node, level + 1)

    # normal level order traversal with DFS
    dfs(root, 0)

    return results
