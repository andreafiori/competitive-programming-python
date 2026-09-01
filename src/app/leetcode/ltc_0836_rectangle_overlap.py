"""
Leetcode Problem: 836. Rectangle Overlap | https://leetcode.com/problems/rectangle-overlap/
"""

class RectangleOverlap:

    def solution(self, rec1: list[int], rec2: list[int]) -> bool:
        """
        :type rec1: list[int]
        :type rec2: list[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top
