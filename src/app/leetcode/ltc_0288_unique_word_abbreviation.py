"""
Leetcode 288. Unique Word Abbreviation | https://leetcode.com/problems/unique-word-abbreviation/
"""

class ValidWordAbbr:

    def __init__(self, dictionary: list[str]):
        """
        initialize your data structure here.
        :type dictionary: list[str]
        """
        self.dictionary = set(dictionary)
        self.abb_dic = {}
        for s in self.dictionary:
            curr = self.get_abb(s)
            if curr in self.abb_dic:
                self.abb_dic[curr] = False
            else:
                self.abb_dic[curr] = True

    def solution(self, word: str) -> bool:
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abb = self.get_abb(word)
        has_abbr = self.abb_dic.get(abb, None)
        return has_abbr == None or (has_abbr and word in self.dictionary)


    def get_abb(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
