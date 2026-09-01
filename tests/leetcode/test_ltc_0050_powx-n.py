from app.leetcode.ltc_0050_powx_n import PowXN

class TestPowXN:
    def test_my_pow(self):
        pow_x_n = PowXN()
        assert pow_x_n.my_pow(2.0, 10) == 1024.0
        assert pow_x_n.my_pow(2.1, 3) == 9.261000000000001
        assert pow_x_n.my_pow(2.0, -2) == 0.25
        assert pow_x_n.my_pow(2.0, 0) == 1.0