"""
Maximal Square | Leetcode 221 | Medium | https://leetcode.com/problems/maximal-square/

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

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
