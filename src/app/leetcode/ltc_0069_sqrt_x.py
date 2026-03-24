"""
Sqrt(x) | https://leetcode.com/problems/sqrtx/
"""
class SqrtX:

    def sqrt_x(self, x: int) -> int:
        start = 0
        end = x

        while start + 1 < end:
            mid = start + (end - start) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid

        if end * end == x:
            return end

        return start

    def sqrt(self, x: int) -> int:
        # sqrt(x) = 2 * sqrt(x / 4) for n % 4 == 0
        # sqrt(x) = 1 + 2 * sqrt(x / 4) for n % 4 != 0
        if x == 0:
            return 0
        if x < 4:
            return 1
        res = 2 * self.sqrt(x / 4)
        # (res + 1) * (res + 1) >= 0 for avoiding overflow
        if (res + 1) * (res + 1) <= x and (res + 1) * (res + 1) >= 0:
            return res + 1
        return  res
