"""
Move Zeroes | leetcode 283 | https://leetcode.com/problems/move-zeroes/
"""

class MoveZeroes:

    def move(self, nums):
        # O(n)
        ls = len(nums)
        n_pos = 0
        for i in range(ls):
            if nums[i] != 0:
                temp = nums[n_pos]
                nums[n_pos] = nums[i]
                nums[i] = temp
                n_pos += 1


