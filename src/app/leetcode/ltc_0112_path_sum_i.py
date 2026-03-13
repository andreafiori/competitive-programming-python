"""
Path Sum | https://leetcode.com/problems/path-sum/
"""

from common.tree_node import TreeNode

class PathSum:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        sum = sum - root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        # check left
        left = self.has_path_sum(root.left, sum)
        # check right
        right = self.has_path_sum(root.right, sum)
        return (left or right)
