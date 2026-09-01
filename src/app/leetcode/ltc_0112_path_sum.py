"""
Path Sum | leetcode 112 | https://leetcode.com/problems/path-sum/
"""


class PathSum:
    def solution(self, root, sum):
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
        left = self.solution(root.left, sum)
        # check right
        right = self.solution(root.right, sum)
        return (left or right)
