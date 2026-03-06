from app.leetcode.ltc_0954_array_of_doubled_pairs import ArrayOfDoubledPairs

class TestArrayOfDoubledPairs:

    def setup_class(self):
        self.array_doubled_pairs = ArrayOfDoubledPairs()

    def test_can_reorder_doubled_false_case1(self):
        assert not self.array_doubled_pairs.can_reorder_doubled([3, 1, 3, 6])

    def test_can_reorder_doubled_false_case2(self):
        assert not self.array_doubled_pairs.can_reorder_doubled([2, 1, 2, 6])

    def test_can_reorder_doubled_false_case3(self):
        assert not self.array_doubled_pairs.can_reorder_doubled([1, 2, 4, 16, 8, 4])

    def test_can_reorder_doubled_true_case(self):
        assert self.array_doubled_pairs.can_reorder_doubled([4, -2, 2, -4])
