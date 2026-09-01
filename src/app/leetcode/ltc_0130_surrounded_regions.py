"""
Leetcode Problem: 130. Surrounded Regions | https://leetcode.com/problems/surrounded-regions/

"""

class SurroundedRegions:

    def solution(self, board: list[list[str]]) -> None:
        """
        :type board: list[list[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not any(board): return
        height, width = len(board), len(board[0])
        save = [ij for k in range(height + width) for ij in ((0, k), (height - 1, k), (k, 0), (k, width - 1))]
        while save:
            i, j = save.pop()
            if 0 <= i < height and 0 <= j < width and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
