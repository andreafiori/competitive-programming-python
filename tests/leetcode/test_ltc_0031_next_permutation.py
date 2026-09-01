from app.leetcode.ltc_0031_next_permutation import NextPermutation

class TestNextPermutation:
    def test_solution(self):
        next_permutation = NextPermutation()
        nums = [1, 2, 3]
        next_permutation.solution(nums)
        assert nums == [1, 3, 2]

        nums = [3, 2, 1]
        next_permutation.solution(nums)
        assert nums == [1, 2, 3]

        nums = [1, 1, 5]
        next_permutation.solution(nums)
        assert nums == [1, 5, 1]

        nums = [1]
        next_permutation.solution(nums)
        assert nums == [1]

        nums = [1, 3, 2]
        next_permutation.solution(nums)
        assert nums == [2, 1, 3]