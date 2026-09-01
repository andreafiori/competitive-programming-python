"""
Find All Numbers Disappeared in an Array | leetcode 448 | https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

class FindAllNumbersDisappearedInAnArray:
    def find_disappeared_numbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        if nums:
            n = len(nums)
            for i in range(n):
                val = abs(nums[i]) - 1
                if nums[val] > 0:
                    nums[val] = -nums[val]
            for i in range(n):
                if nums[i] > 0:
                    res.append(i + 1)
        return res
