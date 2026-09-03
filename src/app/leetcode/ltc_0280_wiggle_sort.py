"""
Leetcode Problem 280: Wiggle Sort | https://leetcode.com/problems/wiggle-sort/
"""

class WiggleSort:

    def sort(self, nums: list[int]) -> None:
        """
        :type nums: list[int]
        :rtype: None
        """
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or\
                (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
