import sys

from common.tree_node import TreeNode

"""
Recovery Binary Search Tree | https://leetcode.com/problems/recover-binary-search-tree/
"""
class RecoveryBinarySearchTree:

    def __init__(self):
        self.first = self.second = None
        self.pre = TreeNode(-sys.maxsize - 1)

    def recover_tree(self, root):
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        if self.pre.val >= root.val:
            if self.first is None:
                self.first = self.pre
            if self.first is not None:
                self.second = root
        self.pre = root
        self.traverse(root.right)
