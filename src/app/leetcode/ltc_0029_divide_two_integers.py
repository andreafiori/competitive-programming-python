"""
Divide two integers without using multiplication, division and mod operator. | https://leetcode.com/problems/divide-two-integers/
"""

import math

class DivideTwoIntegers:
    MAX_INT = int(100000)

    def divide(self, dividend, divisor):
        if divisor == 0:
            return self.MAX_INT
        if dividend == 0:
            return 0
        isPositive = (dividend < 0) == (divisor < 0)
        m = abs(dividend)
        n = abs(divisor)
        # ln and exp
        res = math.log(m) - math.log(n)
        res = int(math.exp(res))
        if isPositive:
            return min(res, 2147483647)
        return max(0 - res, -2147483648)
