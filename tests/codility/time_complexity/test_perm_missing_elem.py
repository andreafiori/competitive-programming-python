
import random

from app.codility.time_complexity.perm_missing_elem import PerMissElem

class TestPerMissElem:

    def setup_class(self):
        self.perm_missing_elem = PerMissElem()
        self.INT_RANGE = (0, 100000)

    def test_example1(self):
        assert self.perm_missing_elem.solution([2,3,1,5]) == 4

    def test_single(self):
        assert self.perm_missing_elem.solution([2]) == 1
        assert self.perm_missing_elem.solution([1]) == 2

    def test_random(self):
        arr = [n for n in range(1, random.randint(*self.INT_RANGE))]
        missing =  random.randint(0, len(arr))
        arr.remove(missing)

        assert self.perm_missing_elem.solution(arr) == missing

    def test_maximum(self):
        arr = [n for n in range(1, self.INT_RANGE[1]+1)]
        arr.pop()
        assert self.perm_missing_elem.solution(arr) == self.INT_RANGE[1]
