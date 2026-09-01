from app.codility.prefix_sums.min_avg_two_slice import MinAvgTwoSlice

class MinAvgTwoSliceTest:

    def test_solution(self):
        mat = MinAvgTwoSlice()
        A = [4, 2, 2, 5, 1, 5, 8]
        assert mat.solution(A) == 1
