from app.leetcode.ltc_0041_first_missing_positive import FirstMissingPositive

class TestFirstMissingPositive:
    def test_solution(self):
        first_missing_positive = FirstMissingPositive()
        assert first_missing_positive.solution([1, 2, 0]) == 3
        assert first_missing_positive.solution([3, 4, -1, 1]) == 2
        assert first_missing_positive.solution([7, 8, 9, 11, 12]) == 1
        assert first_missing_positive.solution([1]) == 2
        assert first_missing_positive.solution([2]) == 1
        assert first_missing_positive.solution([-1]) == 1
        assert first_missing_positive.solution([-1, -2]) == 1
        assert first_missing_positive.solution([-1, -2, -3]) == 1
        assert first_missing_positive.solution([-1, -2, -3, -4]) == 1
        assert first_missing_positive.solution([-1, -2, -3, -4, -5]) == 1