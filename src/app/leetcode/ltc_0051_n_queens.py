"""
N queens | leetcode 51 | Hard | https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9

"""

class NQueens:

    def solve_n_queens(self, n: int):
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
