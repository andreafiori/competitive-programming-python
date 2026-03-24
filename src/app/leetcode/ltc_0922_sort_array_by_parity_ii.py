"""
Sort Array By Parity II | https://leetcode.com/problems/sort-array-by-parity-ii/
"""
class SortArrayByParityII:

    def sort(self, A):
        odd = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[odd] % 2:
                    odd += 2
                A[i], A[odd] = A[odd], A[i]
        return A
