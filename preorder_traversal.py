"""

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Stack approach
def preorder(root):
    if root is None:
        return []
    # Check that root is not None, if so return an empty array
    stack, res = [root], []
    # Initiate base values for result and the stack.

    while stack:
        # Root is stack.pop()
        root = stack.pop()
        # Add the popped value to res
        res.append(root.val)
        # Combine root.
        stack.extend(root.children[::-1])
    return res


# recursive approach

def preorder_re(root):
    if root is None:
        return []
    res = []

    def helper(node):
        res.append(node.val)
        for node in node.children:
            if node is not None:
                helper(node)

    helper(root)
    return res


def postorder(root):
    if root is None:
        return []

    stack, output = [root, ], []
    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
        for c in root.children:
            stack.append(c)

    return output[::-1]
