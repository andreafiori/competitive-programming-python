from app.leetcode.ltc_0027_remove_element import RemoveElement

class TestRemoveElement:
    def test_remove_element(self):
        remover = RemoveElement()
        nums = [3, 2, 2, 3]
        val = 3
        k = remover.solution(nums, val)
        assert k == 2
        assert nums[:k] == [2, 2]