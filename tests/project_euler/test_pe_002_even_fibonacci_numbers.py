from app.project_euler.pe_002_fibonacci import EvenFibonacciNumbers

class TestEvenFibonacciNumbers:

    def test_solution_one(self):
        assert EvenFibonacciNumbers(10).solution_one() == 10
        assert EvenFibonacciNumbers(1).solution_one() == 0
        assert EvenFibonacciNumbers(0).solution_one() == 0
