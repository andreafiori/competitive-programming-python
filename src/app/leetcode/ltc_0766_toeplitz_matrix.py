"""
Toeplitz Matrix | https://leetcode.com/problems/toeplitz-matrix/
"""
class ToeplitzMatrix:
    """ Time: O(m*n) | Space: O(1) """

    def is_toeplitz_matrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Actually, we don't need to check the last row and column
        for r in range(len(matrix) - 1):
            for c in range(len(matrix[0]) - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True
