"""
House Robber | leetcode 198 | Medium | https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
class HouseRobber:

    def rob_dp(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp
        ls = len(nums)
        if ls == 0:
            return 0
        dp = [0] * ls
        dp[0] = nums[0]
        for i in range(1, ls):
            if i < 2:
                dp[i] = max(nums[i], dp[i - 1])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[ls - 1]

    def rob_iterative(self, nums: list[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[-1]

    def rob_optimized(self, nums: list[int]) -> int:
        prev_max = curr_max = 0
        for num in nums:
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp
        return curr_max
