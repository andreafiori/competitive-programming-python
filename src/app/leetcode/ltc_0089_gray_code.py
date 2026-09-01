"""
Gray Code | LeetCode 89 | https://leetcode.com/problems/gray-code/
"""

class GrayCode:
    def solution(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            for j in reversed(range(len(res))):
                res.append(res[j] + (1 << i))
        return res

    def solution_two(self, num):
        count = 0
        while num:
            num &= (num - 1)
            count += 1
        return count
