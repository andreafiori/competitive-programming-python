from app.leetcode.ltc_0014_longest_common_prefix import LongestCommonPrefix

class TestLongestCommonPrefix:
    def test_find(self):
        lcp = LongestCommonPrefix()
        assert lcp.find(["flower","flow","flight"]) == "fl"
        assert lcp.find(["dog","racecar","car"]) == ""
        assert lcp.find([""]) == ""
        assert lcp.find(["a"]) == "a"
        assert lcp.find(["ab", "a"]) == "a"
        assert lcp.find(["ab", "ac"]) == "a"