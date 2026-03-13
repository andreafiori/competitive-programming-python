"""
. Reverse Words in a String III | https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""
class RevereseWordsInAStringIII:

    def reverse_words(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word[::-1] for word in s.split(' ')])
