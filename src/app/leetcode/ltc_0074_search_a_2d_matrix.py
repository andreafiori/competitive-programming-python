"""
Leetcode Problem: 74. Search a 2D Matrix | https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length

"""

class SearchMatrix:

    def solution(self, matrix: list[list[int]], target: int) -> bool:
        try:
            ls_row, ls_col = len(matrix), len(matrix[0])
        except:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        begin, end = 0, ls_row * ls_col - 1
        while begin <= end:
            mid = (begin + end) // 2
            row, col = mid // ls_col, mid % ls_col
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return False
