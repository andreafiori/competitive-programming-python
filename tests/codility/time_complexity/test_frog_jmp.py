import pytest
from app.codility.time_complexity.frog_jmp import FrogJmp

@pytest.fixture
def frog_jmp():
    return FrogJmp()

@pytest.mark.parametrize(
    "start, end, jump, expected",
    [
        (10, 85, 30, 3),
        (0, 10, 1, 10),
        (0, 10, 20, 1),
        (10, 100, 10, 9),
        (10, 10, 10, 0),
        (9, 29, 10, 2),
    ],
)
def test_frog_jmp_solution(frog_jmp, start, end, jump, expected):
    assert frog_jmp.solution(start, end, jump) == expected