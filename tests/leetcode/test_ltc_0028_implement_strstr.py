
import pytest

from app.leetcode.ltc_0028_implement_strstr import ImplementStrStr

@pytest.fixture
def implement_str_str():
    return ImplementStrStr()

class TestImplementStrStr:
    haystack = "hello"
    needle = "ll"

    def test_solution_one(self, implement_str_str):
        assert implement_str_str.solution_one(self.haystack, self.needle) == 2

    def test_solution_two(self, implement_str_str):
        assert implement_str_str.solution_two(self.haystack, self.needle) == 2
