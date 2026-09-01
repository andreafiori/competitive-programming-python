"""
Binary Tree Longest Consecutive Sequence | leetcode 298 | https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

"""

class BinaryTreeLongestConsecutiveSequence:
    def solution(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.longest_consecutive_helper(root, -10000, 1)

    def longest_consecutive_helper(self, root, previous, curr):
        # Top down recursion
        if root is None:
            return 0
        if root.val - 1 == previous:
            curr += 1
        else:
            curr = 1
        l_res = self.longest_consecutive_helper(root.left, root.val, curr)
        r_res = self.longest_consecutive_helper(root.right, root.val, curr)
        return max(curr, l_res, r_res)
