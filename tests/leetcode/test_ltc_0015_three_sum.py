from app.leetcode.ltc_0015_three_sum import ThreeSum

class TestThreeSum:
    def test_solution_one(self):
        ts = ThreeSum()
        assert ts.solution_one([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
        assert ts.solution_one([0, 0, 0]) == [[0, 0, 0]]
        assert ts.solution_one([0]) == []