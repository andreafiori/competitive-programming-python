"""
Minimum Moves to Equal Array Elements | https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
"""
class MinimumMovesToEqualArrayElements:

    def min_moves(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        min_num = min(nums)
        return sum([i - min_num for i in nums])
