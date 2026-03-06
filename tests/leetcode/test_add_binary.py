from app.leetcode.ltc_0067_add_binary import AddBinary

class TestAddBinary:
    def setup_class(self):
        self.add_binary = AddBinary()

    def test_solution(self):
        assert self.add_binary.solution_one("11", "1") == "100"
