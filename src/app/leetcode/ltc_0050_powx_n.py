"""
Pow(x, n) | LeetCode 50 | https://leetcode.com/problems/powx-n/

https://leetcode.com/discuss/93413/iterative-log-n-solution-with-clear-explanation
"""

class PowXN:

    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res ,curr = 1, abs(n)
        while curr > 0:
            if curr & 1 == 1:
                res *= x
            curr >>= 1
            x *= x
        if n < 0:
            return 1 / res
        return  res
