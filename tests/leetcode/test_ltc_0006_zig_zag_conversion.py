from app.leetcode.ltc_0006_zig_zag_conversion import ZigZagConversion

class TestZigZagConversion:
    def test_convert(self):
        zzc = ZigZagConversion()
        assert zzc.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
        assert zzc.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
        assert zzc.convert("A", 1) == "A"
        assert zzc.convert("ABCD", 2) == "ACBD"
        assert zzc.convert("ABCDE", 4) == "ABCED"
