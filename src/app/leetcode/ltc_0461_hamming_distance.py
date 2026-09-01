"""
Hamming Distance | leetcode 461 | https://leetcode.com/problems/hamming-distance/

"""

class HammingDistance:

    def solution(self, x: int, y: int) -> int:
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
