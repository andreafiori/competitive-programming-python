from app.leetcode.ltc_0012_integer_to_roman import IntegerToRoman

class TestIntegerToRoman:

    def test_solution(self):
        converter = IntegerToRoman()
        assert converter.solution(3749) == "MMMDCCXLIX"
        assert converter.solution(58) == "LVIII"
        assert converter.solution(1994) == "MCMXCIV"
        assert converter.solution(1) == "I"
        assert converter.solution(3999) == "MMMCMXCIX"