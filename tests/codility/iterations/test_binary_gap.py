import pytest

from app.codility.iterations.binary_gap import BinaryGap


@pytest.fixture
def binary_gap():
    """Provide a fresh BinaryGap instance."""
    return BinaryGap()

class TestBinaryGap:

    def test_example1(self, binary_gap):
        assert binary_gap.solution_one(1041) == 5
        assert binary_gap.solution_two(1041) == 5

    def test_example2(self, binary_gap):
        assert binary_gap.solution_one(15) == 0
        assert binary_gap.solution_two(15) == 0

    def test_extremes(self, binary_gap):
        assert binary_gap.solution_one(1) == 0
        assert binary_gap.solution_one(5) == 1
        assert binary_gap.solution_one(binary_gap.MAXINT)  == 0

    def test_trailing_zeros(self, binary_gap):
        assert binary_gap.solution_one(6) == 0
        assert binary_gap.solution_one(328) == 2

    def test_simple1(self, binary_gap):
        assert binary_gap.solution_one(9) == 2
        assert binary_gap.solution_one(11) == 1

    def test_simple2(self, binary_gap):
        assert binary_gap.solution_one(19) == 2
        assert binary_gap.solution_one(42) == 1

    def test_simple3(self, binary_gap):
        assert binary_gap.solution_one(1162) == 3
        assert binary_gap.solution_one(5) == 1

    def test_medium1(self, binary_gap):
        assert binary_gap.solution_one(51712) == 2
        assert binary_gap.solution_one(20) == 1

    def test_medium2(self, binary_gap):
        assert binary_gap.solution_one(561892) == 3
        assert binary_gap.solution_one(9) == 2

    def test_medium3(self, binary_gap):
        assert binary_gap.solution_one(66561) == 9

    def test_large1(self, binary_gap):
        assert binary_gap.solution_one(6291457) == 20

    def test_large2(self, binary_gap):
        assert binary_gap.solution_one(74901729) == 4

    def test_large3(self, binary_gap):
        assert binary_gap.solution_one(805306369) == 27

    def test_large4(self, binary_gap):
        assert binary_gap.solution_one(1376796946) == 5

    def test_large5(self, binary_gap):
        assert binary_gap.solution_one(1073741825) == 29

    def test_large6(self, binary_gap):
        assert binary_gap.solution_one(1610612737) == 28

    def test_non_int(self, binary_gap):
        with pytest.raises(TypeError):
            binary_gap.solution_one(1.0)

    def test_zero(self, binary_gap):
        with pytest.raises(ValueError):
            binary_gap.solution_one(0)

    def test_maxint_plus_one(self, binary_gap):
        with pytest.raises(ValueError):
            binary_gap.solution_one(2147483648)
