"""
Gray Code | https://leetcode.com/problems/gray-code/

"""

class GrayCode:
    def solution(self, n: int) -> list[int]:
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            for j in reversed(range(len(res))):
                res.append(res[j] + (1 << i))
        return res
