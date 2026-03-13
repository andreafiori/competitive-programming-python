"""
Nim Game | https://leetcode.com/problems/nim-game/
"""
class NimGame:

    def can_win_nim(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
