"""
Paint Fence | LeetCode 276 | https://leetcode.com/problems/paint-fence/

"""

class PaintFence:

    def solution_one(self, n: int, k: int) -> int:
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        w = [0, k, k*k]
        while len(w) <= n:
            w += sum(w[-2:]) * (k-1),
        return w[n]

    def solution_two(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return k
        dp = [0] * 2
        dp[0] = k
        dp[1] = k * k
        for _ in range(2, n):
            temp = dp[1]
            dp[1] = sum(dp) * (k - 1)
            dp[0] = temp
        return dp[1]
