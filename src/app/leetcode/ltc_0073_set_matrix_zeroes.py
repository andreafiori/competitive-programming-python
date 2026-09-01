"""
Leetcode Problem 73. Set Matrix Zeroes | https://leetcode.com/problems/set-matrix-zeroes/

"""

class SetMatrixZeroes:

    def solution(self, matrix: list[list[int]]) -> None:
        """
        :type matrix: list[list[int]]
        :rtype: None
        """
        if not matrix:
            return
        m = len(matrix)
        if m == 0:
            return
        r = []
        c = []
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        # row with zero
        r = set(r)
        # column with zero
        c = set(c)
        for i in r:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in c:
                matrix[i][j] = 0
