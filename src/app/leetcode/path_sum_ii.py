"""
113. Path Sum II | https://leetcode.com/problems/path-sum-ii/

"""

from common.tree_node import TreeNode

class PathSumII:
    def pathSum(self, root: TreeNode, sum: int):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        if sum == root.val and root.left is None and root.right is None:
            return [[root.val]]
        # left side
        left_res = self.pathSum(root.left, sum - root.val)
        # right side
        right_res = self.pathSum(root.right, sum - root.val)
        # add current prefix
        for t in left_res + right_res:
            res.append([root.val] + t)
        return res
