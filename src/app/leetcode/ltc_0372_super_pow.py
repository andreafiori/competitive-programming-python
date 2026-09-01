"""
LeetCode Problem: 372. Super Pow | https://leetcode.com/problems/super-pow/

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:
Input: a = 2, b = [3]
Output: 8

Example 2:
Input: a = 2, b = [1,0]
Output: 1024

Example 3:
Input: a = 1, b = [4,3,3,8,5,2]
Output: 1

Constraints:
1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b does not contain leading zeros.

"""

class SuperPow:

    def __init__(self):
        self.base = 1337

    def solution(self, a: int, b: list[int]) -> int:
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if b is None or len(b) == 0:
            return 1
        last_digit = b.pop()
        return self._pow_mod(self.solution(a, b), 10) * \
            self._pow_mod(a, last_digit) % self.base

    def _pow_mod(self, a: int, k: int) -> int:
        a %= self.base
        result = 1
        for _ in range(k):
            result = (result * a) % self.base
        return result
