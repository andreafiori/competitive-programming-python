"""
Single Number II | https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,3,2]
    Output: 3

Example 2:
    Input: [0,1,0,1,0,1,99]
    Output: 99

"""
class SingleNumberII:

    def solution(self, nums: list[int]) -> int:
        """
        # bitmask
        # ones as a bitmask to represent the ith bit had appeared once.
        # twos as a bitmask to represent the ith bit had appeared twice.
        # threes as a bitmask to represent the ith bit had appeared three times.
        :param nums: int
        :return: int
        """
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
