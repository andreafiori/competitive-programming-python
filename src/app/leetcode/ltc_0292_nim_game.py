"""
Nim Game | leetcode 292 | https://leetcode.com/problems/nim-game/
"""

class NimGame:

    def solution(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0