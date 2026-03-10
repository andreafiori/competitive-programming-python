"""
Pow(x, n) | https://leetcode.com/problems/powx-n/
"""
class PowXN:
    def my_pow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        temp = pow(x, n / 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x

    def my_pow2(self, x, n):
        """ """
        if n == 0:
            return 1
        res ,curr = 1, abs(n)
        while curr > 0:
            if curr & 1 == 1:
                res *= x
            curr >>= 1
            x *= x
        if n < 0:
            return 1 / res
        return  res
