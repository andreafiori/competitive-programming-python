from app.leetcode.ltc_0022_generate_parentheses import GenerateParentheses

class TestGenerateParentheses:
    def test_generate_parentheses(self):
        generator = GenerateParentheses()

        assert sorted(generator.generate(1)) == ['()']
        assert sorted(generator.generate(2)) == ['(())', '()()']
        assert sorted(generator.generate(3)) == ['((()))', '(()())', '(())()', '()(())', '()()()']
        assert sorted(generator.generate(4)) == [
            '(((())))',
            '((()()))',
            '((())())',
            '((()))()',
            '(()(()))',
            '(()()())',
            '(()())()',
            '(())(())',
            '(())()()',
            '()((()))',
            '()(()())',
            '()(())()',
            '()()(())',
            '()()()()'
        ]