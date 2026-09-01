"""
Leetcode Problem: 867. Transpose Matrix | https://leetcode.com/problems/transpose-matrix/
"""

from typing import List

class Solution:

    def transpose(self, a: List[List[int]]) -> List[List[int]]:
        """
        :type a: List[List[int]]
        """
        R, C = len(a), len(a[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(a):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
