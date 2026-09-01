"""
Leetcode Problem: 242. Valid Anagram | https://leetcode.com/problems/valid-anagram/

"""

class ValidAnagram:

    def solution(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for num in counter:
            if num != 0:
                return False
        return True