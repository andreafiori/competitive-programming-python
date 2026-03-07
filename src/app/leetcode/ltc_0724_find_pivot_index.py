"""
724. Find Pivot Index | https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""

from typing import List

class FindPivotIndex:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

    def find(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = sum(nums)
        leftsum = 0
        for i, v in enumerate(nums):
            # leftsum == rightsum
            if leftsum == totalsum - leftsum - v:
                return i
            leftsum += v
        return -1
