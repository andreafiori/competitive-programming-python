"""
Leetcode 1260: Shift 2D Grid | https://leetcode.com/problems/shift-2d-grid/

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100


"""

class Shift2dGrid:
    def solution(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # m * n temp array
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        # Compute final location
        true_k = k % (m * n)
        # row move
        move_i = true_k / n
        # col move
        move_j = true_k % n

        for i in range(m):
            for j in range(n):
                new_i = i + move_i
                # move one row if move_j + j >= n
                if move_j + j >= n:
                    new_i += 1
                new_i %= m
                new_j = (j + move_j) % n
                new_grid[new_i][new_j] = grid[i][j]
        return new_grid
