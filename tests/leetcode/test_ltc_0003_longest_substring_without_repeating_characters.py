from app.leetcode.ltc_0003_longest_substring_without_repeating_characters import LongestSubstringWithoutRepeatingCharacters

class TestLongestSubstringWithoutRepeatingCharacters:
    def test_solution_one(self):
        ltc = LongestSubstringWithoutRepeatingCharacters()
        assert ltc.solution_one("abcabcbb") == 3
        assert ltc.solution_one("bbbbb") == 1
        assert ltc.solution_one("pwwkew") == 3
        assert ltc.solution_one("") == 0
        assert ltc.solution_one(" ") == 1
        assert ltc.solution_one("au") == 2
        assert ltc.solution_one("dvdf") == 3

    def test_solution_two(self):
        ltc = LongestSubstringWithoutRepeatingCharacters()
        assert ltc.solution_two("abcabcbb") == 3
        assert ltc.solution_two("bbbbb") == 1
        assert ltc.solution_two("pwwkew") == 3
        assert ltc.solution_two("") == 0
        assert ltc.solution_two(" ") == 1
        assert ltc.solution_two("au") == 2
        assert ltc.solution_two("dvdf") == 3