import pytest

from app.project_euler.pe_004_largest_palindrome_product import LargestPalindromeProduct

class TestLargestPalindromeProduct:
    @pytest.mark.parametrize(
        "input_value, expected_output",
        [
            (998001, 906609),
            (800000, 793397),
        ],
    )
    def test_largest_palindrome_product(self, input_value, expected_output):
        assert LargestPalindromeProduct(input_value).solution() == expected_output
