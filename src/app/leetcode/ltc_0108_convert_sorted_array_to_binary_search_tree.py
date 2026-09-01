"""
Convert Sorted Array to Binary Search Tree | Leetcode 108 | Medium | https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from app.common.tree_node import TreeNode


class ConvertSortedArrayToBinarySearchTree:

    def sorted_array_to_bst(self, nums):
        return self.get_helper(nums, 0, len(nums) - 1)

    def get_helper(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.get_helper(nums, start, mid - 1)
        node.right = self.get_helper(nums, mid + 1, end)
        return node