"""
Leetcode Problem 44: Wildcard Matching | https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Constraints:
0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

"""

class WildcardMatching:

    def solution(self, s: str, p: str) -> bool:
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_index, p_index = 0, 0
        star, s_star = -1, 0
        s_len, p_len = len(s), len(p)
        while s_index < s_len:
            if p_index < p_len and (s[s_index] == p[p_index] or p[p_index] == '?'):
                s_index += 1
                p_index += 1
            elif p_index < p_len and p[p_index] == '*':
                star = p_index
                s_star = s_index
                p_index += 1
            elif star != -1:
                p_index = star + 1
                s_star += 1
                s_index = s_star
            else:
                return False
        while p_index < p_len and p[p_index] == '*':
            p_index += 1
        return p_index == p_len
