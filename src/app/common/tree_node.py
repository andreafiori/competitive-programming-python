"""
TreeNode class definition for binary tree nodes.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        :param val: The value of the node.
        :param left: The left child of the node.
        :param right: The right child of the node.
        """
        self.val = val
        self.left = left
        self.right = right
