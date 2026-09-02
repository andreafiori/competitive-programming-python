
from app.leetcode.ltc_0415_add_strings import AddStrings

class TestAddStrings:
    def test_solution(self):
        add_string = AddStrings()
        assert add_string.solution("11", "123") == "134"
        assert add_string.solution("456", "77") == "533"
        assert add_string.solution("0", "0") == "0"
