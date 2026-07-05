import pytest

from app.codility.leader.dominator import Dominator

@pytest.fixture
def dominator():
    return Dominator()

class TestDominator:
    def test_solution_copilot_returns_valid_index(self, dominator):
        values = [3, 4, 3, 2, 3, -1, 3, 3]
        result = dominator.solution_copilot(values)

        assert result in {0, 2, 4, 6, 7}
        assert values[result] == 3

    def test_solution_one_returns_valid_index(self, dominator):
        values = [3, 3, 4, 3, 2, 3, 3]
        result = dominator.solution_one(values)

        assert result != -1
        assert values[result] == 3

    def test_returns_minus_one_when_no_dominator(self, dominator):
        values = [1, 2, 3, 4, 5, 6]

        assert dominator.solution_copilot(values) == -1
        assert dominator.solution_one(values) == -1

    def test_single_element_returns_zero(self, dominator):
        assert dominator.solution_copilot([42]) == 0
        assert dominator.solution_one([42]) == 0
