import pytest

from app.leetcode.ltc_0258_add_digits import AddDigits
class TestAddDigits:

    @pytest.mark.parametrize("num, expected", [
        (38, 2),
        (0, 0),
        (9, 9),
        (10, 1),
        (11, 2),
        (99, 9),
        (12345, 6)
    ])

    def test_add_digits_parametrized(self, num, expected):
        assert AddDigits().solution(num) == expected
