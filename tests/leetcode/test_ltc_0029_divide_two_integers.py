from app.leetcode.ltc_0029_divide_two_integers import DivideTwoIntegers

class TestDivideTwoIntegers:
    def test_divide(self):
        divide_two_integers = DivideTwoIntegers()
        assert divide_two_integers.divide(10, 3) == 3
        assert divide_two_integers.divide(7, -3) == -2
        assert divide_two_integers.divide(-2147483648, -1) == 2147483647