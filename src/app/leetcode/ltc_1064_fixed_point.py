"""
Fixed Point Fixed Point | https://leetcode.com/problems/fixed-point/
"""
class FixedPoint:
    """ Fixed Point """

    def fix(self, A: list[int]) -> int:
        """ @return: return the fixed point of A, return -1 if it does not exist """
        l, h = 0, len(A) - 1
        while l <= h:
            mid = (l + h) // 2
            if A[mid] < mid:
                l = mid + 1
            elif A[mid] > mid:
                h = mid - 1
            else:
                return mid
        return -1
