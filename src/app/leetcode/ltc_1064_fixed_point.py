"""
Fixed Point | leetcode 1064 | https://leetcode.com/problems/fixed-point/

"""

class FixedPoint:

    def fix(self, a: list[int]) -> int:
        """
        :param a: list[int]
        :return: int
        """
        l, h = 0, len(a) - 1
        while l <= h:
            mid = (l + h) // 2
            if a[mid] < mid:
                l = mid + 1
            elif a[mid] > mid:
                h = mid - 1
            else:
                return mid
        return -1
