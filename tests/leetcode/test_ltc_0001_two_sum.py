import pytest

from app.leetcode.ltc_0001_two_sum import TwoSum

@pytest.fixture
def two_sum():
    """Provide a fresh TwoSum instance for each test."""
    return TwoSum()

class TestTwoSum:
    def test_solution(self, two_sum):
        assert two_sum.solution([2, 7, 11, 15], 9) == [0, 1]
