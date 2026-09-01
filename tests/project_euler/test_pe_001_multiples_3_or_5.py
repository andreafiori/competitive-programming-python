from app.project_euler.pe_001_multiples_of_3_and_5 import MultiplesOf3And5

class TestMultiplesOf3And5:

    def test_solution_1(self):
        assert MultiplesOf3And5(3).solution_1() == 0
        assert MultiplesOf3And5(4).solution_1() == 3
        assert MultiplesOf3And5(10).solution_1() == 23
        assert MultiplesOf3And5(600).solution_1() == 83700
        assert MultiplesOf3And5(-7).solution_1() == 0
