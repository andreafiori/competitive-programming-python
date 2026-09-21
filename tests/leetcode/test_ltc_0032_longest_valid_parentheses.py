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

    def test_solution_with_stack(self):
        longest_valid_parentheses = LongestValidParentheses()
        assert longest_valid_parentheses.solution_with_stack("(()") == 2
        assert longest_valid_parentheses.solution_with_stack(")()())") == 4
        assert longest_valid_parentheses.solution_with_stack("") == 0
        assert longest_valid_parentheses.solution_with_stack("()(()") == 2
        assert longest_valid_parentheses.solution_with_stack("()()") == 4
        assert longest_valid_parentheses.solution_with_stack("((()))") == 6

    def test_solution_with_two_passes(self):
        longest_valid_parentheses = LongestValidParentheses()
        assert longest_valid_parentheses.solution_with_two_passes("(()") == 2
        assert longest_valid_parentheses.solution_with_two_passes(")()())") == 4
        assert longest_valid_parentheses.solution_with_two_passes("") == 0
        assert longest_valid_parentheses.solution_with_two_passes("()(()") == 2
        assert longest_valid_parentheses.solution_with_two_passes("()()") == 4
        assert longest_valid_parentheses.solution_with_two_passes("((()))") == 6