"""
Leetcode Problem: 557. Reverse Words in a String III | https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

class ReverseWordsInAStringIII:

    def solution(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word[::-1] for word in s.split(' ')])
