"""
Peak Index in a Mountain Array | leetcode 852 | https://leetcode.com/problems/peak-index-in-a-mountain-array/

"""

class PeakIndexInAMountainArray:
    def solution_one(self, a: list) -> int:
        """
        :type a: List[int]
        :rtype: int
        """
        i = 0
        while a[i + 1] >= a[i]:
            i += 1
        return i

    def solution_two(self, a: list) -> int:
        lo, hi = 0, len(a) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < a[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
