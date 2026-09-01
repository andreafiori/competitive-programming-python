from app.leetcode.ltc_0032_longest_valid_parentheses import LongestValidParentheses

class TestLongestValidParentheses:
    def test_solution(self):
        longest_valid_parentheses = LongestValidParentheses()
        assert longest_valid_parentheses.solution("(()") == 2
        assert longest_valid_parentheses.solution(")()())") == 4
        assert longest_valid_parentheses.solution("") == 0
        assert longest_valid_parentheses.solution("()(()") == 2
        assert longest_valid_parentheses.solution("()()") == 4
        assert longest_valid_parentheses.solution("((()))") == 6