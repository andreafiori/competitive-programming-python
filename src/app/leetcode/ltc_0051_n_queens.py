"""
N queens | leetcode | https://leetcode.com/problems/n-queens/

"""

class NQueens:

    def solve_n_queens(self, n: int) -> list[list[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # recusive
        if n == 0:
            return 0
        res = []
        board = [['.'] * n for _ in range(n)]
        self._recursive_helper(res, board, n)
        return res

    def _recursive_helper(self, res: list[list[str]], board: list[list[str]], num: int):
        if num == 0:
            res.append([''.join(t) for t in board])
            return
        ls = len(board)
        pos = ls - num
        check = [True] * ls
        for i in range(pos):
            for j in range(ls):
                if board[i][j] == 'Q':
                    check[j] = False
                    step = pos - i
                    if j + step < ls:
                        check[j + step] = False
                    if j - step >= 0:
                        check[j - step] = False
                    break
        for j in range(ls):
            if check[j]:
                board[pos][j] = 'Q'
                self._recursive_helper(res, board, num - 1)
                board[pos][j] = '.'

