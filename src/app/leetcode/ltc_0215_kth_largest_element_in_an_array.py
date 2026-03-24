"""
Kth Largest Element in an Array | https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
import random

class KthLargestElementInAnArray:

    def find_kth_largest(self, nums: list[int], k: int) -> int:
        # shuffle nums to avoid n*n
        random.shuffle(nums)
        return self._quick_selection(nums, 0, len(nums) - 1, len(nums) - k)

    def _quick_selection(self, nums: list[int], start: int, end: int, k: int) -> int:
        if start > end:
            return float('inf')
        pivot = nums[end]
        left = start
        for i in range(start, end):
            if nums[i] <= pivot:
                # swip left and i
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[end] = nums[end], nums[left]
        if left == k:
            return nums[left]
        elif left < k:
            return self._quick_selection(nums, left + 1, end, k)
        else:
            return self._quick_selection(nums, start, left - 1, k)
