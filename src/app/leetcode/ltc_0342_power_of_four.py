"""
Power of Four | https://leetcode.com/problems/power-of-four/
"""
class PowerOfFour(object):

    def is_power_of_four(self, num: int) -> bool:
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num-1) == 0 and len(bin(num)[3:]) % 2 == 0
