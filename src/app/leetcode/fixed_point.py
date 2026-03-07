"""
Fixed Point | https://leetcode.com/problems/fixed-point/

"""

class FixedPoint:

    def fix(self, A):
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
