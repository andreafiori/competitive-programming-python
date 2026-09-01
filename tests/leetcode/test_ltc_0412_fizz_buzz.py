
import pytest

from app.leetcode.ltc_0412_fizz_buzz import FizzBuzz

@pytest.fixture
def fizz_buzz():
    return FizzBuzz()

class TestFizzBuzz:
    def test_solution(self, fizz_buzz):
        assert fizz_buzz.solution_one(3) == ["1", "2", "Fizz"]
        assert fizz_buzz.solution_two(3) == ["1", "2", "Fizz"]
        assert fizz_buzz.solution_three(3) == ["1", "2", "Fizz"]