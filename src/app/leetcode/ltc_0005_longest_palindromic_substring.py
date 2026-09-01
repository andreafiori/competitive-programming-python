"""
Longest Palindromic Substring | leetcode 5 | https://leetcode.com/problems/longest-palindromic-substring

"""

class LongestPalindromicSubstring:
    def solution(self, s, left, right):
        ls = len(s)
        while (left >= 0 and right < ls and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1
