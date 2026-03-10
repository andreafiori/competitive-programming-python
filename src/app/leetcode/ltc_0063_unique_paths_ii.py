"""
Unique Paths II | https://leetcode.com/problems/unique-paths-ii/
"""
class UniquePathsII:

    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:
        m, n = len(obstacle_grid), len(obstacle_grid[0])
        if m == 0:
            return 0
        dmap = [[0] * (n + 1) for _ in range(m + 1)]
        dmap[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in  range(n - 1, -1, -1):
                if obstacle_grid[i][j] == 1:
                    dmap[i][j] = 0
                else:
                    dmap[i][j] = dmap[i][j + 1] + dmap[i + 1][j]
        return dmap[0][0]
