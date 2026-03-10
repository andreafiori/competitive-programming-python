"""
Word Pattern | https://leetcode.com/problems/word-pattern/
"""
class WordPattern:
    """:type pattern: str"""

    def wordPattern(self, pattern: str, s: str) -> bool:
        """ :type s: str :rtype: bool """
        vocab = dict()
        seens = dict()
        sent = s.split(" ")

        if len(sent) != len(pattern):
            return False

        for i in range(len(pattern)):
            i_patt = pattern[i]
            i_sent = sent[i]

            if vocab.get(i_patt):
                if vocab[i_patt] != i_sent:
                    return False
            else:
                if seens.get(i_sent):
                    return False
                vocab[i_patt] = i_sent
                seens[i_sent] = True

        return True