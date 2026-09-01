"""
Leetcode Problem: 78. Subsets | https://leetcode.com/problems/subsets/
"""

class Subsets:

    def solution(self, nums):
        # Sort and iteratively generate n subset with n-1 subset, O(n^2) and O(2^n)
        nums.sort()
        res = [[]]
        for index in range(len(nums)):
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
        return res
