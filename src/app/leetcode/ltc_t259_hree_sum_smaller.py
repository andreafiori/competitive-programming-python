"""
3 Sum Smaller | https://leetcode.com/problems/3sum-smaller/
"""
class ThreeSumSmaller:
    """ Triple Sum Smaller different solutions """

    def sum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # https://leetcode.com/articles/3sum-smaller/#approach-2-binary-search-accepted
        nums.sort()
        ls = len(nums)
        res = 0
        for i in range(ls - 1):
            res += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return res

    def sum2(self, nums, start, target):
        res, left, right = 0, start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res