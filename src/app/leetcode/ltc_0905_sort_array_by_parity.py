"""
Sort Array By Parity | https://leetcode.com/problems/sort-array-by-parity/
"""
class SortArrayByParity:

    def sort(self, A: list[int]) -> list[int]:
        # Quit like quick sort or quick selection
        lo, hi = 0, len(A) - 1
        while lo < hi:
            if A[lo] % 2 > A[hi] % 2:
                A[lo], A[hi] = A[hi], A[lo]
            if A[lo] % 2 == 0: lo += 1
            if A[hi] % 2 == 1: hi -= 1
        return A
