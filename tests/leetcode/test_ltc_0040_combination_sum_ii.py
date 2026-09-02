from app.leetcode.ltc_0040_combination_sum_ii import CombinationSumII

class TestCombinationSumII:
    def test_solution(self):
        combination_sum_ii = CombinationSumII()
        assert combination_sum_ii.solution([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
        assert combination_sum_ii.solution([2], 1) == []
        assert combination_sum_ii.solution([1], 1) == [[1]]
        assert combination_sum_ii.solution([1], 2) == []