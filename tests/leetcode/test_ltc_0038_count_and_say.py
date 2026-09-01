from app.leetcode.ltc_0038_count_and_say import CountAndSay

class TestCountAndSay:
    def test_solution(self):
        count_and_say = CountAndSay()
        assert count_and_say.solution(1) == '1'
        assert count_and_say.solution(2) == '11'
        assert count_and_say.solution(3) == '21'
        assert count_and_say.solution(4) == '1211'
        assert count_and_say.solution(5) == '111221'
        assert count_and_say.solution(6) == '312211'
        assert count_and_say.solution(7) == '13112221'
        assert count_and_say.solution(8) == '1113213211'
        assert count_and_say.solution(9) == '31131211131221'
        assert count_and_say.solution(10) == '13211311123113112211'