"""
Valid Word Abbreviation | https://leetcode.com/problems/valid-word-abbreviation/
"""
class ValidWordAbbreviation(object):

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """Check if the given abbreviation is valid for the given word."""
        pos = curr = 0
        for i in range(len(abbr)):
            try:
                num = int(abbr[i])
                if num == 0 and curr == 0:
                    return False
                curr = curr * 10 + num
            except ValueError:
                pos += curr
                curr = 0
                if pos >= len(word):
                    return False
                if word[pos] != abbr[i]:
                    return False
                pos += 1
        pos += curr
        if pos == len(word):
            return True
        return False
