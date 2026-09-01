"""
Flip Game II | leetcode 294 | https://leetcode.com/problems/flip-game-ii/
"""

class FlipGameII:

    def can_win(self, s: str) -> bool:
        if s is None or len(s) < 2:
            return False
        list_s = list(s)
        return self._can_win_helper(list_s)

    def _can_win_helper(self, s: list[str]) -> bool:
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                s[i] = '-'
                s[i + 1] = '-'
                res = self._can_win_helper(s)
                s[i] = '+'
                s[i + 1] = '+'
                if not res:
                    return True
        return False
