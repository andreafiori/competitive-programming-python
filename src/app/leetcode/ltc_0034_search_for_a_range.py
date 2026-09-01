"""
Leetcode Problem: 34. Find First and Last Position of Element in Sorted Array | https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""

class FindLastPositionOfElementInSortedArray:

    def solution(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]
        _min = 0
        _max = length - 1
        while _min <= _max:
            pos = (_min + _max) / 2
            if nums[pos] > target:
                _max = pos - 1
            elif nums[pos] < target:
                _min = pos + 1
            else:
                # when nums[pos] == target find the min and max
                for i in range(_min, _max + 1):
                    if nums[i] == target:
                        if _min < i and nums[_min] != nums[i]:
                            _min = i
                        _max = i
                return [_min, _max]
        return [-1, -1]