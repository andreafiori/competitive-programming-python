"""
Maximal Square | Leetcode 221 | Medium | https://leetcode.com/problems/maximal-square/
"""

class MaximalSquare:

    def solution(self, matrix: list[list[str]]) -> int:
        """
        :param matrix: list[list[str]]
        :return: int
        """
        if matrix is None or len(matrix) == 0:
            return 0
        rows, cols, res, prev = len(matrix), len(matrix[0]), 0, 0
        dp = [0] * (cols + 1)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return res * res
