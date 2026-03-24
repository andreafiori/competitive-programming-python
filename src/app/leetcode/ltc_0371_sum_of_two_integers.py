"""
Sum of Two Integers | https://leetcode.com/problems/sum-of-two-integers/

https://leetcode.com/discuss/111705/one-positive-one-negative-case-successful-for-python-rules
"""
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        import ctypes
        sum = 0
        carry = ctypes.c_int32(b)
        while carry.value != 0:
            sum = a ^ carry.value
            carry = ctypes.c_int32(a & carry.value)
            carry.value <<= 1
            a = sum
        return sum