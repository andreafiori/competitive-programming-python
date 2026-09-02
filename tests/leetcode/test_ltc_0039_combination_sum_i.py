from app.leetcode.ltc_0039_combination_sum import CombinationSum

class TestCombinationSum:
    def test_solution(self):
        combination_sum = CombinationSum()
        assert combination_sum.solution([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
        assert combination_sum.solution([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        assert combination_sum.solution([2], 1) == []
        assert combination_sum.solution([1], 1) == [[1]]
        assert combination_sum.solution([1], 2) == [[1, 1]]