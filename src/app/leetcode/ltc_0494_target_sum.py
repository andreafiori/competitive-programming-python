"""
Target sum | leetcode 494 | https://leetcode.com/problems/target-sum/

Given an array of integers nums and an integer target, return the number of ways to assign + and - signs to make the sum of nums equal to target.

Example 1:
    Input: nums = [1,1,1,1,1], target = 3
    Output: 5

Example 2:
    Input: nums = [1], target = 1
    Output: 1

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000
"""

class TargetSum:
    def solution(self, nums: list[int], target: int) -> int:
        N = len(nums)
        mem = dict()

        if N == 0:
            return 0

        def knapsack(n, s):
            if n == N:
                return 1 if s == target else 0

            if (n, s) in mem:
                return mem[(n, s)]

            mem[(n, s)] = knapsack(n+1, s + nums[n]) + knapsack(n+1, s - nums[n])
            return mem[(n, s)]

        return knapsack(0, 0)
