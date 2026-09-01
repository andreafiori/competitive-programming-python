"""
Number of 1 Bits | leetcode 191 | https://leetcode.com/problems/number-of-1-bits/

"""

class NumberOf1Bits:

    def solution(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
