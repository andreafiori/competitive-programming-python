"""
Path Sum II | leetcode 113 | https://leetcode.com/problems/path-sum-ii/

"""

from app.common.tree_node import TreeNode

class PathSumII:

    def solution(self, root: TreeNode, sum: int):
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
        left_res = self.solution(root.left, sum - root.val)
        # right side
        right_res = self.solution(root.right, sum - root.val)
        # add current prefix
        for t in left_res + right_res:
            res.append([root.val] + t)
        return res
