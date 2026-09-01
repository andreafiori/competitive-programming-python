"""
House Robber II | leetcode 213 | https://leetcode.com/problems/house-robber-ii/

"""

class HouseRobberII:

    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums, 0, len(nums) - 2), self.rob_helper(nums, 1, len(nums) - 1))

    def rob_helper(self, nums: list[int], low: int, high: int) -> int:
        prev_max = curr_max = 0
        for index in range(low, high + 1):
            temp = curr_max
            curr_max = max(prev_max + nums[index], curr_max)
            prev_max = temp
        return curr_max
