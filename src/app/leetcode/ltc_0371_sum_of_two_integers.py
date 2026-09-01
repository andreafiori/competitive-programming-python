"""
Leetcode Problem: 371. Sum of Two Integers | https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000

"""

import ctypes

class SumOfTwoIntegers:

    def solution(self, a: int, b: int) -> int:
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        _sum = 0
        carry = ctypes.c_int32(b)
        while carry.value != 0:
            _sum = a ^ carry.value
            carry = ctypes.c_int32(a & carry.value)
            carry.value <<= 1
            a = _sum
        return _sum
