
import pytest

from app.leetcode.ltc_0412_fizz_buzz import FizzBuzz

@pytest.fixture
def fizz_buzz():
    return FizzBuzz()

class TestFizzBuzz:
    @pytest.mark.parametrize("n, expected", [
        (1, ["1"]),
        (2, ["1", "2"]),
        (3, ["1", "2", "Fizz"]),
        (4, ["1", "2", "Fizz", "4"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (6, ["1", "2", "Fizz", "4", "Buzz", "Fizz"]),
        (7, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]),
        (8, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8"]),
        (9, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz"]),
        (10, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]),
    ])
    def test_solution(self, fizz_buzz, n, expected):
        assert fizz_buzz.solution_one(n) == expected
        assert fizz_buzz.solution_two(n) == expected
        assert fizz_buzz.solution_three(n) == expected
