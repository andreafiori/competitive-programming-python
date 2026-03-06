from app.leetcode.ltc_0258_add_digits import AddDigits

class TestAddDigits:

    def setup_class(self):
        self.add_digits = AddDigits()

    def test_add_digits(self):
        assert self.add_digits.add(38) == 2
