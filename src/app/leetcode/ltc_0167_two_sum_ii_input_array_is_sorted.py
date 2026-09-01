"""
Leetcode 167. Two Sum II - Input Array Is Sorted | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class TwoSumII:

    def solution(self, numbers: list[int], target: int) -> list[int]:
        """
        :param numbers: List[int]
        :param target: int
        :return: List[int]
        """
        # Two Points
        begin, end = 0, len(numbers) - 1
        while begin < end:
            curr = numbers[begin] + numbers[end]
            if curr == target:
                return [begin + 1, end + 1]
            elif curr < target:
                begin += 1
            else:
                end -= 1
