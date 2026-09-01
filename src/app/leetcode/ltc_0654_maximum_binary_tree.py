"""
Maximum Binary Tree | leetcode 654 | https://leetcode.com/problems/maximum-binary-tree/

"""

from typing import List

from app.common.tree_node import TreeNode

class MaxBinaryTree:

    def solution(self, nums: List[int]) -> TreeNode:
        """
        :param nums: List[int]
        :return: TreeNode
        """
        # O (n^2) and O(n)
        if nums is None or len(nums) == 0:
            return None
        max_index, max_value = 0, 0
        for i, value in enumerate(nums):
            if value >= max_value:
                max_value = value
                max_index = i
        root = TreeNode(max_value)
        root.left = self.solution(nums[:max_index])
        root.right = self.solution(nums[max_index+1:])
        return root
