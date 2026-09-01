"""
Leetcode Problem 140: Word Break II | https://leetcode.com/problems/word-break-ii/

"""

class WordBreakII:

    def __init__(self):
        self.memo = {}

    def solution(self, s, word_dict):
        """
        :type s: str
        :type word_dict: Set[str]
        :rtype: List[str]
        """
        try:
            return self.memo[s]
        except KeyError:
            pass
        result = []
        if s in word_dict:
            result.append(s)
        for i in range(1, len(s)):
            word = s[i:]
            if word in word_dict:
                rem = s[:i]
                prev = self.solution(rem, word_dict)
                result.extend([res + ' ' + word for res in prev])
        self.memo[s] = result
        return result
