import pytest

from app.codility.prefix_sums.count_div import CountDiv


@pytest.fixture
def count_div():
    return CountDiv()


class TestCountDiv:
    def test_every_divisible_value_within_range(self, count_div):
        assert count_div.solution(6, 11, 2) == 3
        assert count_div.solution(10, 10, 5) == 1
        assert count_div.solution(10, 15, 5) == 2
        assert count_div.solution(0, 0, 11) == 1

    def test_non_divisible_ranges(self, count_div):
        assert count_div.solution(1, 5, 7) == 0
        assert count_div.solution(17, 19, 10) == 0

    def test_edge_case_when_a_is_divisible_by_k(self, count_div):
        assert count_div.solution(5, 12, 5) == 2

    def test_edge_case_when_a_is_not_divisible_by_k(self, count_div):
        assert count_div.solution(5, 13, 5) == 2
