from app.leetcode.ltc_0005_longest_palindromic_substring import LongestPalindromicSubstring

class TestLongestPalindromicSubstring:
    def test_solution(self):
        lps = LongestPalindromicSubstring()
        assert lps.solution("babad", 0, 0) == 1
        assert lps.solution("babad", 1, 1) == 3
        assert lps.solution("babad", 2, 2) == 3
        assert lps.solution("babad", 3, 3) == 1
        assert lps.solution("babad", 4, 4) == 1
        assert lps.solution("cbbd", 0, 0) == 1
