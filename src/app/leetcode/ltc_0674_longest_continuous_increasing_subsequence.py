"""
Longest Continuous Increasing Subsequence | https://leetcode.com/problems/longest-continuous-increasing-subsequence/
"""
class LongestContinuousIncreasingSubsequence:

    def find_length_of_LCIS(self, nums):
        if not nums or len(nums) == 0:
            return 0
        ans = curr = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
        return ans
