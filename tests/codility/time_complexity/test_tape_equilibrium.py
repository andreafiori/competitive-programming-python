from app.codility.time_complexity.tape_equilibrium import TapeEquilibrium

class TestTapeEquilibrium:

    def setup_class(self):
        self.tape_equilibrium = TapeEquilibrium()
        self.N_RANGE = (2, 100000)
        self.ELEMENT_RANGE = (-1000, 1000)

    def test_example1(self):
        assert self.tape_equilibrium.solution([3, 1, 2, 4, 3]) == 1

    def test_simple(self):
        assert self.tape_equilibrium.solution([1,2]) == 1

    def test_double(self):
        assert self.tape_equilibrium.solution([-1000, 1000]) == 2000

    # def test_random(self, tape_equilibrium):
    #     N = random.randint(*self.N_RANGE)
    #     arr = [random.randint(*self.ELEMENT_RANGE) for _ in range(N)]

    # def test_maximum(self, tape_equilibrium):
    #     arr = [random.randint(*TapeEquilibrium.ELEMENT_RANGE) for _ in range(100000)]
