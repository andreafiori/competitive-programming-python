"""
Power of Two | https://leetcode.com/problems/power-of-two/
"""
class PowerOfTwo:
    """ Check if a number is a power of two. """

    def isPowerOfTwo(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        bin_str = bin(n)
        return sum(map(lambda x: int(x), list(bin_str[2:]))) == 1
