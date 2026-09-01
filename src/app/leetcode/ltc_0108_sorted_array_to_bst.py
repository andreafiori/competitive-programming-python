"""
Leetcode 108. Sorted array to bst | https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given a sorted array of int, convert it to a balanced binary search tree

method: take middle element as root, use recursion for depth first, add each subtree as a balanced bst

"""

from app.common.tree_node import TreeNode

class SortedArrayToBST:

    def solution(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(val = nums[mid])
        root.left = self.solution(nums[:mid])
        root.right = self.solution(nums[mid+1:])

        return root
