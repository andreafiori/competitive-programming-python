"""
How Many Numbers Are Smaller Than the Current Number | leetcode 1365 | https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

"""

class HowManyNumbersAreSmallerThanTheCurrentNumber:

    def solution(self, nums: list[int]) -> list[int]:
        count_list = [0] * 101
        # count math
        for v in nums:
            count_list[v] += 1
        # compute math before current index
        for i in range(1, 101):
            count_list[i] += count_list[i-1]
        res = []
        for v in nums:
            if v == 0:
                res.append(0)
            else:
                res.append(count_list[v-1])
        return res
