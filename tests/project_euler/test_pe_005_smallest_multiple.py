from app.project_euler.pe_005_smallest_multiple import SmallestMultiple

class TestSmallestMultiple:
    def test_solution_one(self):
        assert SmallestMultiple(10).solution_one() == 2520
        assert SmallestMultiple(20).solution_one() == 232792560
    def test_solution_two(self):
        assert SmallestMultiple(10).solution_two() == 2520
        assert SmallestMultiple(20).solution_two() == 232792560
