"""
Guess Number Higher or Lower II | htttp://leetcode.com/problems/guess-number-higher-or-lower-ii/

https://discuss.leetcode.com/topic/51353/simple-dp-solution-with-explanation/2

"""

import sys

class GuessNumberHigherOrLowerII:

    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(2, n + 1):
            for i in range(j - 1, 0, -1):
                global_min = sys.maxsize
                for k in range(i + 1, j):
                    local_max = k + max(dp[i][k - 1], dp[k + 1][j])
                    global_min = min(global_min, local_max)
                if i + 1 == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = global_min
        return dp[1][n]
