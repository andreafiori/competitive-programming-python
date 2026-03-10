"""
Unique Word Abbreviation | https://leetcode.com/problems/unique-word-abbreviation/
"""
class UniqueWordAbbreviation:
    def __init__(self, dictionary: list[str]):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dictionary = set(dictionary)
        self.abb_dic = {}
        for s in self.dictionary:
            curr = self.getAbb(s)
            if curr in self.abb_dic:
                self.abb_dic[curr] = False
            else:
                self.abb_dic[curr] = True

    def isUnique(self, word: str) -> bool:
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abb = self.getAbb(word)
        hasAbbr = self.abb_dic.get(abb, None)
        return hasAbbr == None or (hasAbbr and word in self.dictionary)

    def getAbb(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
