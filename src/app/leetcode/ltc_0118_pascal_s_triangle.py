"""
Pascal's Triangle | leetcode 118 | https://leetcode.com/problems/pascals-triangle/
"""

class PascalsTriangle:

    def solution(self, num_rows):
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(num_rows):
            result.append([0] * (i + 1))
        for i in range(num_rows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
