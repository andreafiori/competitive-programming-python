from app.leetcode.ltc_0051_n_queens import NQueens

class TestNQueens:
    def test_solve_n_queens(self):
        nq = NQueens()
        assert nq.solve_n_queens(4) == [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
        assert nq.solve_n_queens(1) == [["Q"]]
        assert nq.solve_n_queens(0) == 0
