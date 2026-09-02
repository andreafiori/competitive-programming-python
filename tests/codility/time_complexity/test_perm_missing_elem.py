import random
import pytest
from app.codility.time_complexity.perm_missing_elem import PermMissingElem


@pytest.fixture
def perm_missing_elem():
    return PermMissingElem()


class TestPermMissingElem:
    INT_RANGE = (0, 100000)

    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([2, 3, 1, 5], 4),
            ([1], 2),
            ([2], 1),
        ],
    )
    def test_solution_cases(self, perm_missing_elem, arr, expected):
        assert perm_missing_elem.solution(arr) == expected

    def test_random(self, perm_missing_elem):
        arr = list(range(1, random.randint(*self.INT_RANGE)))
        missing = random.randint(0, len(arr))
        if missing != 0:
            arr.remove(missing)

        assert perm_missing_elem.solution(arr) == missing

    def test_maximum(self, perm_missing_elem):
        arr = list(range(1, self.INT_RANGE[1] + 1))
        arr.pop()
        assert perm_missing_elem.solution(arr) == self.INT_RANGE[1]