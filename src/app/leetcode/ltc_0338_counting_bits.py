"""
Counting Bits | Leetcode 338 | Medium | https://leetcode.com/problems/counting-bits/
"""

class CountingBits:
    def solution(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            # res[left:last] + last bit
            res[i] = res[i >> 1] + (i & 1)
        return res

