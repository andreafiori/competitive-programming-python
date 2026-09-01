from app.leetcode.ltc_0018_four_sum import FourSum

class TestFourSum:
    def test_solution(self):
        four_sum = FourSum()
        assert sorted(four_sum.solution([1, 0, -1, 0, -2, 2], 0)) == sorted([(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)])
        assert sorted(four_sum.solution([2, 2, 2, 2, 2], 8)) == sorted([(2, 2, 2, 2)])