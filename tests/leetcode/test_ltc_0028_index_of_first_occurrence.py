from app.leetcode.ltc_0028_index_of_first_occurrence import IndexOfFirstOccurrence

class TestIndexOfFirstOccurrence:
    haystack = "hello"
    needle = "ll"

    def test_str_str(self):
        index_of_first_occurrence = IndexOfFirstOccurrence()
        assert index_of_first_occurrence.str_str(self.haystack, self.needle) == 2
