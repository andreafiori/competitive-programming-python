"""
Binary Tree Longest Consecutive Sequence

You are given the root of a binary tree. Your task is to find the length of the longest consecutive sequence path in the tree.

A consecutive sequence path is defined as a path where each node's value is exactly one more than its parent node's value in the path. For example, a path with values 1 → 2 → 3 is a consecutive sequence.

Key constraints to note:

The path can start at any node in the tree (not necessarily the root)
The path must follow parent-to-child connections only (you cannot traverse from a child back to its parent)
The values must increase by exactly 1 at each step along the path
For example, if you have a tree where a parent node has value 5, only a child with value 6 would continue the consecutive sequence. A child with value 7 or 4 would start a new sequence.

The function should return an integer representing the maximum length of any consecutive sequence path found in the tree.
"""

class BinaryTreeLongestConsecutiveSequence:
    def longestConsecutive(self, root):
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

    # def __init__(self):
    #     self.max_length = 0

    # def longest_consecutive(self, root):
    #     self.longestConsecutive_helper(root)
    #     return self.max_length

    # def longest_consecutive_helper(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # Bottom up
    #     if root is None:
    #         return 0
    #     l_res = self.longestConsecutive_helper(root.left) + 1
    #     r_res = self.longestConsecutive_helper(root.right) + 1
    #     if root.left is not None and root.val + 1 != root.left.val:
    #         l_res = 1
    #     if root.right is not None and root.val + 1 != root.right.val:
    #         r_res = 1
    #     length = max(l_res, r_res)
    #     self.max_length = max(self.max_length, length)
    #     return length
