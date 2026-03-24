"""
Missing Number | https://leetcode.com/problems/missing-number/
"""
class MissingNumber:

    def find_missing_number(self, nums):
        res = len(nums)
        for i, v in enumerate(nums):
            res ^= i
            res ^= v
        return res

    # def find_missing_number2(self, nums):
    #     nums.sort()
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = (left + right) / 2
    #         if nums[mid] <= mid:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return left

    # def find_missing_number3(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     return (n ** 2 + n) / 2 - sum(nums)