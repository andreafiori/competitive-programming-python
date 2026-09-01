"""
Leetcode Problem: 905. Sort Array By Parity | https://leetcode.com/problems/sort-array-by-parity/

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000

"""

class SortArrayByParity:

    def solution(self, a: list[int]) -> list[int]:
        lo, hi = 0, len(a) - 1
        while lo < hi:
            if a[lo] % 2 > a[hi] % 2:
                a[lo], a[hi] = a[hi], a[lo]
            if a[lo] % 2 == 0: lo += 1
            if a[hi] % 2 == 1: hi -= 1
        return a
