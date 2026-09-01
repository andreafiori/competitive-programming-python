import pytest

from app.codility.iterations.binary_gap import BinaryGap

@pytest.fixture
def binary_gap():
    """Provide a fresh BinaryGap instance."""
    return BinaryGap()

class TestBinaryGap:

    @pytest.mark.parametrize(
        "number,expected",
        [
            (1041, 5),
            (15, 0),
        ],
    )
    def test_solutions_parity(self, binary_gap, number, expected):
        assert binary_gap.solution_one(number) == expected
        assert binary_gap.solution_two(number) == expected

    @pytest.mark.parametrize(
        "number,expected",
        [
            (1, 0),
            (5, 1),
            (6, 0),
            (328, 2),
            (9, 2),
            (11, 1),
            (19, 2),
            (42, 1),
            (1162, 3),
            (51712, 2),
            (20, 1),
            (561892, 3),
            (66561, 9),
            (6291457, 20),
            (74901729, 4),
            (805306369, 27),
            (1376796946, 5),
            (1073741825, 29),
            (1610612737, 28),
        ],
    )
    def test_solution_one_values(self, binary_gap, number, expected):
        assert binary_gap.solution_one(number) == expected

    def test_maxint_constant(self, binary_gap):
        assert binary_gap.solution_one(binary_gap.MAXINT) == 0

    @pytest.mark.parametrize(
        "invalid_input,exception",
        [
            (1.0, TypeError),
            (0, ValueError),
            (2147483648, ValueError),
        ],
    )
    def test_invalid_inputs(self, binary_gap, invalid_input, exception):
        with pytest.raises(exception):
            binary_gap.solution_one(invalid_input)