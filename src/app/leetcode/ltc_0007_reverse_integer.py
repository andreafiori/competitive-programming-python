"""
Leetcode Problem 7: Reverse Integer | https://leetcode.com/problems/reverse-integer/
"""

class ReverseInteger:

    def solution(self, x: int) -> int:
        res, is_pos = 0, 1
        if x < 0:
            is_pos = -1
            x = -1 * x
        while x != 0:
            res = res * 10 + x % 10
            if res > 2147483647:
                return 0
            x //= 10
        return res * is_pos
