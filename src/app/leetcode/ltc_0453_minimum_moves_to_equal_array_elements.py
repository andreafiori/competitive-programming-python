"""
Minimum Moves to Equal Array Elements | Leetcode 453 | https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

"""

class MinimumMovesToEqualArrayElements:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        min_num = min(nums)
        return sum([i - min_num for i in nums])
