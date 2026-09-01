"""
Longest consecutive sequence | leetcode 128 | https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
- 0 <= nums.length <= 105
- 109 <= nums[i] <= 109)

"""

class LongestConsecutiveSequence:

    def longest_consecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0

        all = set(nums)
        longest = 0

        for each in all:
            if each - 1 not in all:
                curr = each
                seq = 1
                while curr + 1 in all:
                    seq += 1
                    curr = curr + 1
                if seq > longest:
                    longest = seq

        return longest
