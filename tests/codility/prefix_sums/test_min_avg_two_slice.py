from app.codility.prefix_sums.min_avg_two_slice import MinAvgTwoSlice

class MinAvgTwoSliceTest:
    def test_solution(self):
        min_avg_two_slice = MinAvgTwoSlice()
        assert min_avg_two_slice.solution([4, 2, 2, 5, 1, 5, 8]) == 1
        assert min_avg_two_slice.solution([1, 2]) == 0
        assert min_avg_two_slice.solution([1, 2, 3]) == 0
        assert min_avg_two_slice.solution([3, 2, 1]) == 1
        assert min_avg_two_slice.solution([1, 1, 1]) == 0
        assert min_avg_two_slice.solution([1, 2, 3, 4]) == 0
        assert min_avg_two_slice.solution([4, 3, 2, 1]) == 2
        assert min_avg_two_slice.solution([1, 2, -3, -4]) == 2