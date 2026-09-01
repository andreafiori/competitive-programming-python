import pytest

from app.project_euler.pe_003_largest_prime_factor import LargestPrimeFactor

class TestLargestPrimeFactor:
    @pytest.mark.parametrize(
        "input_value, expected_output",
        [
            (13195, 29),
            (10, 5),
            (17, 17),
            (3.4, 3),
        ],
    )
    def test_solution_one_with_valid_inputs(self, input_value, expected_output):
        assert LargestPrimeFactor(input_value).solution_one() == expected_output

    @pytest.mark.parametrize(
        "input_value, expected_exception",
        [
            (0, ValueError),
            (-17, ValueError),
            ([], TypeError),
            ("asd", TypeError),
        ],
    )
    def test_solution_one_with_invalid_inputs(self, input_value, expected_exception):
        lpf = LargestPrimeFactor(input_value)
        with pytest.raises(expected_exception):
            lpf.solution_one()