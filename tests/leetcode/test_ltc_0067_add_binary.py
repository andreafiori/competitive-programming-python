"""
Add Binary | LeetCode 67 | https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""

from app.leetcode.ltc_0067_add_binary import AddBinary

class TestAddBinary:
    def test_solution(self):
        assert AddBinary().solution_one("11", "1") == "100"
