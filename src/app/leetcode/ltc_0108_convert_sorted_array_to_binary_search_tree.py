"""
Convert Sorted Array to Binary Search Tree | https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from app.common.tree_node import TreeNode

class ConvertSortedArrayToBinarySearchTree:

    def sortedArrayToBST(self, nums):
        # Recursion with index
        return self.getHelper(nums, 0, len(nums) - 1)

    def getHelper(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        node.left = self.getHelper(nums, start, mid - 1)
        node.right = self.getHelper(nums, mid + 1, end)
        return node