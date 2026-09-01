"""
Jump game | https://leetcode.com/problems/jump-game-ii/

"""

from typing import List

class JumpGameII:
    def jump(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        end = 0 + nums[0]
        start = 0
        step = 1
        max_dis = 0 + nums[0]
        while end < len(nums) - 1:
            for i in range(start + 1, end + 1):
                # greedy
                max_dis = max(max_dis, nums[i] + i)
            start = end
            end = max_dis
            step += 1
        return step
