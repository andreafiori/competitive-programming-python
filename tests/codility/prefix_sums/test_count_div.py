import pytest

from app.codility.prefix_sums.count_div import CountDiv

@pytest.fixture
def count_div():
    return CountDiv()

class TestCountDiv:
    def test_count_div(self, count_div):
        assert count_div.solution(6, 11, 2) == 3
        assert count_div.solution(0, 0, 11) == 1
        assert count_div.solution(10, 10, 5) == 1
        assert count_div.solution(10, 10, 7) == 0
        assert count_div.solution(10, 10, 20) == 0
        assert count_div.solution(10, 10, 1) == 1
        assert count_div.solution(10, 10, 2) == 1
        assert count_div.solution(10, 10, 3) == 0
        assert count_div.solution(10, 10, 4) == 0
        assert count_div.solution(10, 10, 5) == 1
        assert count_div.solution(10, 10, 6) == 0
        assert count_div.solution(10, 10, 7) == 0
        assert count_div.solution(10, 10, 8) == 0
        assert count_div.solution(10, 10, 9) == 0
        assert count_div.solution(10, 10, 10) == 1
