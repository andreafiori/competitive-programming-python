"""
Number of 1 Bits | http://leetcode.com/problems/number-of-1-bits/
"""
class NumberOf1Bits:
    # def hammingWeight(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     # using bin
    #     s_n = bin(n)[2:]
    #     return s_n.count('1')

    def hamming_weight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://leetcode.com/articles/number-1-bits/
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
