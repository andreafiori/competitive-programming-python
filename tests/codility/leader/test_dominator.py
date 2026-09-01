from app.codility.leader.dominator import Dominator

class TestDominator:
    def test_example_case(self):
        dominator = Dominator()
        A = [3, 4, 3, 2, 3, -1, 3, 3]
        result = dominator.solution_copilot(A)
        assert result in [0, 2, 4, 6, 7]

    def test_no_dominator(self):
        dominator = Dominator()
        A = [1, 2, 3, 4]
        result = dominator.solution_copilot(A)
        assert result == -1

    def test_empty_array(self):
        dominator = Dominator()
        A = []
        result = dominator.solution_copilot(A)
        assert result == -1

    def test_single_element(self):
        dominator = Dominator()
        A = [42]
        result = dominator.solution_copilot(A)
        assert result == 0