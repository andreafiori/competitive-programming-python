"""
LeetCode Problem: 977. Squares of a Sorted Array | https://leetcode.com/problems/squares-of-a-sorted-array/
"""

class SquaresOfSortedArray:

    def solution(self, a: list[int]) -> list[int]:
        pos = 0
        while pos < len(a) and a[pos] < 0:
            pos += 1
        # pos points to first positive
        # npos points to largest negative
        npos = pos - 1
        res = []
        while pos < len(a) and npos >= 0:
            if a[npos] ** 2 < a[pos] ** 2:
                res.append(a[npos] ** 2)
                npos -= 1
            else:
                res.append(a[pos] ** 2)
                pos +=1 
        while npos >= 0:
            res.append(a[npos] ** 2)
            npos -= 1
        while pos < len(a):
            res.append(a[pos] ** 2)
            pos += 1
        return res
