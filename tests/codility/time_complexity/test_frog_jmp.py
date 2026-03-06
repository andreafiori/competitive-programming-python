from app.codility.time_complexity.frog_jmp import FrogJmp

class TestFrogJmp:

    def setup_class(self):
        self.frog_jmp = FrogJmp()

    def test_example1(self):
        assert self.frog_jmp.solution(10, 85, 30) == 3

    def test_one(self):
        assert self.frog_jmp.solution(0, 10, 1) == 10

    def test_big_steps(self):
        assert self.frog_jmp.solution(0, 10, 20) == 1

    def test_even_steps(self):
        assert self.frog_jmp.solution(10, 100, 10) == 9

    def test_equal_steps(self):
        assert self.frog_jmp.solution(10, 10, 10) == 0

    def test_odd_steps(self):
        assert self.frog_jmp.solution(9, 29, 10) == 2
