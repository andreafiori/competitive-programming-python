from app.leetcode.ltc_0042_trapping_rain_water import TrappingRainWater

class TestTrappingRainWater:
    def test_solution(self):
        trw = TrappingRainWater()
        assert trw.solution([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
        assert trw.solution([4,2,0,3,2,5]) == 9
        assert trw.solution([0]) == 0
        assert trw.solution([1]) == 0
        assert trw.solution([1, 2]) == 0
        assert trw.solution([2, 1]) == 0
        assert trw.solution([3, 0, 2]) == 2
        assert trw.solution([3, 0, 2, 0]) == 2
        assert trw.solution([3, 0, 2, 0, 4]) == 7