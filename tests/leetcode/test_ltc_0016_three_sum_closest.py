from app.leetcode.ltc_0016_three_sum_closest import ThreeSumClosest

class TestThreeSumClosest:
    def test_find(self):
        tsc = ThreeSumClosest()
        assert tsc.find([-1, 2, 1, -4], 1) == 2
        assert tsc.find([0, 0, 0], 1) == 0
        assert tsc.find([1, 1, 1, 0], -100) == 2
        assert tsc.find([-3, -2, -5, 3, -4], -1) == -2