from app.leetcode.ltc_0028_index_of_first_occurrence import IndexOfFirstOccurrence

class TestIndexOfFirstOccurrence:

    def test_str_str(self):
        haystack = "hello"
        needle = "ll"
        index_of_first_occurrence = IndexOfFirstOccurrence()
        assert index_of_first_occurrence.str_str(haystack, needle) == 2

    def test_str_str_not_found(self):
        haystack = "aaaaa"
        needle = "bba"
        index_of_first_occurrence = IndexOfFirstOccurrence()
        assert index_of_first_occurrence.str_str(haystack, needle) == -1
