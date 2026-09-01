from app.leetcode.ltc_0017_letter_combinations_of_a_phone_number import LetterCombinations

class TestLetterCombinations:
    def test_solution(self):
        lc = LetterCombinations()
        assert lc.solution("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        assert lc.solution("2") == ["a","b","c"]
        assert lc.solution("") == []