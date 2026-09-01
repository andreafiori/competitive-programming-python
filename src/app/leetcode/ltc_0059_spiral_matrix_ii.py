"""
Leetcode 59. Spiral Matrix II | https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20

"""

class SpiralMatrixII:

    def solution(self, n: int) -> list[list[int]]:
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        pos = [0, 0]
        move = (0, 1)
        for index in range(1, n * n + 1):
            res[pos[0]][pos[1]] = index
            if res[(pos[0] + move[0]) % n][(pos[1] + move[1]) % n] > 0:
                # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
                move = (move[1], -1 * move[0])
            pos[0] = pos[0] + move[0]
            pos[1] = pos[1] + move[1]
        return res
