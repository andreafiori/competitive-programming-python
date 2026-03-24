"""
Palindrome Partitioning | https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.

"""
class PalindromePartitioning:

    def partition(self, s: str) -> list:
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        curr = []
        self.recur_partition(result, curr, s, 0)
        return result

    def recur_partition(self, result: list, curr: list, s: str, start: int):
        if start == len(s):
            result.append(list(curr))
        for i in range(start, len(s)):
            if self.is_palindrome(s, start, i):
                curr.append(s[start:i + 1])
                self.recur_partition(result, curr, s, i + 1)
                curr.pop()

    def is_palindrome(self, s: str, begin: int, end: int) -> bool:
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True