import random

from app.codility.sorting.distinct import Distinct

class TestDistinct:
    def setup_class(self):
        self.distinct_instance = Distinct()
        self.RANGE_A = (-1000000, 1000000)
        self.RANGE_N = (0, 100000)

    def test_solution_is_three(self):
        x = [2, 1, 1, 2, 3, 1]
        assert self.distinct_instance.solution(x) == 3

    def test_simple(self):
        assert self.distinct_instance.solution([0, 1, 2, 3, 4]) == 5

    def test_edges(self):
        assert self.distinct_instance.solution([]) == 0
        assert self.distinct_instance.solution([0]) == 1
        assert self.distinct_instance.solution([1]) == 1
        assert self.distinct_instance.solution([0, 1]) == 2
        assert self.distinct_instance.solution([-1, 1]) == 2
        assert self.distinct_instance.solution([self.RANGE_A[0], self.RANGE_A[1]]) == 2

    def test_medium(self):
        assert self.distinct_instance.solution([1] * 500) == 1
        assert self.distinct_instance.solution([x for x in range(-250, 250)]) == 500
        assert self.distinct_instance.solution([x for x in range(-500, 500, 2)]) == 500
        assert self.distinct_instance.solution([x for x in range(-500, 500, 2)] * 2) == 500

    def test_random(self):
        A = [random.randint(*self.RANGE_A) for _ in range(*self.RANGE_N)]

    def test_extreme(self):
        A = [x for x in range(*self.RANGE_N)]
        assert self.distinct_instance.solution(A) == self.RANGE_N[1]
