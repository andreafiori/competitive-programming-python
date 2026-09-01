from app.leetcode.ltc_0004_median_of_two_sorted_arrays import MedianOfTwoSortedArray

class TestMedianOfTwoSortedArray:

    def test_solution(self):
        median_of_two_sorted_array = MedianOfTwoSortedArray()
        assert median_of_two_sorted_array.solution([1, 3], [2]) == 2.0
        assert median_of_two_sorted_array.solution([1, 2], [3, 4]) == 2.5
        assert median_of_two_sorted_array.solution([0, 0], [0, 0]) == 0.0
        assert median_of_two_sorted_array.solution([], [1]) == 1.0
        assert median_of_two_sorted_array.solution([2], []) == 2.0