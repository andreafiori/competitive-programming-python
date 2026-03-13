"""
Paint Fence | https://leetcode.com/problems/paint-fence/
"""
class PaintFence:

    def num_ways(self, n, k):
        if n == 0:
            return 0
        elif n == 1:
            return k
        dp = [0] * 2
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            temp = dp[1]
            dp[1] = sum(dp) * (k - 1)
            dp[0] = temp
        return dp[1]