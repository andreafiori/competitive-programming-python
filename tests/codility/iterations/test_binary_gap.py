import pytest

from app.codility.iterations.binary_gap import BinaryGap


@pytest.fixture
def binary_gap():
    return BinaryGap()


class TestBinaryGap:

    @pytest.mark.parametrize("method_name", ["solution_one", "solution_two"])
    def test_binary_gap_examples(self, binary_gap, method_name):
        solution = getattr(binary_gap, method_name)

        assert solution(1041) == 5
        assert solution(15) == 0
        assert solution(1) == 0
        assert solution(5) == 1
        assert solution(6) == 0
        assert solution(328) == 2
        assert solution(9) == 2
        assert solution(11) == 1
        assert solution(19) == 2
        assert solution(42) == 1

    @pytest.mark.parametrize(
        "method_name,value,expected",
        [
            ("solution_one", 1162, 3),
            ("solution_two", 1162, 3),
            ("solution_two", 51712, 2),
            ("solution_two", 561892, 3),
            ("solution_two", 66561, 9),
            ("solution_two", 6291457, 20),
            ("solution_two", 74901729, 4),
            ("solution_two", 805306369, 27),
            ("solution_two", 1376796946, 5),
            ("solution_two", 1073741825, 29),
            ("solution_two", 1610612737, 28),
        ],
    )
    def test_binary_gap_large_values(self, binary_gap, method_name, value, expected):
        solution = getattr(binary_gap, method_name)

        assert solution(value) == expected

    def test_solution_one_rejects_invalid_inputs(self, binary_gap):
        with pytest.raises(TypeError):
            binary_gap.solution_one(1.0)

        with pytest.raises(ValueError):
            binary_gap.solution_one(0)

        with pytest.raises(ValueError):
            binary_gap.solution_one(binary_gap.MAXINT + 1)

    def test_solution_two_raises_type_error_for_non_int(self, binary_gap):
        with pytest.raises(TypeError):
            binary_gap.solution_two(1.0)
