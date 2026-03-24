"""
Peak Index in a Mountain Array | http://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
class PeakIndexInMountainArray:

    def peak_index(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
